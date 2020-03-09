all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/p-messung-a.pdf: python-skripts/messung-a.py data/messung-a.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/messung-a.py

build/p-messung-b.pdf: python-skripts/messung-b.py data/messung-b.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/messung-b.py
build/p-messung-b-diff.pdf: build/p-messung-b.pdf
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: \
	build/p-messung-a.pdf \
	build/p-messung-b.pdf \
	build/p-messung-b-diff.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
		--interaction=batchmode \
		--halt-on-error \
	main.tex

preview: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
		-pvc \
	  --lualatex \
	  --output-directory=build \
		--interaction=nonstopmode \
		--halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
