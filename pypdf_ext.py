from pypdf import PdfReader
reader = PdfReader("./tests/input/AmazonWebServices.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
# text = page.extract_text()
# print(text)

# text = page.extract_text(extraction_mode="layout")
# print(text)

# text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
# print(text)

# text = page.extract_text(extraction_mode="layout", layout_mode_scale_weight=3.0)
# print(text)



# svg files

# from pypdf import PdfReader
# import svgwrite

# reader = PdfReader("./tests/input/PO5.pdf")
# page = reader.pages[0] # first page

# dwg = svgwrite.Drawing("PO5.svg", profile="tiny")


# def visitor_svg_rect(op, args, cm, tm):
#     if op == b"re":
#         (x, y, w, h) = (args[i].as_numeric() for i in range(4))
#         dwg.add(dwg.rect((x, y), (w, h), stroke="red", fill_opacity=0.05))


# def visitor_svg_text(text, cm, tm, fontDict, fontSize):
#     (x, y) = (cm[4], cm[5])
#     dwg.add(dwg.text(text, insert=(x, y), fill="blue"))


# page.extract_text(
#     visitor_operand_before=visitor_svg_rect, visitor_text=visitor_svg_text
# )
# dwg.save()