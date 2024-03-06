import fitz
import os
directory = os.fsencode('./')

def convertPdfToJpg(pdffile):
    doc = fitz.open(pdffile)
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    count = 0
    # Count variable is to get the number of pages in the pdf
    for p in doc:
        count += 1
    for i in range(count):
        val = f"{pdffile[:-4]}_{i+1}.jpg"
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat)
        pix.save(val)
    doc.close()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename.endswith('.pdf'):
        convertPdfToJpg(filename)


