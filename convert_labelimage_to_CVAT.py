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




### read xml file


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
                if 'bndbox' == tag:

                    x0 = (int)(grand_child.find('xmin').text)
                    y0 = (int)(grand_child.find('ymin').text)
                    x1 = (int)(grand_child.find('xmax').text)
                    y1 = (int)(grand_child.find('ymax').text)
                    bbox = [x0, y0, x1, y1]
                    ls_box.append(bbox)
                    min = x0 + y0
                    check = check + 1

    y_min_row = 999999
    x_max_row = -999999

    list_bb_1_row = []
    print("list box la:")
    print(ls_box)
    print("list box la:")

    root = ET.Element("annotation")
    ET.SubElement(root, "folder")
    ET.SubElement(root, "filename").text = xml_file.name[:-4] + ".jpg"

    child_F1 = ET.SubElement(root, "source")

    ET.SubElement(child_F1, "database").text = "Unknown"
    ET.SubElement(child_F1, "annotation").text = "Unknown"
    ET.SubElement(child_F1, "image").text = "Unknown"

    #get width height image
    im = Image.open(str(xml_file)[:-4] + ".jpg")
    width, height = im.size

    chil_F1_1 = ET.SubElement(root, "size")

    ET.SubElement(chil_F1_1, "width").text = str(width)
    ET.SubElement(chil_F1_1, "height").text = str(height)
    ET.SubElement(chil_F1_1, "depth").text = ""

    ET.SubElement(root, "segmented").text = "0"

    index1 = 0
    print("ls name")
    print(ls_name)
    for box in ls_box:

        print("bb in row:" +  str(index1))
        chil_F1_2 = ET.SubElement(root, "object")
        ET.SubElement(chil_F1_2, "name").text= ls_name[index1]
        ET.SubElement(chil_F1_2, "occluded").text= "0"

        chil_F2_0 = ET.SubElement(chil_F1_2, "bndbox")
        ET.SubElement(chil_F2_0, "xmin").text = str(box[0])
        ET.SubElement(chil_F2_0, "ymin").text = str(box[1])
        ET.SubElement(chil_F2_0, "xmax").text = str(box[2])
        ET.SubElement(chil_F2_0, "ymax").text = str(box[3])

        chil_F2_1 = ET.SubElement(chil_F1_2, "attributes")
        chil_F3_0 = ET.SubElement(chil_F2_1, "attribute")
        ET.SubElement(chil_F3_0, "name").text = "atr" + " " + ls_name[index1]
        ET.SubElement(chil_F3_0, "value").text = "none"

        index1 = index1 + 1

    tree = ET.ElementTree(root)
    tree.write(xml_file)


### Main
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'




#load folder pt3
wav_xmls = list(Path("/home/congdanh/Desktop/", "pt4").glob("**/*.xml"))
index_xml = 0


for one_wav_xml in wav_xmls:
    min = 0
    print("Xu ly file thu:" + str(index_xml))
    read_xml_yolo(one_wav_xml)
    index_xml = index_xml + 1
    # print(one_wav_xml.parent.name)

    with open(one_wav_xml, 'rb') as open_file:
        content = open_file.read()

    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    with open(one_wav_xml, 'wb') as open_file:
        open_file.write(content)

print("hello")