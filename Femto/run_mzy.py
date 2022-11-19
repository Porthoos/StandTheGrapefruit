import os

import numpy as np
from pyntcloud import PyntCloud

import PointCloud
import draw_row
import reload_mzy as reload

temp = 'models/kinect7'
path1 =   temp + '/test.ply'
path2 =   temp + '/test1.ply'
path3 =   temp + '/test2.ply'
path3_1 = temp + '/test2_1.ply'
path4 =   temp + '/test3.ply'

# print(111)
# if os.path.exists(path1):
#     os.remove(path1)
# # file = open('models/lyy.ply', 'w').close()
# print(11)
# pcl = PointCloud.Cloud(file=path1, depth=True)
# pcl = PointCloud.Cloud(file=path1, color=True)
# print(1)
# pcl2 = PointCloud.Cloud(file=path1)
#
# print(1111)
# pcl1 = PointCloud.Cloud(path1)
reload.load_ply(path1, path2)
reload.remove_color(path2, path3)

# PointCloud.Cloud(file=path3)

# point_cloud_pynt = PyntCloud.from_file(path3)
# points = point_cloud_pynt.points
# w, rows, center = PCA1.PCA(points)
#
# print(rows)
# print(center)
#
# c = []
# c.append(center[0])
# c.append(center[1])
# c.append(center[2])
# print(c)
#
# print(np.degrees(np.arccos(np.dot(rows[0], [0,1,0]))))
#
# draw_row.change_dly(path3, path4, rows, c)

reload.remove_unreliable_point(path3, path3_1)
# pcl2 = PointCloud.Cloud(path3_1)

point_cloud_pynt1 = PyntCloud.from_file(path3_1)
points = point_cloud_pynt1.points
data_mean = np.mean(points, axis=0)


row = reload.findxy(path3_1, path4)
# draw_row.change_dly(path1, path1+"_with_row", rows1, center1)
# print("##################")


# pcl2 = PointCloud.Cloud('models/data7/test_tmp_model.ply')
