#pdflatex main.tex
mv *.aux aux_files
mv *.log aux_files
mv main.pdf output.pdf
git add output.pdf
git add aux_files/*.aux
git add aux_files/*.log
git add *.enl
git add *.bib
git add *.Data
