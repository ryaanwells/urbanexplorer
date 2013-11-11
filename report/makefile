all: report

report: report.tex report.bib
	pdflatex report
	bibtex report
	pdflatex report
	pdflatex report

clean:
	rm -rf *.aux
	rm -rf *.log
	rm -rf *.toc
	rm -rf *~
