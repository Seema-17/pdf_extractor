# For loop to get all the json files for the inputs in tests/input
# the output can be found in tests/output

import os
import ext

directory = os.fsencode('./tests/input/')

map_pdf_pagenum = {}

filenames = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filenames.append(filename)

filenames.sort()

for file in filenames:
    filename = file
    pdf_type = filename[:filename.rfind('_')]
    page_num = -1
    if pdf_type in map_pdf_pagenum.keys():
        page_num = map_pdf_pagenum[pdf_type]+1
        map_pdf_pagenum[pdf_type] = map_pdf_pagenum[pdf_type]+1
    else:
        page_num = 1
        map_pdf_pagenum[pdf_type] = 1
    
    if filename.endswith(".jpg"):
        ext.jsonExtractor(filename, page_num)
        