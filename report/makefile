all: wells-2013-urbanexplorer

wells-2013-urbanexplorer: wells-2013-urbanexplorer.tex report.bib
	pdflatex wells-2013-urbanexplorer
	bibtex report
	pdflatex wells-2013-urbanexplorer
	pdflatex wells-2013-urbanexplorer

clean:
	rm -rf *.aux
	rm -rf *.log
	rm -rf *.toc
	rm -rf *~
