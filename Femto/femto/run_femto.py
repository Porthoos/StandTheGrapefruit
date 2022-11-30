import os
# import PointCloud
import time

import reload_femto as reload

temp = 'temp/femto_tmp/'
path1 =   temp + 'test.ply'
path2 =   temp + 'test1.ply'
path3 =   temp + 'test2.ply'
path3_1 = temp + 'test2_1.ply'
path4 =   temp + 'test3.ply'

# srcfile 需要复制、移动的文件
# dstpath 目的地址

import os
import shutil
from glob import glob


def movefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        fname = "test.ply"
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))


# src_dir = './'
# dst_dir = './move/'  # 目的路径记得加斜杠
# src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改
# for srcfile in src_file_list:
#     movefile(srcfile, dst_dir)  # 移动文件


def shoot():
    while True:
        time.sleep(5)
        if os.path.exists(path1):
            os.remove(path1)
        path = "C:/Users/jdy/Desktop/OrbbecViewer/output/PointCloud/"
        filelist = glob(path + '*')
        if len(filelist) == 0:
            print("there is no file.")
        elif len(filelist) == 1:
            print("there is only one file.")
            time.sleep(20)
            print('test if sleep')
            for f in filelist:
                movefile(f, temp)
            break
        else:
            print("there are more than one file")
            for f in filelist:
                os.remove(f)

        # os.exit()

    # 直接读取ply文件
    # pcl = PointCloud.Cloud(file=path1, depth=True)
    # pcl = PointCloud.Cloud(file=path1, color=True)

def reload_total():
    # xyz问题
    reload.load_ply(path1, path2)
    reload.remove_color(path2, path3)
    reload.remove_unreliable_point(path3, path3_1)
