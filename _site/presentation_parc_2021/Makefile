FILE=$(wildcard *.md)
TARGET=$(FILE:.md=.pdf) $(FILE:.md=.html)  $(FILE:.md=.pptx) 

all: $(TARGET)

%.pdf: %.md
	pandoc  $< -o $@

%.html: %.md
	pandoc  --standalone -t revealjs $< -o $@

%.pptx: %.md
	pandoc  $< -o $@
