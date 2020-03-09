all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/vorbereitung.pdf: python-skripts/vorbereitung.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/vorbereitung.py

build/stabi-2konfokal.pdf: python-skripts/stabi.py data/2konkav.csv data/konkav-planar.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/stabi.py
build/stabi-konfokal-planar.pdf: build/stabi-2konfokal.pdf

build/tem00.pdf: python-skripts/moden.py data/tem00.csv data/tem10.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/moden.py
build/tem00-mu.tex: build/tem00.pdf
build/tem00-sigma.tex: build/tem00.pdf
build/tem00-a.tex: build/tem00.pdf
build/tem10.pdf: build/tem00.pdf
build/tem10-mua.tex: build/tem00.pdf
build/tem10-mub.tex: build/tem00.pdf
build/tem10-a.tex: build/tem00.pdf
build/tem10-b.tex: build/tem00.pdf


build/polar.pdf: python-skripts/polar.py data/polarisation.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/polar.py

build/gitter100.tex: python-skripts/wellenlaenge.py | build
	python python-skripts/wellenlaenge.py
build/gitter100.txt: build/gitter100.tex
build/gitter80.tex: build/gitter100.tex
build/gitter80.txt: build/gitter100.tex

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/vorbereitung.pdf \
	build/stabi-2konfokal.pdf \
	build/stabi-konfokal-planar.pdf \
	build/tem00.pdf \
	build/tem00-mu.tex \
	build/tem00-sigma.tex \
	build/tem00-a.tex \
	build/tem10.pdf \
	build/tem10-mua.tex \
	build/tem10-mub.tex \
	build/tem10-a.tex \
	build/tem10-b.tex \
	build/polar.pdf \
	build/gitter100.tex \
	build/gitter100.txt \
	build/gitter80.tex \
	build/gitter80.txt

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

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
