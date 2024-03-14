from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import json

# Create an OCR object
ocr = PaddleOCR(use_angle_cls=True, lang="en")

# Load the image
image_path = './tests/input/PO_81_2075111_0_US_1.jpg'

# Run OCR on the image
result = ocr.ocr(image_path, cls=True)

# print(result[0])

# Function to process OCR results and extract specific fields
def extract_fields(ocr_result):
    # print(ocr_result)
    text_blocks = [line[1][0] for line in ocr_result if line[1][0].strip() != '']
    ship_to, invoice_to, supplier = [], [], []
    current_section = None
    
    for block in text_blocks:
        if 'Ship-to Location:' in block:
            current_section = 'ship_to'
        elif 'Invoice-to Location:' in block:
            current_section = 'invoice_to'
        elif 'Supplier:' in block:
            current_section = 'supplier'
        else:
            if current_section == 'ship_to':
                ship_to.append(block)
            elif current_section == 'invoice_to':
                invoice_to.append(block)
            elif current_section == 'supplier':
                supplier.append(block)

    return {
        'Ship to Location': " ".join(ship_to),
        'Invoice to Location': " ".join(invoice_to),
        'Supplier': " ".join(supplier)
    }

# Process the OCR result to extract the required fields
extracted_data = extract_fields(result)

# Convert to JSON format
json_data = json.dumps(extracted_data, indent=4)
print(json_data)

json_file = './tests/output/PO_81.json'


with open(json_file, "w") as outfile:
    outfile.write(json_data)

# with open(json_file) as f:
#     data = json.load(f)
#     data.update(extracted_data)
#     with open(json_file, 'w') as f:
#         json.dump(data, f, indent=4)
#     # with open(json_file, 'w') as f:
#     #     json.dump(data, f, indent=4)