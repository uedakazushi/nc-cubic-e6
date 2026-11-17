#!/usr/bin/env python3
"""Package current research, three PDFs and reproducibility assets.

No previous bundles, Git database, logs, caches, or external literature PDFs
are included. Run make papers first; this script rejects stale PDFs.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "publication-v33"
DATE = "2026-11-18"
PAPERS = ("nc-cubic-e6", "fricke-geometry", "cubic-boundary-prym")
PREFIX = f"nc-cubic-e6-{VERSION}-{DATE.replace('-', '')}"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "build" / f"{PREFIX}.zip")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "computations/verify_sources.py")],
                   cwd=ROOT, check=True)
    sys.path.insert(0, str(ROOT / "computations"))
    from verify_sources import expand

    entries = {}
    fixed = ("README.md", "00_research_plan.md", "AGENTS.md", "Makefile",
             ".latexmkrc", "papers/.latexmkrc", ".gitignore", ".vscode/settings.json",
             "research/publication_status.md")
    for name in fixed:
        path = ROOT / name
        if not path.is_file():
            raise RuntimeError(f"required source missing: {name}")
        entries[name] = path
    for folder, suffixes in (("papers", {".tex"}), ("research", {".md"}),
                             ("computations", {".py", ".json", ".txt"}),
                             ("scripts", {".py"})):
        for path in (ROOT / folder).rglob("*"):
            if path.is_file() and path.suffix in suffixes and "__pycache__" not in path.parts:
                entries[path.relative_to(ROOT).as_posix()] = path

    for name in PAPERS:
        sources, _ = expand(ROOT / "papers" / f"{name}.tex")
        pdf = ROOT / "build" / f"{name}.pdf"
        if not pdf.is_file():
            raise RuntimeError(f"missing PDF: {pdf.name}; run make papers")
        if pdf.stat().st_mtime < max(path.stat().st_mtime for path in sources):
            raise RuntimeError(f"stale PDF: {pdf.name}; run make papers")
        data = pdf.read_bytes()
        if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-2048:]:
            raise RuntimeError(f"invalid PDF container: {pdf.name}")
        entries[f"pdf/{name}.pdf"] = pdf

    validation = json.loads((ROOT / "computations/validation.json").read_text())
    if validation.get("status") != "PASS" or len(validation.get("completed", [])) != 36:
        raise RuntimeError("current 36-validator PASS manifest is required")
    # Validators/helpers must match the actual run. The runner's recorded hash
    # remains provenance even if its reporting was improved after that run.
    for item in validation["completed"]:
        path = ROOT / "computations" / item["script"]
        if digest(path) != item["source_sha256"]:
            raise RuntimeError(f"validator changed since recorded run: {item['script']}")
    for name, expected in validation.get("support_source_sha256", {}).items():
        if digest(ROOT / "computations" / name) != expected:
            raise RuntimeError(f"support source changed since recorded run: {name}")

    comparison = json.loads((ROOT / "computations/r13_comparison_certificate.json").read_text())
    if comparison.get("status") != "PASS" or comparison.get("source_sha256") != digest(
            ROOT / "computations/verify_r13_comparison.py"):
        raise RuntimeError("current R13 comparison certificate is required; run make comparison")

    manifest = {
        "version": VERSION, "date": DATE,
        "start_here": "00_research_plan.md",
        "scope": "Current research sources, three PDFs and reproducibility assets.",
        "mathematical_verification": "See research/publication_status.md; not independent peer review.",
        "files": [{"path": name, "size_bytes": path.stat().st_size,
                   "sha256": digest(path)} for name, path in sorted(entries.items())],
    }
    out = args.output.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = out.with_suffix(".zip.tmp")
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, path in sorted(entries.items()):
            archive.write(path, f"{PREFIX}/{name}")
        archive.writestr(f"{PREFIX}/bundle_manifest.json",
                         json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    with zipfile.ZipFile(temporary) as archive:
        failed = archive.testzip()
        if failed:
            raise RuntimeError(f"ZIP integrity failure: {failed}")
        for item in manifest["files"]:
            data = archive.read(f"{PREFIX}/{item['path']}")
            if hashlib.sha256(data).hexdigest() != item["sha256"]:
                raise RuntimeError(f"packaged-byte mismatch: {item['path']}")
    temporary.replace(out)
    print(json.dumps({"status": "PASS", "file": str(out),
                      "files": len(entries) + 1, "bytes": out.stat().st_size,
                      "sha256": digest(out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
