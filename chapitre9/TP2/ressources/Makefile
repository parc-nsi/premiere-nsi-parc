FILE=$(wildcard *.md)
TARGET=$(FILE:.md=.pdf) 

all: $(TARGET)

%.pdf: %.md
	pandoc -s $<  -o $@ --pdf-engine=xelatex
	
 
