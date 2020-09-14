# Génération de fichiers aux formats `pdf`, `markdown`, `html`, `slide-html` à partir d'un seul fichier source `***-source.md` 

* Sources documentaires : 
  * Markdown et Pandoc : <https://enacit.epfl.ch/cours/markdown-pandoc/>
  * Pandoc Guide : [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)
  * Filtres Pandoc : 
    * [https://pandoc.org/filters.html](https://pandoc.org/filters.html)
    * Filtres en Python : [pandocfilters](https://github.com/jgm/pandocfilters)
* Placer le fichier `Makefile` contenu dans ce répertoire dans le même répertoire que le fichier source  `***-source.md`


~~~
FILE=$(wildcard *source.md)
TARGET=$(FILE:source.md=.pdf) $(FILE:source.md=.tex) $(FILE:source.md=git.md)  $(FILE:source.md=.html)   $(FILE:source.md=slidy.html) 

all: $(TARGET)

%.pdf: %source.md
	pandoc -s $< --listings --template="template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.tex: %source.md
	pandoc -s $< --listings --template="template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.html: %source.md
	pandoc -s   -c "style_nsi.css"  --mathjax --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%slidy.html: %source.md
	pandoc -s  -V geometry:margin=1.5cm --mathjax -t slidy  -c "style_nsi.css" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%git.md: %source.md
	pandoc -s   --filter filtre.py --webtex  -V colorlinks --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables -t gfm  $<  -o $@
~~~

* Modifier  les chemins relatifs, pour que dans chaque répertoire où s'effectue la compilation, le `Makefile` puisse retrouver les templates 
 
