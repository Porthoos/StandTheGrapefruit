import numpy as np

import PointCloud
import os
import reload
import PCA1
import draw_row
from pyntcloud import PyntCloud

temp = 'models/dataTwoKinect1'
path1 =   temp + '/test_tmp.ply'
path2 =   temp + '/test_tmp1.ply'
path3 =   temp + '/test_tmp2.ply'
path3_1 = temp + '/test_tmp2_1.ply'
path4 =   temp + '/test_tmp3.ply'


if os.path.exists(path1):
    os.remove(path1)
# file = open('models/lyy.ply', 'w').close()
pcl = PointCloud.Cloud(file=path1, depth=True)
pcl = PointCloud.Cloud(file=path1, depth=True)
pcl2 = PointCloud.Cloud(file=path1)
print(11111)
# pcl.visualize()
print(2)
