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

def write_date_to_txt(url_image):
    indexx=0
    for i in urls_txt_cccd:
        string_name_image_after_cut = ""

        if i.name.find(".pdf") == -1:
            string_name_image_after_cut = i.name[:-34]
            string_url_image = str(i)[:-34]
            # print(string_url_image)
        else:

            string_name_image_after_cut = i.name[:-38]

        # print("#########")
        # print(string_name_image_after_cut)

        s_image_png = Path(str(i)[:-7] + ".png")
        s_image_jpg = Path(str(i)[:-7] + ".jpg")
        if s_image_png.exists() :
            # print("ton tai")


            if url_image.name[:-4] == string_name_image_after_cut:
                indexx = indexx + 1
                print("#########")
                print(url_image.name[:-4])
                print(string_name_image_after_cut)
                print(str(indexx))
                #tao file de ghi
                # f = open("demofile4.txt", "a")
                # f.close()
                if Path("/home/congdanh/Desktop/ex/kq/" +string_name_image_after_cut + ".txt").exists():
                    print()
                    f = open(i, "r")
                    f_r = open("/home/congdanh/Desktop/ex/kq/" + string_name_image_after_cut + ".txt", "r")
                    old_date = f_r.readline()
                    date_i = f.readline()
                    if datetime.strptime(old_date,'%d/%m/%Y') > datetime.strptime(date_i,'%d/%m/%Y'):
                        f_w = open("/home/congdanh/Desktop/ex/kq/" + string_name_image_after_cut + ".txt", "a")
                        # f_w.write("ngay het han")
                        f_w.write(date_i)

                else:
                    f = open(i, "r")
                    # f.readline()
                    f1 = open("/home/congdanh/Desktop/ex/kq/" + string_name_image_after_cut + ".txt", "a")
                    # print(f.readline())
                    f1.write(f.readline())

                # print("ton tai")

                # f.write("Now the file has more content!\n")
                # f.close()
        # else:
        #      print("khong ton tai anh phu hop voi file txt")


    # print("start")



urls_image_root = list(Path("/home/congdanh/Desktop/", "image_15K").glob("**/*.png"))
urls_txt_cccd = list(Path("/home/congdanh/Desktop/", "CCCD").glob("**/*.txt"))
index_xml = 0
for image_root in urls_image_root:
    min = 0
    print("Xu ly file thu:" + str(index_xml))
    print(str(image_root))

    write_date_to_txt(image_root)

    # read_xml_yolo(one_wav_xml)
    index_xml = index_xml + 1
    print(image_root.parent.name)

print("hello")