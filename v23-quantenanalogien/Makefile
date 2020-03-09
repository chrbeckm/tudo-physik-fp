all: build/main.pdf

pyf = matplotlibrc header-matplotlib.tex
# hier Python-Skripte:
build/theorie-schwingung.pdf: python/theorie.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/theorie.py

build/50mm-zwei-resonanzen.pdf: python/50mm-zwei-resonanzen.py auswertung/50mm-zwei-resonanzen.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python/50mm-zwei-resonanzen.py
build/50mm-zwei-resonanzen.csv: build/50mm-zwei-resonanzen.pdf | build
build/50mm-zwei-resonanzen.tex: build/50mm-zwei-resonanzen.pdf | build

build/50mm-oszi-computer-01.pdf: python/50mm-oszi-computer.py data/Messaufgabe-2/*zylinder.dat $(pyf) | build
	TEXINPUTS=$$(pwd): python python/50mm-oszi-computer.py
build/50mm-oszi-computer-04.pdf: build/50mm-oszi-computer-01.pdf | build
build/50mm-oszi-computer-12.pdf: build/50mm-oszi-computer-01.pdf | build

build/h-atom-resonanz.pdf: python/h-atom-resonanz.py data/h-atom/h-atom-resonanz.dat $(pyf) | build
	TEXINPUTS=$$(pwd): python python/h-atom-resonanz.py

build/zylinderAnzahl-01.pdf: python/resonatorkette10mm.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/resonatorkette10mm.py
build/zylinderAnzahl-04.pdf: build/zylinderAnzahl-01.pdf | build
build/zylinderAnzahl-12.pdf: build/zylinderAnzahl-01.pdf | build
build/zylinder1_4_12-10mm-Blende.pdf: build/zylinderAnzahl-01.pdf | build

build/ZylAnzahl-13mm-01.pdf: python/ZylKette-13mm.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/ZylKette-13mm.py
build/ZylAnzahl-13mm-04.pdf: build/ZylAnzahl-13mm-01.pdf | build
build/ZylAnzahl-13mm-12.pdf: build/ZylAnzahl-13mm-01.pdf | build
build/zylinder1_4_12-13mm-Blende.pdf: build/ZylAnzahl-13mm-01.pdf | build

build/zylkette-ohne-Blende-01.pdf: python/zylkette-ohne-blende.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/zylkette-ohne-blende.py
build/zylkette-ohne-Blende-04.pdf: build/zylkette-ohne-Blende-01.pdf | build
build/zylkette-ohne-Blende-12.pdf: build/zylkette-ohne-Blende-01.pdf | build
build/zylinder1_4_12-ohne-Blende.pdf: build/zylkette-ohne-Blende-01.pdf | build

build/h-381.pdf: python/h-winkel.py auswertung/h-*.csv $(pyf) | build
	TEXINPUTS=$$(pwd): python python/h-winkel.py
build/h-2130.pdf: build/h-381.pdf | build
build/h-9240.pdf: build/h-381.pdf | build

build/kette_2.pdf: python/kette_aufgabe2.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/kette_aufgabe2.py
build/peaks_kette.pdf: build/kette_2.pdf | build

build/zwischenringe.pdf: python/zwischenringe.py data/h-atom/*mm-kugel.dat $(pyf) | build
	TEXINPUTS=$$(pwd): python python/zwischenringe.py
build/zwischenringe-zoom.pdf: build/zwischenringe.pdf
build/h-9mm.pdf: build/zwischenringe.pdf | build

build/abwechselnde-Blende.pdf: python/blenden13-16-13.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/blenden13-16-13.py

build/h2blende.pdf: python/molekuel.py $(pyf) | build
	TEXINPUTS=$$(pwd): python python/molekuel.py
build/h2winkel.pdf: build/h2blende.pdf | build
build/h2winkel.csv: build/h2blende.pdf | build

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/theorie-schwingung.pdf \
	build/50mm-zwei-resonanzen.pdf \
	build/50mm-zwei-resonanzen.csv \
	build/50mm-zwei-resonanzen.tex \
	build/50mm-oszi-computer-01.pdf \
	build/50mm-oszi-computer-04.pdf \
	build/50mm-oszi-computer-12.pdf \
	build/h-atom-resonanz.pdf \
	build/zylinderAnzahl-01.pdf \
	build/zylinderAnzahl-04.pdf \
	build/zylinderAnzahl-12.pdf \
	build/ZylAnzahl-13mm-01.pdf \
	build/ZylAnzahl-13mm-04.pdf \
	build/ZylAnzahl-13mm-12.pdf \
	build/zylkette-ohne-Blende-01.pdf \
	build/zylkette-ohne-Blende-04.pdf \
	build/zylkette-ohne-Blende-12.pdf \
	build/h-381.pdf \
	build/h-2130.pdf \
	build/h-9240.pdf \
	build/zwischenringe.pdf \
	build/zwischenringe-zoom.pdf \
	build/h-9mm.pdf \
	build/kette_2.pdf \
	build/abwechselnde-Blende.pdf \
	build/h2blende.pdf \
	build/h2winkel.pdf \
	build/h2winkel.csv

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
