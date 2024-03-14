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


def get_address(path):
# Example usage
    pdf_path = path
    text = extract_text(pdf_path)
    text_with_coordinates = extract_text_with_coordinates(pdf_path)

    # print("Extracted Text:")
    # print(text)

    # print("\nText with Coordinates:")
    # for item in text_with_coordinates:
    #     print(f"Text: {item['text']}, Coordinates: ({item['x0']}, {item['top']}) to ({item['x1']}, {item['bottom']})")

    x_coord = -1.00000
    max_y_coord = -1.00000

    for item in text_with_coordinates:
        if item['text'] == 'Bill':
            x_coord = item['x0']
            y_coord = item['top']
            max_y_coord = max(max_y_coord, item['top'])

    item_x_coord = []
    for item in text_with_coordinates:
        if item['x0'] == x_coord and item['top'] > y_coord:
            item_x_coord.append(item)

    line_gap = item_x_coord[1]['top'] - item_x_coord[0]['top']
    # print(line_gap)
    numLines = 0

    for i in range(0, len(item_x_coord)-1):
        gap = item_x_coord[i+1]['top'] - item_x_coord[i]['top']
        if gap == line_gap:
            continue
        else:
            numLines = i+1
            break

    item_x_coord = item_x_coord[:numLines]

    # for item in item_x_coord:
    #     print(item)

    all_items = []
    
    print("Address")

    for item in item_x_coord:
        s = ""
        y_cord = item['top']
        for it in text_with_coordinates:
            if it['top'] == y_cord:
                s = s + it['text'] + " "
        print(s)




