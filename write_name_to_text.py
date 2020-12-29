# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:46:20 2020

@author: admin
"""
import xml.etree.ElementTree as ET
import os
import ntpath
import glob
from pathlib import Path
import xml.etree.cElementTree as ET
from PIL import Image
import cv2
import os
import cv2
from datetime import datetime

def write_date_to_txt(url_image):
    indexx=0
    for i in urls_txt_cccd_name:
        string_name_image_after_cut = ""

        if i.name.find(".pdf") == -1:
            string_name_image_after_cut = i.name[:-23]
            string_url_image = str(i)[:-23]
            print("khong co pdf ------------")
            print(i)
            print(string_url_image)
        else:
            print("Co pdf ------------")
            print(i)
            string_name_image_after_cut = i.name[:-23]
            print(string_name_image_after_cut)

urls_image_root = list(Path("/home/congdanh/Desktop/", "image_15K").glob("**/*.jpg"))
urls_txt_cccd_name = list(Path("/home/congdanh/Downloads/6K_CCCD_NAME_OK/", "CCCD").glob("**/*.txt"))

index_xml = 0
for image_root in urls_image_root:
    min = 0
    print("Xu ly file thu:" + str(index_xml))
    print(str(image_root))
    print("ten file goc")
    print(image_root.name)
    print("duong dan goc")
    print(str(image_root))


    write_date_to_txt(image_root)
    index_xml = index_xml + 1

