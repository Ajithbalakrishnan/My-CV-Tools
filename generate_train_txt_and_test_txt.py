import os, csv, time
import glob


def write_list_file(listfile, jpg_file):
    f = open(listfile, 'w')

    wd = os.getcwd()
    for filename in glob.glob("{}/JPEGImages/{}".format(wd, jpg_file)):
        print(filename)
        f.write(filename+"\n")

    f.close()

write_list_file('traindwdw.txt', '[1-13]*.jpg')
write_list_file('test.txt', '14*.jpg')
