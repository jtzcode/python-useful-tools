import fitz, sys  # to import the PyMuPDF library

print(fitz.__doc__)
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
    except :
        print('Please specify the absolute path of target PDF file.')
    doc = fitz.open(file_name)
    highlights = {}

    for page in doc:
        # annot = page.firstAnnot
        wordlist = page.getText("words")  # list of words on page
        wordlist.sort(key=lambda w: (w[3], w[0]))  # ascending y, then x
        for annot in page.annots():
            i = 0
            #while annot:
            # underline / highlight / strikeout / squiggly : 8 / 9 / 10 / 11
            if annot.type[0] == 8:
                highlights[i] = _parse_highlight(annot, wordlist)
                print('> ' + highlights[i] + '\n')
                i += 1
                #annot = annot.next
    # Export highlights to files.


if __name__ == "__main__":
    run()