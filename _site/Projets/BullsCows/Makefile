#Makefile modèle pour création de fichiers pdf

FILE=$(wildcard *.tex)
TARGET=$(FILE:.tex=.pdf)

all: $(TARGET)

%.pdf: %.tex
	latexmk -pdf -quiet $< || rubber-info $<
	latexmk -c $<

clean:
	latexmk -c $(FILE)

mrproper:
	rm -f $(TARGET)

