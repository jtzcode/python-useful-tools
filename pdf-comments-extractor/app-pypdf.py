import sys, os
from PyPDF2 import PdfFileWriter, PdfFileReader

try :
    file_name = sys.argv[1]
except :
    print('Please specify the absolute path of target PDF file.')

# put the role into the rst file
# src = os.path.abspath(file_name)
pdf_input = PdfFileReader(open(file_name, "rb"))
n_pages = 30 #pdf_input.getNumPages()
print("This document has %d pages." % n_pages)

for i in range(n_pages) :
# get the data from this PDF page (first line of text, plus annotations)
    page = pdf_input.getPage(i)
    text = page.extractText()

    try :
        if '/Annots' in page:
            print("Page comments num: %d" % len(page["/Annots"]))
            for annot in page['/Annots'] :
                # Other subtypes, such as /Link, cause errors
                #for key in annot.getObject().keys():
                        #print(annot.getObject()[key])
                subtype = annot.getObject()['/Subtype']
                #if subtype == "/Popup":
                #    print(annot.getObject()['/Parent']['/Popup'])
                if subtype == "/Highlight":
                    print(annot.getObject()['/Contents'])
    except :
        # there are no annotations on this page
        raise Exception("Error when reading annotations on page %d" % i)