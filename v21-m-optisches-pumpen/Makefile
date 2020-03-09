all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/messung-b.tex: python-skripts/messung-b.py | build
	python python-skripts/messung-b.py


build/messung-c.csv: python-skripts/messung-c.py data/messung-c.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/messung-c.py
build/messung-c-m1.tex: build/messung-c.csv
build/messung-c-b1.tex: build/messung-c.csv
build/messung-c-m2.tex: build/messung-c.csv
build/messung-c-b2.tex: build/messung-c.csv
build/messung-c-m3.tex: build/messung-c.csv
build/messung-c-b3.tex: build/messung-c.csv

build/messung-c-gf2.tex: build/messung-c.csv
build/messung-c-gf3.tex: build/messung-c.csv
build/messung-c-i2.tex: build/messung-c.csv
build/messung-c-i3.tex: build/messung-c.csv

build/messung-h-dE2.tex: build/messung-c.csv
build/messung-h-dE3.tex: build/messung-c.csv

build/messung-c.pdf: build/messung-c.csv


build/messung-i.pdf: python-skripts/messung-i.py data/messung-i.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/messung-i.py
build/messung-i-a1.tex: build/messung-i.pdf
build/messung-i-b1.tex: build/messung-i.pdf
build/messung-i-c1.tex: build/messung-i.pdf

build/messung-i-a2.tex: build/messung-i.pdf
build/messung-i-b2.tex: build/messung-i.pdf
build/messung-i-c2.tex: build/messung-i.pdf

build/messung-i-bb.tex: build/messung-i.pdf

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: \
	build/messung-b.tex \
	build/messung-c.csv \
	build/messung-c-m1.tex \
	build/messung-c-b1.tex \
	build/messung-c-m2.tex \
	build/messung-c-b2.tex \
	build/messung-c-m3.tex \
	build/messung-c-b3.tex \
	build/messung-c-gf2.tex \
	build/messung-c-gf3.tex \
	build/messung-c-i2.tex \
	build/messung-c-i3.tex \
	build/messung-c.pdf \
	build/messung-h-dE2.tex \
	build/messung-h-dE3.tex \
	build/messung-i.pdf \
	build/messung-i-a1.tex \
	build/messung-i-b1.tex \
	build/messung-i-c1.tex \
	build/messung-i-a2.tex \
	build/messung-i-b2.tex \
	build/messung-i-c2.tex \
	build/messung-i-bb.tex

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
		--interaction=batchmode \
		--halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
