#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
from shutil import copyfile

path_to_pdfs = 'ethics_essay.Data/PDF/'
dest_dir = 'tmp_pdf/'

pdf_dirs =  os.listdir(path_to_pdfs)

for i in range(len(pdf_dirs)):

    
    list_element = os.listdir(path_to_pdfs + '/' + str(pdf_dirs[i]))
    pdf_file = path_to_pdfs + str(pdf_dirs[i]) + '/' + list_element[0]
    f_name = list_element[0]
    copyfile(pdf_file, (dest_dir + f_name))
    print pdf_file


