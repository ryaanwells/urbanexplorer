all: wells-2013-urbanexplorer

wells-2013-urbanexplorer: wells-2013-urbanexplorer.tex wells-2013-urbanexplorer.bib
	pdflatex wells-2013-urbanexplorer
	bibtex wells-2013-urbanexplorer
	pdflatex wells-2013-urbanexplorer
	pdflatex wells-2013-urbanexplorer

clean:
	rm -rf *.aux
	rm -rf *.log
	rm -rf *.toc
	rm -rf *~
