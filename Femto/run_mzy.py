import os

import numpy as np
from pyntcloud import PyntCloud

import PointCloud
import draw_row
import reload_mzy as reload

temp = 'models/kinect_tmp'
path1 =   temp + '/test.ply'
path2 =   temp + '/test1.ply'
path3 =   temp + '/test2.ply'
path3_1 = temp + '/test2_1.ply'
path4 =   temp + '/test3.ply'
def shoot():
    if os.path.exists(path1):
        os.remove(path1)
    pcl = PointCloud.Cloud(file=path1, depth=True)
    pcl = PointCloud.Cloud(file=path1, color=True)
    pcl2 = PointCloud.Cloud(file=path1)
    pcl1 = PointCloud.Cloud(path1)

def reload_total():
    reload.load_ply(path1, path2)
    reload.remove_color(path2, path3)
    reload.remove_unreliable_point(path3, path3_1)
    point_cloud_pynt1 = PyntCloud.from_file(path3_1)
    points = point_cloud_pynt1.points
    data_mean = np.mean(points, axis=0)
    row = reload.findxy(path3_1, path4)
