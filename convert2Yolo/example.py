#-*-coding:utf-8-*-

#python example.py --datasets KITTI --img_path /home/ajithbalakrishnan/vijnalabs/My_Learning/FL/vehicle_detection/data_object_image_2/training/training_1/ --label /home/ajithbalakrishnan/vijnalabs/My_Learning/FL/vehicle_detection/data_object_label_2/training/label_2/ --convert_output_path /home/ajithbalakrishnan/vijnalabs/My_Learning/FL/vehicle_detection/yolo_kitti_labels --img_type ".png" --manipast_path ./ --cls_list_file /home/ajithbalakrishnan/vijnalabs/My_Learning/FL/vehicle_detection/names.txt

import os
from xml.etree.ElementTree import dump
import json
import pprint

import argparse


from Format import VOC, COCO, UDACITY, KITTI, YOLO

parser = argparse.ArgumentParser(description='label Converting example.')
parser.add_argument('--datasets', type=str, help='type of datasets')
parser.add_argument('--img_path', type=str, help='directory of image folder')
parser.add_argument('--label', type=str, help='directory of label folder or label file path')
parser.add_argument('--convert_output_path', type=str, help='directory of label folder')
parser.add_argument('--img_type', type=str, help='type of image')
parser.add_argument('--manipast_path', type=str, help='directory of manipast file', default="./")
parser.add_argument('--cls_list_file', type=str, help='directory of *.names file', default="./")


args = parser.parse_args()

def main(config):

    if config["datasets"] == "VOC":
        voc = VOC()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = voc.parse(config["label"])

        if flag == True:

            flag, data = yolo.generate(data)
            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"] ,
                                       config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))


        else:
            print("VOC Parsing Result : {}, msg : {}".format(flag, data))


    elif config["datasets"] == "COCO":
        coco = COCO()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = coco.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                        config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("COCO Parsing Result : {}, msg : {}".format(flag, data))

    elif config["datasets"] == "UDACITY":
        udacity = UDACITY()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = udacity.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                       config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("UDACITY Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("COCO Parsing Result : {}, msg : {}".format(flag, data))

    elif config["datasets"] == "KITTI":
        kitti = KITTI()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = kitti.parse(config["label"], config["img_path"], img_type=config["img_type"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                       config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("KITTI Parsing Result : {}, msg : {}".format(flag, data))

    else:
        print("Unkwon Datasets")

if __name__ == '__main__':

    config ={
        "datasets": args.datasets,
        "img_path": args.img_path,
        "label": args.label,
        "img_type": args.img_type,
        "manipast_path": args.manipast_path,
        "output_path": args.convert_output_path,
        "cls_list": args.cls_list_file,
    }

    main(config)
