all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex
data = data/messung-1.csv data/messung-2.csv
# hier Python-Skripte:
build/p-temperatur.pdf: python-skripts/temperatur.py $(pyf) $(data) | build
	TEXINPUTS=$$(pwd): python python-skripts/temperatur.py

build/p-strom.pdf: python-skripts/strom.py $(pyf) $(data) | build
	TEXINPUTS=$$(pwd): python python-skripts/strom.py

build/p-korrelation.pdf: python-skripts/korrelation.py $(pyf) $(data) | build
	TEXINPUTS=$$(pwd): python python-skripts/korrelation.py

build/p-korrektur-1.pdf: python-skripts/korrektur-1.py $(pyf) data/messung-1.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/korrektur-1.py
build/p-korrektur-1-a.tex: build/p-korrektur-1.pdf
build/p-korrektur-1-b.tex: build/p-korrektur-1.pdf
build/p-messwerte-1.csv: build/p-korrektur-1.pdf

build/p-korrektur-2.pdf: python-skripts/korrektur-2.py $(pyf) data/messung-2.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/korrektur-2.py
build/p-korrektur-2-a.tex: build/p-korrektur-2.pdf
build/p-korrektur-2-b.tex: build/p-korrektur-2.pdf
build/p-messwerte-2.csv: build/p-korrektur-2.pdf

build/p-rate-m-1.tex: python-skripts/aktivierung-1.py $(pyf) build/p-messwerte-1.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/aktivierung-1.py
build/p-rate-b-1.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-1-m.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-1-b.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-1-W.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-1-W-eV.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-1.pdf: build/p-rate-m-1.tex
build/p-aktivierung-1-stromr-1.pdf: build/p-rate-m-1.tex
build/p-akt-1-meth-2-m.tex: build/p-rate-m-1.tex
build/p-atk-1-meth-2-b.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-2-W.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-methode-2-W-eV.tex: build/p-rate-m-1.tex
build/p-aktivierung-1-fit-1.pdf: build/p-rate-m-1.tex

build/p-rate-m-2.tex: python-skripts/aktivierung-2.py $(pyf) build/p-messwerte-2.csv | build
	TEXINPUTS=$$(pwd): python python-skripts/aktivierung-2.py
build/p-rate-b-2.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-1-m.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-1-b.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-1-W.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-1-W-eV.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-1.pdf: build/p-rate-m-2.tex
build/p-aktivierung-2-stromr-1.pdf: build/p-rate-m-2.tex
build/p-akt-2-meth-2-m.tex: build/p-rate-m-2.tex
build/p-atk-2-meth-2-b.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-2-W.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-methode-2-W-eV.tex: build/p-rate-m-2.tex
build/p-aktivierung-2-fit-1.pdf: build/p-rate-m-2.tex

build/p-taukurve1.pdf: python-skripts/relaxation.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/relaxation.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/p-temperatur.pdf \
	build/p-strom.pdf \
	build/p-korrelation.pdf \
	build/p-korrektur-1.pdf \
	build/p-korrektur-1-a.tex \
	build/p-korrektur-1-b.tex \
	build/p-messwerte-1.csv \
	build/p-korrektur-2.pdf \
	build/p-korrektur-2-a.tex \
	build/p-korrektur-2-b.tex \
	build/p-messwerte-2.csv \
	build/p-rate-m-1.tex \
	build/p-rate-b-1.tex \
	build/p-aktivierung-1-methode-1-m.tex \
	build/p-aktivierung-1-methode-1-b.tex \
	build/p-aktivierung-1-methode-1-W.tex \
	build/p-aktivierung-1-methode-1-W-eV.tex \
	build/p-aktivierung-1-methode-1.pdf \
	build/p-aktivierung-1-stromr-1.pdf \
	build/p-akt-1-meth-2-m.tex \
	build/p-atk-1-meth-2-b.tex \
	build/p-aktivierung-1-methode-2-W.tex \
	build/p-aktivierung-1-methode-2-W-eV.tex \
	build/p-aktivierung-1-fit-1.pdf \
	build/p-rate-m-2.tex \
	build/p-rate-b-2.tex \
	build/p-aktivierung-2-methode-1-m.tex \
	build/p-aktivierung-2-methode-1-b.tex \
	build/p-aktivierung-2-methode-1-W.tex \
	build/p-aktivierung-2-methode-1-W-eV.tex \
	build/p-aktivierung-2-methode-1.pdf \
	build/p-aktivierung-2-stromr-1.pdf \
	build/p-akt-2-meth-2-m.tex \
	build/p-atk-2-meth-2-b.tex \
	build/p-aktivierung-2-methode-2-W.tex \
	build/p-aktivierung-2-methode-2-W-eV.tex \
	build/p-aktivierung-2-fit-1.pdf \
	build/p-taukurve1.pdf

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
