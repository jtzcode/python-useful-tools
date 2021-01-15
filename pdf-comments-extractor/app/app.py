import sys, os, fitz
from PyPDF2 import PdfFileWriter, PdfFileReader
from pprint import pprint
from exporter import FileExporter

def _parse_highlight(annot: fitz.Annot, wordlist: list):
    points = annot.vertices
    quad_count = int(len(points) / 4)
    sentences = ['' for i in range(quad_count)]
    for i in range(quad_count):
        r = fitz.Quad(points[i * 4: i * 4 + 4]).rect
        words = [w for w in wordlist if fitz.Rect(w[:4]).intersects(r)]
        sentences[i] = ' '.join(w[4] for w in words)
    sentence = ' '.join(sentences)
    return sentence

def run():
    try :
        file_name = sys.argv[1]
        ouput_file = sys.argv[2]
    except :
        print('Please specify the absolute path of target PDF file.')

    # put the role into the rst file
    # src = os.path.abspath(file_name)
    pypdf_doc = PdfFileReader(open(file_name, "rb"))
    mupdf_doc = fitz.open(file_name)
    n_pages = pypdf_doc.getNumPages()
    print("This document has %d pages." % n_pages)

    result_notes = {}

    for i in range(n_pages) :
    # get the data from this PDF page (first line of text, plus annotations)
        pypdf_page = pypdf_doc.getPage(i)
        mupdf_page = mupdf_doc.loadPage(i)
        result_notes.setdefault(i, {})
        # Load highlighted text of current page
        try:
            wordlist = mupdf_page.getText("words")  # list of words on page
            wordlist.sort(key=lambda w: (w[3], w[0]))  # ascending y, then x
            result_notes[i]["highlights"] = []

            for annot in mupdf_page.annots():
                # underline / highlight / strikeout / squiggly : 8 / 9 / 10 / 11
                if annot.type[0] == 8:
                    result_notes[i]["highlights"].append(_parse_highlight(annot, wordlist))
                    # print('> ' + highlights[index] + '\n')
        except:
            raise Exception("Error when reading highlights on page %d" % i)
        # Load popup comments of current page
        try :
            result_notes[i]["comments"] = []
            if '/Annots' in pypdf_page:
                print("Page comments num: %d" % len(pypdf_page["/Annots"]))
                for annot in pypdf_page['/Annots'] :
                    subtype = annot.getObject()['/Subtype']
                    if subtype == "/Highlight":
                        # print(annot.getObject()['/Contents'])
                        result_notes[i]["comments"].append(annot.getObject()['/Contents'])
        except:
            raise Exception("Error when reading comments on page %d" % i)
    
    file_exporter = FileExporter(ouput_file, 'text')
    file_exporter.run()

    pprint(result_notes)

if __name__ == "__main__":
    run()