all: build/main.pdf

# hier Python-Skripte:
build/double.pdf: plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:

build/single.pdf: plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2.py

build/main.pdf: build/double.pdf build/single.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
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
