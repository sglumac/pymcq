.PHONY: clean test clean-all

%.pdf: %.tex
	latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make $<

test:
	python test.py
	make test.pdf
	make matrix.pdf
	make answers.pdf

clean:
	latexmk -c

clean-all:
	latexmk -C
