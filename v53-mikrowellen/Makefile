all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex
# hier Python-Skripte:
#build/energieverlust.pdf: python-skripts/energieverlust.py data/messung_c*.csv $(pyf) | build
#	TEXINPUTS=$$(pwd): python python-skripts/energieverlust.py

build/messung1_f.pdf: data/messung-1.csv python-skripts/aufgabe1.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/aufgabe1.py
build/messung1_Uaus.pdf: build/messung1_f.pdf

build/messung2.csv: data/messung-2.csv python-skripts/aufgabe2.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/aufgabe2.py

build/messung3_daempf.pdf: data/messung-3.csv python-skripts/aufgabe3.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/aufgabe3.py

build/messung4_direkt.pdf: data/messung-4.csv data/messung-5.csv data/messung-6.csv python-skripts/aufgabe4.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python-skripts/aufgabe4.py
build/messung4_3dB.pdf: build/messung4_direkt.pdf

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/messung1_f.pdf \
	build/messung1_Uaus.pdf \
	build/messung2.csv \
	build/messung3_daempf.pdf \
	build/messung4_direkt.pdf \
	build/messung4_3dB.pdf

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
