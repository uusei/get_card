# code:utf-8
import os
import numpy as np
import random as ra
import sys

def read_num():
    picpath, save_video = init_file()
    if os.path.isfile('picnum1.npy'):
        print('YES,get num')
        pic = np.load('picnum1.npy')
        print(pic)
        count_pic = len(pic)
        if count_pic > 0:
            # 应该返回的重要数值有 图片数组 抽到的路径 图片的数组位置 当前图片数量
            return pic, count_pic
        else:
            print('remove old now')
            os.remove('picnum1.npy')
            print('create num now')
            count_pic, pic_files = list_pic(picpath)
            pic = np.array(pic_files)
            # 应该返回的重要数值有 图片数组 抽到的路径 当前图片数量
            return pic, count_pic

    elif not os.path.isfile('picnum1.npy'):
        print('create num now')
        count_pic, pic_files = list_pic(picpath)
        pic = np.array(pic_files)
            # 应该返回的重要数值有 图片数组 抽到的路径 当前图片数量
        return pic, count_pic


def gachi_card_out(pic, count_pic):
    picpath, save_video = init_file()
    try:
        initpic = int(ra.randint(0, count_pic - 1))
    except:
        initpic = 0
    picname = pic[initpic]
    print(picname)
    picdir = picpath + '\\' + picname
    print(picdir)
    return picdir, initpic


def gachi_v_out(pic, count_pic, picpath):
    try:
        initpic = int(ra.randint(0, count_pic - 1))
    except:
        initpic = 0
    picname = pic[initpic]
    print(picname)
    picdir = picpath + '\\' + picname
    print(picdir)
    return picdir

def init_file():
    picpath = os.getcwd() + '\\' + 'pic'
    if not os.path.isdir(picpath):
        os.mkdir("pic")
    save_video = os.getcwd() + '\\' + 'video'
    if not os.path.isdir(save_video):
        os.mkdir("video")
    return picpath, save_video


def list_pic(picpath):
    print("Get image files ... ", end='\n')

    files = os.listdir(picpath)
    print(files, end='\n')
    pic_files = []

    for f in files:
        if os.path.isdir(f):
            continue

        if get_file_ext(f).lower() == '.jpg':
            pic_files.append(f)

        if get_file_ext(f).lower() == '.jpeg':
            pic_files.append(f)

        if get_file_ext(f).lower() == '.png':
            pic_files.append(f)

    count_pic = len(pic_files)
    print("%s found" % count_pic)
    print(picpath, end='\n')
    return count_pic, pic_files


def get_file_ext(file_name):
    dot_pos = file_name.rfind('.')
    if dot_pos == -1:
        ext = ''
    else:
        ext = file_name[dot_pos:]

    return ext


def list_video(picpath):
    files = os.listdir(picpath)
    print(files, end='\n')
    pic_files = []

    for f in files:
        if os.path.isdir(f):
            continue

        if get_file_ext(f).lower() == '.mp4':
            pic_files.append(f)

    count_pic = len(pic_files)
    print("%s found" % count_pic)
    print(picpath, end='\n')
    return count_pic, pic_files

