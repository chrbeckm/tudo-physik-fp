all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/p-temperatur.csv: python-skripts/auswertung.py data/messwerte.csv build/p-alphafit.csv | build
	python python-skripts/auswertung.py
build/p-cees.csv: build/p-temperatur.csv

build/p-temperatur.pdf: build/p-temperatur.csv python-skripts/temperatur-plot.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/temperatur-plot.py

build/p-alphafit.csv: data/alphafit.csv python-skripts/alphafit.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/alphafit.py
	sed -i 's|+/-|, |g' build/p-alphafit.csv
build/p-alphafit.pdf: build/p-alphafit.csv

build/p-cv.pdf: build/p-cees.csv python-skripts/cv.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/cv.py
build/p-cp.pdf: build/p-cees.csv python-skripts/cp.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/cp.py

build/p-debye.tex: data/debye.csv python-skripts/debye.py | build
	python python-skripts/debye.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/p-temperatur.pdf \
	build/p-alphafit.pdf \
	build/p-cv.pdf \
	build/p-cp.pdf \
	build/p-debye.tex

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
