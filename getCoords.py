# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Load your image
# img = mpimg.imread('tests/input/AmazonWebServices_1.jpg')

# fig, ax = plt.subplots()
# ax.imshow(img)

# def onclick(event):
#     # Print the x and y coordinates of the click
#     print(event.xdata, event.ydata)

# # Connect the click event to the onclick function
# cid = fig.canvas.mpl_connect('button_press_event', onclick)

# plt.show()

import PyPDF2
import pdfplumber

def extract_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text.strip()

def extract_text_with_coordinates(pdf_path):
    text_with_coordinates = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for obj in page.extract_words():
                text_with_coordinates.append({
                    "text": obj["text"],
                    "x0": obj["x0"],
                    "top": obj["top"],
                    "x1": obj["x1"],
                    "bottom": obj["bottom"]
                })
    return text_with_coordinates

# Example usage
pdf_path = './tests/input/AmazonWebServices3.pdf'
text = extract_text(pdf_path)
text_with_coordinates = extract_text_with_coordinates(pdf_path)

print("Extracted Text:")
print(text)

print("\nText with Coordinates:")
for item in text_with_coordinates:
    print(f"Text: {item['text']}, Coordinates: ({item['x0']}, {item['top']}) to ({item['x1']}, {item['bottom']})")


# from typing import List, Tuple, Dict
# from difflib import SequenceMatcher

# def find_closest_box(
#     text_boxes: List[Tuple[str, Tuple[int, int, int, int]]], 
#     target_text: str,
#     deviation_threshold: int = 10
# ) -> Tuple[str, Tuple[int, int, int, int], float]:
#     """
#     Finds the closest text box that matches the target text type considering deviations in coordinates.
    
#     Parameters:
#         text_boxes (List[Tuple[str, Tuple[int, int, int, int]]]): 
#             A list of tuples where each tuple contains the type of text 
#             and the coordinates of the box (x1, y1, x2, y2).
#         target_text (str): The target text type to match.
#         deviation_threshold (int): Allowed deviation for coordinates matching.
        
#     Returns:
#         Tuple[str, Tuple[int, int, int, int], float]: The closest matching text box, its coordinates, and similarity score.
#     """
#     def calculate_similarity(a: str, b: str) -> float:
#         """Calculates similarity between two strings."""
#         return SequenceMatcher(None, a, b).ratio()

#     def coordinate_similarity(box_coords: Tuple[int, int, int, int]) -> float:
#         """Estimates similarity based on box coordinates deviation."""
#         dx = min(abs(target_coords[0] - box_coords[0]), abs(target_coords[2] - box_coords[2]))
#         dy = min(abs(target_coords[1] - box_coords[1]), abs(target_coords[3] - box_coords[3]))
#         return max(0, deviation_threshold - max(dx, dy)) / deviation_threshold

#     # Assume target_coords are the ideal coordinates for the target_text type.
#     # You might want to set these based on your application's needs.
#     target_coords = (0, 0, 100, 50)  # Placeholder values; adjust as necessary.

#     closest_box = None
#     highest_score = 0

#     for box_text, box_coords in text_boxes:
#         text_similarity = calculate_similarity(box_text, target_text)
#         coord_similarity = coordinate_similarity(box_coords)
#         score = text_similarity * 0.7 + coord_similarity * 0.3  # Adjust weights as needed

#         if score > highest_score:
#             closest_box = (box_text, box_coords, score)
#             highest_score = score

#     return closest_box

# # Example usage
# text_boxes = [
#     ("Invoice num.:", (10, 10, 100, 40)),
#     ("Invoice date:", (10, 200, 100, 230)),
#     ("Main", (50, 50, 150, 100))
# ]
# target_text = "Invoice Number"

# closest_box = find_closest_box(text_boxes, target_text)
# print(closest_box)


# import fitz  # PyMuPDF
# import pytesseract

# def extract_text_blocks_with_coordinates(pdf_path):
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_path)
    
#     text_blocks = []
    
#     # Iterate through each page of the PDF
#     for page_number in range(len(pdf_document)):
#         page = pdf_document.load_page(page_number)
        
#         # Extract text using PyMuPDF
#         text = page.get_text()
        
#         # Extract text blocks and their coordinates using Pytesseract
#         image = page.get_pixmap()
#         text_boxes = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        
#         # Combine extracted text and coordinates
#         for i, text_block in enumerate(text_boxes['text']):
#             x = text_boxes['left'][i]
#             y = text_boxes['top'][i]
#             width = text_boxes['width'][i]
#             height = text_boxes['height'][i]
#             text_block = text_block.strip()
            
#             # Ignore empty text blocks
#             if text_block:
#                 text_blocks.append({
#                     'text': text_block,
#                     'x': x,
#                     'y': y,
#                     'width': width,
#                     'height': height
#                 })
    
#     # Close the PDF document
#     pdf_document.close()
    
#     return text_blocks

# # Example usage
# pdf_path = './tests/input/AmazonWebServices.pdf'
# text_blocks = extract_text_blocks_with_coordinates(pdf_path)
# for block in text_blocks:
#     print(f"Text: {block['text']}, Coordinates: ({block['x']}, {block['y']}) - ({block['x'] + block['width']}, {block['y'] + block['height']})")


# import fitz
# from multi_column import column_boxes

# doc = fitz.open("./tests/input/AmazonWebServices.pdf")
# for page in doc:
#     bboxes = column_boxes(page, footer_margin=5, no_image_text=True)
#     for rect in bboxes:
#         print(page.get_text(clip=rect, sort=True))
#     print("-" * 80)
