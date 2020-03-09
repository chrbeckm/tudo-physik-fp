all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex
# hier Python-Skripte:
build/energieverlust.pdf: python-skripts/energieverlust.py data/messung_c*.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/energieverlust.py

build/streuquerschnitt.pdf: python-skripts/streuquerschnitt.py data/winkel_2mikrometer.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/streuquerschnitt.py

build/mehrfach.pdf: python-skripts/mehrfach.py $(pyf)| build
	TEXINPUTS=$$(pwd): python python-skripts/mehrfach.py

build/z_abh.pdf: python-skripts/z.py $(pyf)| build
	TEXINPUTS=$$(pwd): python python-skripts/z.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/energieverlust.pdf \
	build/streuquerschnitt.pdf \
	build/mehrfach.pdf \
	build/z_abh.pdf \

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
