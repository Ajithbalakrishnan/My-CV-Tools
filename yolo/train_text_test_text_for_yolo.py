# This code is to create train.text,test.text files for yolo
#python word_edit_2.py -i /home/ajith/Downloads/car-tank/2-2 -o /home/ajith/Desktop/sample  

import string  
import os
import os.path
import re
import shutil
from PIL import Image
from shutil import copyfile
import argparse
import glob
import math
import random
import time 
def iterate_dir(source, dest,file_name_):
    source = source.replace('\\', '/')
    dest = dest.replace('\\', '/')
    
    images = [f for f in os.listdir(source)
              if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', f)]

    text_files = [f for f in os.listdir(source)
              if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.txt)$', f)]

    num_img = len(images)
    print("Number of image files",num_img)
    
    num_text = len(text_files)
    print("number of text files:", num_text)
    
    p = 0
    k= open((os.path.join(dest, str(file_name_))),"w+")
   

    for z in range(num_img):
        idx = random.randint(0, len(images)-1)
        filename = images[idx]

        text_filename = os.path.splitext(filename)[0]+'.txt'
        
        k.writelines("data/obj/"+str(filename))
        

        time.sleep(.01)
        k.write("\n")
        time.sleep(.01)
        print("compleated:",str(p))
        p = p+1
    k.close()


def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(description="Partition dataset of images into training and testing sets",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-i', '--imageDir',
        help='Path to the folder where the image dataset is stored. If not specified, the CWD will be used.',
        type=str,
        default=os.getcwd()
    )
    parser.add_argument(
        '-o', '--outputDir',
        help='Path to the output folder where the train and test dirs should be created. '
             'Defaults to the same directory as IMAGEDIR.',
        type=str,
        default=None
    )
    parser.add_argument(
        '-r', '--ratio',
        help='The ratio of the number of test images over the total number of images. The default is 0.1.',
        default=0.1,
        type=float
    )
    parser.add_argument(
        '-f', '--file_name',
        help='output file name '
             'Defaults to the same directory as IMAGEDIR.',
        type=str,
        default=None
    )

    

    args = parser.parse_args()

    if args.outputDir is None:
        args.outputDir = args.imageDir

    # Now we are ready to start the iteration
    iterate_dir(args.imageDir, args.outputDir, args.file_name)  

if __name__ == '__main__':
    main()