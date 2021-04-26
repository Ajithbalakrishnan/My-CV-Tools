import os
import random
from scipy import ndarray
import xml.etree.cElementTree as ET
import os.path
import cv2
#import time
import random
import base64
import configparser
# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io
from os import listdir
from tqdm import tqdm 
import numpy as np

def brightness(img, low, high):
    value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value 
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img
def channel_shift(img, value):
    value = int(random.uniform(-value, value))
    img = img + value
    img[:,:,:][img[:,:,:]>255]  = 255
    img[:,:,:][img[:,:,:]<0]  = 0
    img = img.astype(np.uint8)
    return img
def horizontal_flip(img, flag):
    if flag:
        return cv2.flip(img, 1)
    else:
        return img
def vertical_flip(img, flag):
    if flag:
        return cv2.flip(img, 0)
    else:
        return img
def rotation(img, angle):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    return img

def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    # add random noise to the image
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]

# dictionary of the transformations we defined earlier
available_transformations = {
  #  'rotate': random_rotation,
    'noise': random_noise,
  #  'horizontal_flip': horizontal_flip
}

img_folder_path = '/home/ajithbalakrishnan/vijnalabs/My_Learning/my_workspace/The_iD_Project/VOC_Dataset_45k/JPEGImages/'
annotation_folder_path = "/home/ajithbalakrishnan/vijnalabs/My_Learning/my_workspace/The_iD_Project/VOC_Dataset_45k/Annotations/"
dest_path =  "/media/ajithbalakrishnan/ABD/Personal/iD/Dataset/VOC_Augmented_Dataset_45k"
augmentation_type = "bright_img_"

img_list = [file for file in listdir(img_folder_path) if file.endswith('.PNG')]
xml_list = [file for file in listdir(annotation_folder_path) if file.endswith('.xml')]
print("len(img_source)",len(img_list))
print("len(xml_source)",len(xml_list))

xml_error =  []
img_error = []
text_dest = dest_path + "/ImageSets/Main/"
k= open(str(text_dest + "total.txt"),"a")
for i in tqdm (range (len(img_list)),desc="Loading..."):
    img_name = img_list[i]
    img = img_name.split('.')
    xml_name = str(img[0]) + ".xml"

    img_path = img_folder_path + img_name
    xml_path = annotation_folder_path + xml_name

    if os.path.isfile((xml_path)):
        xml_name = xml_name
    else:
        print("XML File not exist")
        xml_error.append(xml_path)
        continue

    tree = ET.parse(xml_path)
    root = tree.getroot()
    xml_dest = dest_path + "/" +  "Annotations" + "/" + augmentation_type +xml_name
    tree.write(xml_dest)
    try:

        img_read =cv2.imread(img_path)
        bright_img = brightness(img_read, 0.5, 1.2)
        #noisy_img = random_noise (img_read)
        #channel_shift_img = channel_shift(img_read, 80)
        #img = horizontal_flip(img, True)
        #img = vertical_flip(img, True)
        #img = rotation(img, 30)

        img_dest = dest_path + "/" + "JPEGImages" + "/" + augmentation_type + img_name
        cv2.imwrite(img_dest,bright_img) 
       #sk.io.imsave(img_dest, noisy_img)

    except Exception as e:
        print("img read/write error : ",e)
        img_error.append(img_name)

    k.writelines(str(augmentation_type) +str(img[0]))
#    time.sleep(.01)
    k.write("\n")
k.close()
print("XML Error list ", xml_error)
print("img error list ", img_error)
