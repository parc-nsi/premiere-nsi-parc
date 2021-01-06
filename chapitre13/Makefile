FILE=$(wildcard *source.md)
TARGET=$(FILE:source.md=.pdf) $(FILE:source.md=.tex) $(FILE:source.md=git.md)  $(FILE:source.md=.html)   $(FILE:source.md=slidy.html) 

all: $(TARGET)

%.pdf: %source.md
	pandoc -s $< --listings --template="../Pandoc/template-pandocV1.tex" --filter ../Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.tex: %source.md
	pandoc -s $< --listings --template="../Pandoc/template-pandocV1.tex" --filter ../Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.html: %source.md
	pandoc -s   -c "../Pandoc/style_nsi.css"  --mathjax --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%slidy.html: %source.md
	pandoc -s  -V geometry:margin=1.5cm --mathjax -t slidy  -c "../Pandoc/style_nsi.css" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%git.md: %source.md
	pandoc -s   --filter ../Pandoc/filtre.py --webtex  -V colorlinks --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables -t gfm  $<  -o $@

