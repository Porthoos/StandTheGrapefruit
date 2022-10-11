import math
import numpy as np
from pyntcloud import PyntCloud
import PCA1
import ICP
import draw_row
import move_to_origin
import PointCloud
import open3d as o3d

path1 = 'models/data7/test_tmp2.ply'
path2 = 'models/3d/test_Femto.ply'
path3 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221011200120.ply"
path_left = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221011201946.ply"
path_right = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221011202016.ply"
path_up = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221011201637.ply"
# point_cloud_pynt1 = PyntCloud.from_file(path1)
# points1 = point_cloud_pynt1.points
# w1, rows1, center1 = PCA1.PCA(points1)

target = ICP.o3d.io.read_point_cloud(path_right, format='ply')
# source_temp.paint_uniform_color([1, 0.706, 0])
# target.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([target])
# draw_row.draw_only_row(path1, path1 + "_only_row", rows1, center1)
# PointCloud.Cloud(path1)