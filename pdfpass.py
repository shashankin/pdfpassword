from PyPDF2 import PdfFileWriter , PdfFileReader

pdfwriter = PdfFileWriter()

pdf = PdfFileReader("application.pdf")

for page_num in range(pdf.numPages):
      pdfwriter.addPage(pdf.getPage(page_num))

passw = "shasha12"
pdfwriter.encrypt(passw)

with open("unlock.pdf" , 'wb') as f:
    pdfwriter.write(f)
    f.close()
