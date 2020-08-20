import os
from PyPDF2 import PdfFileReader, PdfFileWriter

fn = "reportlab-userguide.pdf"
with open (fn, 'rb') as f:
    pdf = PdfFileReader (f)
    info = pdf.getDocumentInfo ()
    number_of_pages = pdf.getNumPages ()

    print(info)
    print(info.title)
    print(info.author)
    print(info.producer)
    print(info.creator)
    print(number_of_pages)

    page = pdf.getPage (7)
    text = page.extractText ()
    print (text)




