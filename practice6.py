# Write a python program that calls ifconfig and splits its output to files according to
# the network interfaces it finds.
# in this program ifconfig is not called

import sys
import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"


def read_file(file_path):
    file_to_read= open(file_path, "r")  # 读成char的list
    txt=file_to_read.read()
    file_to_read.close()
    return txt


if __name__ == '__main__':
    print("start\n")
    file_path=sys.argv[1]
    txt=read_file(sys.argv[1]).split('\n\n')
    mkdir('.\\practice6')
    for i in txt:
        lines=i.split('\n')
        file_name=(lines[0].split(':'))[0]
        with open('.\\practice6\\'+file_name+'.txt','a+') as f:
            f.write('\n')
            f.writelines(i)
