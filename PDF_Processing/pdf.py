import PyPDF2
import sys


# Reading pdfs

with open('sample.pdf', 'rb') as file:      # rb = read binary
   reader = PyPDF2.PdfFileReader(file)
   print(reader.getDocumentInfo)


# Merging pdfs

input_pdfs = sys.argv[1:]     # extract pdf filenames

def pdf_merger(pdf_list):

   merger = PyPDF2.PdfFileMerger()

   for pdf in pdf_list:
      merger.append(pdf)

   merger.write('PDFs/ combined.pdf')

pdf_merger(input_pdfs)


# Watermarking PDFs

template_pdf = PyPDF2.PdfFileReader(open('./PDFs/ combined.pdf', 'rb'))
watermark_pdf = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
output_pdf = PyPDF2.PdfFileWriter()

for i in range(template_pdf.getNumPages()):
   page = template_pdf.getPage(i)                         # single page of template_pdf
   page.mergePage(watermark_pdf.getPage(0))
   output_pdf.addPage(page)

   with open('./PDFs/ combined_wtr.pdf', 'wb') as file:   # Writing to pdf
      output_pdf.write(file)
