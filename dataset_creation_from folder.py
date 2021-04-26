import xml.etree.cElementTree as ET
import os
import os.path
import cv2
#import time
import random
import base64
import configparser
import os
from os import listdir
from tqdm import tqdm 

folder_id = "14_"
dest_basepath = "/home/ajithbalakrishnan/vijnalabs/My_Learning/my_workspace/The_iD_Project/newdata"
basepath = "/home/ajithbalakrishnan/vijnalabs/My_Learning/my_workspace/The_iD_Project/task_fridge_maaza_1-2021_03_10_20_21_41-pascal"

img_basepath=basepath + "/" + "JPEGImages" + "/"
xml_basepath =basepath + "/" +  "Annotations" + "/"

img_list = [file for file in listdir(img_basepath) if file.endswith('.PNG')]
xml_list = [file for file in listdir(xml_basepath) if file.endswith('.xml')]
print("len(img_source)",len(img_list))
print("len(xml_source)",len(xml_list))
print("folder_id",folder_id)
xml_error =  []
img_error = []
text_dest = dest_basepath + "/ImageSets/Main/"
k= open(str(text_dest + "total.txt"),"a")
for i in tqdm (range (len(img_list)),desc="Loading..."):
    img_name = img_list[i]
    img = img_name.split('.')
    xml_name = str(img[0]) + ".xml"

    img_path = img_basepath + img_name
    xml_path = xml_basepath + xml_name

    if os.path.isfile((xml_path)):
        xml_name = xml_name
    else:
        print("XML File not exist")
        xml_error.append(xml_path)
        continue

    tree = ET.parse(xml_path)
    root = tree.getroot()
    xml_dest = dest_basepath + "/" +  "Annotations" + "/" + folder_id +xml_name
    tree.write(xml_dest)
    try:

        img_read =cv2.imread(img_path)
        
        img_dest = dest_basepath + "/" + "JPEGImages" + "/" + folder_id + img_name
        cv2.imwrite(img_dest,img_read) 
    except:
        print("img read/write error")
        img_error.append(img_name)

    k.writelines(str(folder_id) +str(img[0]))
#    time.sleep(.01)
    k.write("\n")
k.close()
print("XML Error list ", xml_error)
print("img error list ", img_error)




