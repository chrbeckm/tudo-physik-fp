all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/p-m1.pdf: python-skripts/m1.py $(pyf) data/m1.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/m1.py
build/p-m1.csv: build/p-m1.pdf
build/p-m1.tex: build/p-m1.csv python-skripts/m1.sh
	bash python-skripts/m1.sh

build/p-m3-werte.tex: python-skripts/m3.py $(pyf) data/m3.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/m3.py
build/p-m3-phase.tex: build/p-m3-werte.tex
build/p-m3-n10.tex: build/p-m3-werte.tex
build/p-m3-n9.tex: build/p-m3-werte.tex

build/p-m4-werte.csv: python-skripts/m4.py $(pyf) data/m4.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/m4.py
build/p-m4-behbrech.csv: build/p-m4-werte.csv
build/p-m4-fit.csv: build/p-m4-werte.csv
build/p-m4-amean.tex: build/p-m4-werte.csv
build/p-m4-bmean.tex: build/p-m4-werte.csv
build/p-m4-normbrech.tex: build/p-m4-werte.csv
build/p-m4-1.pdf: build/p-m4-werte.csv
build/p-m4-2.pdf: build/p-m4-werte.csv
build/p-m4-3.pdf: build/p-m4-werte.csv
build/p-m4-4.pdf: build/p-m4-werte.csv
build/p-m4-werte.tex: build/p-m4-werte.csv build/p-m4-behbrech.csv build/p-m4-fit.csv python-skripts/m4.sh | build
	bash python-skripts/m4.sh
build/p-m4-behbrech.tex: build/p-m4-werte.tex
build/p-m4-fit.tex: build/p-m4-werte.tex

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: \
	build/p-m1.pdf \
	build/p-m1.csv \
	build/p-m1.tex \
	build/p-m3-werte.tex \
	build/p-m3-phase.tex \
	build/p-m3-n10.tex \
	build/p-m3-n9.tex \
	build/p-m4-werte.csv \
	build/p-m4-werte.tex \
	build/p-m4-behbrech.csv \
	build/p-m4-behbrech.tex \
	build/p-m4-amean.tex \
	build/p-m4-bmean.tex \
	build/p-m4-fit.csv \
	build/p-m4-fit.tex \
	build/p-m4-normbrech.tex \
	build/p-m4-1.pdf \
	build/p-m4-2.pdf \
	build/p-m4-3.pdf \
	build/p-m4-4.pdf

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
