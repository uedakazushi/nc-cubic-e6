#!/usr/bin/env python3
"""Check the static TeX source graph, labels, citations and external references.

This check does not replace LuaLaTeX or inspect mathematical assertions. Run it
from any directory. External-document references are resolved against their
source manuscripts, so a clean checkout does not need pre-existing aux files.
"""
from pathlib import Path
from collections import Counter
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INPUT = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|pageref|autoref|nameref|[cC]ref)\*?\s*\{([^{}]+)\}")
HYPERREF = re.compile(r"\\hyperref\s*\[([^\[\]]+)\]")
CITE = re.compile(r"\\cite\w*\*?\s*(?:\[[^\[\]]*\]\s*)*\{([^{}]+)\}")
BIBITEM = re.compile(r"\\bibitem\s*(?:\[[^\[\]]*\]\s*)?\{([^{}]+)\}")
EXTERNAL = re.compile(r"\\externaldocument\s*(?:\[([^\[\]]*)\])?\s*\{([^{}]+)\}")
SELECTED_BIB = re.compile(r"\\UsePublicationReferences\s*\{([^{}]+)\}")


def read(path):
    # TeX comments are excluded; escaped percent signs are retained.
    return re.sub(r"(?<!\\)%[^\n]*", "", path.read_text(encoding="utf-8"))


def expand(path, stack=()):
    if path in stack:
        raise ValueError("input cycle: " + " -> ".join(str(p.relative_to(ROOT)) for p in (*stack, path)))
    source = read(path)
    files = [path]
    pieces = [source]
    for name in INPUT.findall(source):
        if "\\" in name or "#" in name:
            raise ValueError(f"unsupported dynamic input in {path.relative_to(ROOT)}: {name}")
        candidate = Path(name)
        if not candidate.suffix:
            candidate = candidate.with_suffix(".tex")
        options = [ROOT / candidate, path.parent / candidate]
        child = next((p.resolve() for p in options if p.is_file()), None)
        if child is None:
            raise ValueError(f"missing input in {path.relative_to(ROOT)}: {name}")
        child_files, child_source = expand(child, (*stack, path))
        files.extend(child_files)
        pieces.append(child_source)
    return files, "\n".join(pieces)


def split_keys(values):
    return {key.strip() for value in values for key in value.split(",")
            if key.strip() and "#" not in key and "\\" not in key}


def main():
    papers = sorted(p for p in (ROOT / "papers").glob("*.tex")
                    if "\\begin{document}" in read(p))
    if not papers:
        print("FAIL: no manuscript roots", file=sys.stderr)
        return 1
    expanded = {}
    for paper in papers:
        try:
            expanded[paper.stem] = expand(paper)
        except ValueError as exc:
            print(f"FAIL: {exc}", file=sys.stderr)
            return 1
    errors = []
    used_files = set()
    for paper in papers:
        files, text = expanded[paper.stem]
        root_text = read(paper)
        if len(re.findall(r"\\documentclass\b", root_text)) != 1:
            errors.append(f"{paper.name}: manuscript must contain its own documentclass")
        if len(re.findall(r"\\documentclass\b", text)) != 1:
            errors.append(f"{paper.name}: duplicate/missing documentclass across inputs")
        raw_root = paper.read_text(encoding="utf-8")
        if f"% !TeX root = {paper.name}" not in raw_root:
            errors.append(f"{paper.name}: missing explicit editor root")
        if re.search(r"^%\s*!TeX\s+program\s*=", raw_root, re.M | re.I):
            errors.append(f"{paper.name}: TeX-program comment bypasses the latexmk recipe")
        used_files.update(files)
        labels = LABEL.findall(text)
        duplicates = sorted(key for key, count in Counter(labels).items() if count > 1)
        available = set(labels)
        for prefix, name in EXTERNAL.findall(text):
            stem = Path(name).name
            if stem.endswith(".aux"):
                stem = stem[:-4]
            if stem not in expanded:
                errors.append(f"{paper.name}: unknown external manuscript {name}")
                continue
            external_labels = {prefix + key for key in LABEL.findall(expanded[stem][1])}
            collisions = available & external_labels
            if collisions:
                errors.append(f"{paper.name}: external label collisions: {sorted(collisions)}")
            available.update(external_labels)
        refs = split_keys(REF.findall(text) + HYPERREF.findall(text))
        citations = split_keys(CITE.findall(text))
        bibliography = BIBITEM.findall(text)
        selected_groups = SELECTED_BIB.findall(text)
        selected_bib = split_keys(selected_groups)
        if selected_groups and citations - selected_bib:
            errors.append(f"{paper.name}: citations omitted by bibliography filter: "
                          f"{sorted(citations - selected_bib)}")
        if selected_bib - set(bibliography):
            errors.append(f"{paper.name}: selected bibliography entries do not exist: "
                          f"{sorted(selected_bib - set(bibliography))}")
        if duplicates:
            errors.append(f"{paper.name}: duplicate labels: {duplicates}")
        bib_duplicates = sorted(key for key, count in Counter(bibliography).items() if count > 1)
        if bib_duplicates:
            errors.append(f"{paper.name}: duplicate bibliography keys: {bib_duplicates}")
        if refs - available:
            errors.append(f"{paper.name}: unresolved references: {sorted(refs - available)}")
        if citations - set(bibliography):
            errors.append(f"{paper.name}: unresolved citations: {sorted(citations - set(bibliography))}")
        print(f"{paper.name}: {len(set(files))} source files, {len(labels)} labels, "
              f"{len(refs)} referenced labels, {len(citations)} cited works")
    unused = sorted(p.relative_to(ROOT).as_posix()
                    for p in (ROOT / "papers" / "sections").glob("*.tex")
                    if p.resolve() not in used_files)
    if unused:
        print("Supplementary section sources not included by manuscript roots: " + ", ".join(unused))
    if errors:
        print("\n".join("FAIL: " + e for e in errors), file=sys.stderr)
        return 1
    print("SOURCE GRAPH PASS (static structure only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
