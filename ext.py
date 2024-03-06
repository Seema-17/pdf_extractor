from paddleocr import PaddleOCR,draw_ocr
import json
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = 'img_12.jpg'
result = ocr.ocr(img_path, cls=True)

dictionary = {
    'pdf_type' : img_path
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
    dictionary[idx] = dict_data

json_object = json.dumps(dictionary, indent=4)
ind=img_path.find('.')
json_file = img_path[0:ind]
json_file = json_file + '.json'
with open(json_file, "w") as outfile:
    outfile.write(json_object)







# for idx in range(len(result)):
#     res = result[idx]
    # print(type(res))
    # for line in res:
    #     print(line)

# # draw result
# from PIL import Image
# result = result[0]
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.pdf')