# PDF WATERMARK
from PyPDF2 import PdfReader, PdfWriter
from os import listdir

waterMark = PdfReader("./wtr.pdf")
waterMark_page = waterMark.pages[0]

writer = PdfWriter()

root = "./pdfFolder/"

for file in listdir(root)[::-1]:

    reader = PdfReader(root + file)

    for pag in reader.pages:
        pag.merge_page(waterMark_page)
        writer.add_page(pag)

with open(f"waterMarked.pdf", "wb") as fp:
    writer.write(fp)


# PDF MERGER
# from PyPDF2 import PdfMerger
# from os import listdir
# from os import getcwd

# merger = PdfMerger()
# current = getcwd()

# for pdf in listdir("./pdfFolder")[::-1]:
#     merger.append("./pdfFolder/" + pdf)

# merger.write("merged-pdf.pdf")
# merger.close()