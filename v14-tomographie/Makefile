all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex

# hier Python-Skripte:
build/spektrum.pdf: python-skripts/spektrum.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/spektrum.py
build/spektrum.csv: build/spektrum.pdf

build/wuerfel-1-daten.tex: python-skripts/wuerfel.py python-skripts/csv-conv.py data/wuerfel-*.csv | build
	python python-skripts/wuerfel.py
	sed -i 's|+/-| \& |g' build/wuerfel-1-daten.csv
	sed -i 's|+/-| \& |g' build/wuerfel-1-aluminium-abschwaechung.csv
	sed -i 's|+/-| \& |g' build/wuerfel-2-daten.csv
	sed -i 's|+/-| \& |g' build/wuerfel-3-daten.csv
	sed -i 's|+/-| \& |g' build/wuerfel-5.csv
	sed -i 's|+/-| \& |g' build/wuerfel-5-daten.csv
	python python-skripts/csv-conv.py
build/wuerfel-2-daten.tex: build/wuerfel-1-daten.tex | build
build/wuerfel-3-daten.tex: build/wuerfel-1-daten.tex | build
build/wuerfel-5-daten.tex: build/wuerfel-1-daten.tex | build
build/wuerfel-5.tex: build/wuerfel-1-daten.tex | build

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: \
	build/spektrum.pdf \
	build/spektrum.csv \
	build/wuerfel-1-daten.tex \
	build/wuerfel-2-daten.tex \
	build/wuerfel-3-daten.tex \
	build/wuerfel-5-daten.tex \
	build/wuerfel-5.tex

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
