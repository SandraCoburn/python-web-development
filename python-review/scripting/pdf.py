# PDF - Playground
# install PyPDF2 to be able to process pdf files

import PyPDF2
import sys

inputs = sys.argv[1:]

# Merge several pdfs by adding them on the command line and reading the files with sys.argv
# CL:  python3 pdf.py dummy.pdf twopage.pdf
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super_pdf')

pdf_combiner(inputs)


with open('dummy.pdf', 'rb') as file: # rb convert the file to binary mode so PyPDF can read it
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(reader.numPages)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)



