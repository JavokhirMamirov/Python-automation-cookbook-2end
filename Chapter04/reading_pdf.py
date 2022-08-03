from PyPDF2 import PdfFileReader

file = open('documents/document-2.pdf', 'rb')

document = PdfFileReader(file)

print(document.pages[1].extractText())