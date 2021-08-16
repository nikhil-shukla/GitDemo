import PyPDF2

file=open("Sample.pdf","rb")
reader=PyPDF2.PdfFileReader(file)
print(reader.numPages)
page1=reader.getPage(0)
pdfdata=page1.extractText()
assert "shkla" in pdfdata,"Failed"
print("Passed")
print(pdfdata)

