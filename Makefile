PYTHON ?= python3
LATEXMK ?= latexmk
PAPERS = nc-cubic-e6 fricke-geometry cubic-boundary-prym

.PHONY: all papers sources verify bundle clean
all: papers

sources:
	$(PYTHON) computations/verify_sources.py

verify:
	$(PYTHON) computations/verify_all.py

papers: sources
	@set -e; for paper in $(PAPERS); do \
		$(LATEXMK) -r .latexmkrc -lualatex papers/$$paper.tex; \
	done

bundle: papers
	$(PYTHON) scripts/build_bundle.py

clean:
	@set -e; for paper in $(PAPERS); do \
		$(LATEXMK) -r .latexmkrc -c papers/$$paper.tex; \
	done
