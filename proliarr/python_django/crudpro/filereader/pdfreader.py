import PyPDF2

file = open('/home/madhu/Documents/crudpro/sample.pdf', 'rb')
Reader = PyPDF2.PdfFileReader(file)
print(Reader.numPages)
page = Reader.getPage(1)
print(page.extractText())
file.close()
