import PyPDF2

with open('./PDFs/Proposal.pdf', 'rb') as file:      # rb = read binary
   reader = PyPDF2.PdfFileReader(file)
   print(reader.getDocumentInfo)



