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



####get list name folder data xml
# list_name_foder = []
# wav_fpaths = list(Path("audio_data", "dataset").glob("**/*.wav"))
# str_old_name_folder = ""
# index_list_name_folder = 0
BASE_URL_DATA_OUT = "/home/congdanh/Desktop/data_crop/"



# def read_xml_yolo(xml_file, str_dir_img , str_dir_rs):
def read_xml_yolo(xml_file):
    str_dir_img = ""
    if not os.path.isfile(xml_file):
        print('not xml file')
        return []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    str_name = ''

    for child in root:
        tag = child.tag
        if tag == 'folder':
            if len(str_dir_img) < 1:
                str_dir_img = child.text
        if tag == 'filename':
            str_name = child.text



    ### recognize all regions
    ls_name = []
    ls_box = []
    check = True
    min = -1
    max = -1
    # check =0
    top_left = [0, 0, 0, 0]
    index_bbox_in_xml = 0
    image = cv2.imread(str(xml_file)[:-4] + ".jpg")

    for child in root:
        tag = child.tag
        if tag == 'object':
            ### warning change this method in next version
            ls_grand_child = child.getchildren()
            for grand_child in ls_grand_child:
                tag = grand_child.tag
                if 'name' == tag:
                    str_name_region = grand_child.text
                    ls_name.append(str_name_region)

                    url_folder_image_after_crop= BASE_URL_DATA_OUT + str_name_region + "/"
                    try:
                        if not os.path.exists(url_folder_image_after_crop) :
                            os.makedirs(url_folder_image_after_crop)
                    except OSError:
                        print('Error: Creating directory. ' +  url_folder_image_after_crop)
                if 'bndbox' == tag:

                    x0 = (int)(grand_child.find('xmin').text)
                    y0 = (int)(grand_child.find('ymin').text)
                    x1 = (int)(grand_child.find('xmax').text)
                    y1 = (int)(grand_child.find('ymax').text)
                    bbox = [x0, y0, x1, y1]
                    ls_box.append(bbox)

                    #crop and save image bbox image[y:y + h, x:x + w]=== image[y0:y1, x0:x1]
                    crop_img = image[y0:y1, x0:x1]
                    # cv2.imshow("cropped", crop_img)
                    # cv2.waitKey(2)
                    cv2.imwrite(url_folder_image_after_crop+xml_file.name[:-4]+".jpg", crop_img)

                    check = check + 1
            index_bbox_in_xml = index_bbox_in_xml + 1
    print(ls_name)

wav_xmls = list(Path("/home/congdanh/Desktop/", "pt3").glob("**/*.xml"))
index_xml = 0
for one_wav_xml in wav_xmls:
    min = 0
    print("Xu ly file thu:" + str(index_xml))
    print(str(one_wav_xml))
    read_xml_yolo(one_wav_xml)
    index_xml = index_xml + 1
    print(one_wav_xml.parent.name)

print("hello")