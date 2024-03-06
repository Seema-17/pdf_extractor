from paddleocr import PaddleOCR,draw_ocr
import json

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.

def jsonExtractor(img_path, page_num):
    ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
    result = ocr.ocr('./tests/input/'+img_path, cls=True)

    pdf_type = img_path[:img_path.rfind('_')]

    dictionary1 = {
        'pdf_type' : pdf_type,
        f'page_{page_num}': {
            'page_num' : page_num
        }    
    }

    dictionary2 = {
        f'page_{page_num}': {
            'page_num' : page_num
        } 
    }
    

    for idx in range(len(result)):
        res = result[idx]
        c_1 = res[0][0]
        c_2 = res[0][1]
        c_3 = res[0][2]
        c_4 = res[0][3]
        text = res[1][0]
        dict_data = {
            'c_1' : c_1,
            'c_2' : c_2,
            'c_3' : c_3,
            'c_4' : c_4,
            'var_name' : text
        }
        if page_num == 1:
            dictionary1[f'page_{page_num}'][idx] = dict_data
        else:
            dictionary2[f'page_{page_num}'][idx] = dict_data

    if page_num == 1:
        json_object = json.dumps(dictionary1, indent=4)
        ind=img_path.find('.')
        json_file = img_path[0:ind]
        json_file = './tests/output/'+ pdf_type + '.json'
        with open(json_file, "w") as outfile:
            outfile.write(json_object)
    elif page_num > 1:
        #open the json file: pdf_type.json and append this dictionary to it
        ind=img_path.find('.')
        json_file = img_path[0:ind]
        json_file = './tests/output/'+ pdf_type + '.json'
        with open(json_file) as f:
            data = json.load(f)
            data.update(dictionary2)
            with open(json_file, 'w') as f:
                json.dump(data, f, indent=4)