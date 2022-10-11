import math

import numpy as np
import open3d as o3d


#平移操作
def transform(points, x, y, z):
    transformation = [
        [1., 0., 0., x ],
        [0., 1., 0., y ],
        [0., 0., 1., z ],
        [0., 0., 0., 1.]
    ]
    points.transform(transformation)

#绕X轴逆时针旋转角度θ
def transform_x(points, angle):
    x = 0
    y = 0
    z = 0
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    transformation = [
        [1.,  0.,   1., x ],
        [0., cos, -sin, y ],
        [1., sin,  cos, z ],
        [0.,  0.,   0., 1 ]
    ]
    points.transform(transformation)

#绕Y轴逆时针旋转角度θ
def transform_y(points, angle):
    # angle = 90
    x = 0
    y = 0
    z = 0
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    transformation = [
        [ cos, 0., sin, x ],
        [  0., 1.,  0., y ],
        [-sin, 0., cos, z ],
        [  0., 0.,  0., 1.]
    ]
    points.transform(transformation)

#绕Z轴逆时针旋转角度θ
def transform_z(points, angle):
    x = 0
    y = 0
    z = 0
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    transformation = [
        [cos, -sin, 0., x ],
        [sin,  cos, 0., y ],
        [0. ,   0., 1., z ],
        [0. ,   0., 0., 1.]
    ]
    points.transform(transformation)


if __name__ == '__main__':
    path2 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221009145938.ply"
    path3 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221009145938.ply"

#旋转平移前的两个点云
    source0 = o3d.io.read_point_cloud(path2, format='ply')
    points0_xyz = np.array(source0.points)
    points0_rgb = np.array(source0.colors)
    # points0_xyzrgb = np.c_[points0_xyz, points0_rgb]

    source1 = o3d.io.read_point_cloud(path3, format='ply')
    points1_xyz = np.array(source1.points)
    points1_rgb = np.array(source1.colors)

    points2_xyz = np.concatenate((points0_xyz, points1_xyz), axis=0)
    points2_rgb = np.concatenate((points0_rgb, points1_rgb), axis=0)

    ply_origin = o3d.geometry.PointCloud()
    ply_origin.points = o3d.utility.Vector3dVector(points2_xyz)
    ply_origin.colors = o3d.utility.Vector3dVector(points2_rgb)
    o3d.visualization.draw_geometries([ply_origin])

    #旋转平移之后的两个点云,固定points1！！！
    #旋转平移 调用三种transform的方法！！！
    x = 0
    y = 0
    z = 0
    anglex = 90
    angley = 90
    anglez = 90
    transform(source0,x,y,z)
    transform_x(source0, anglex)
    transform_y(source0, angley)
    transform_z(source0, anglez)

    
    points0_xyz = np.array(source0.points)
    points0_rgb = np.array(source0.colors)
    points3_xyz = np.concatenate((points0_xyz, points1_xyz), axis=0)
    points3_rgb = np.concatenate((points0_rgb, points1_rgb), axis=0)

    ply_final = o3d.geometry.PointCloud()
    ply_final.points = o3d.utility.Vector3dVector(points3_xyz)
    ply_final.colors = o3d.utility.Vector3dVector(points3_rgb)
    o3d.visualization.draw_geometries([ply_final])










































# # -*- coding: utf-8 -*-
# """
# Created on Sat Apr 16 08:51:41 2022
# @author: https://blog.csdn.net/suiyingy
# """
#
# from mayavi import mlab
# import numpy as np
# import open3d as o3d
#
#
#
# def ply_read(file_path):
#     lines = []
#     with open(file_path, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     return lines
#
#
# # 将每一行数据分割后转为数字
# def ls2n(line):
#     line = line.strip().split(' ')
#     return list(map(float, line))
#
#
# def viz_mayavi(points):
#     x = points[:, 0]  # x position of point
#     y = points[:, 1]  # y position of point
#     z = points[:, 2]  # z position of point
#     fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
#     mlab.points3d(x, y, z,
#                   y,  # Values used for Color
#                   mode="point",
#                   colormap='spectral',  # 'bone', 'copper', 'gnuplot'
#                   # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
#                   figure=fig,
#                   )
#     mlab.show()
#
#
# def transform(points):
#     # transformation = [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]
#     transformation = [[0., 0., 1., 0.], [0., 1., 0., 0.], [1., 0., 0., 0.], [0., 0., 0., 1.]]
#     points.transform(transformation)
#
#
# if __name__ == '__main__':
#     path2 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/img/test_Femto.ply"
#     path3 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/img/test_Femto1.ply"
#     source = o3d.io.read_point_cloud(path2, format='ply')
#     transform(source)
#     points0 = np.array(source.points)
#     points = ply_read(path2)
#     points = points[8:]
#     points1 = np.array(list(map(lambda x: ls2n(x), points)))
#
#
#     points = ply_read(path3)
#     points = points[8:]
#     points2 = np.array(list(map(lambda x: ls2n(x), points)))
#
#     # source_temp.transform(transformation)
#     # transform(points2)
#
#     print(points1.shape)
#     points3 = np.concatenate((points1, points2), axis=0)
#     print(points3.shape)
#     viz_mayavi(points3)


# # -*- coding: utf-8 -*-
# """
# Created on Sat Apr 16 08:51:41 2022
# @author: https://blog.csdn.net/suiyingy
# """
#
# from mayavi import mlab
# import numpy as np
# import open3d as o3d
#
#
#
# def ply_read(file_path):
#     lines = []
#     with open(file_path, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     return lines
#
#
# # 将每一行数据分割后转为数字
# def ls2n(line):
#     line = line.strip().split(' ')
#     return list(map(float, line))
#
#
# def viz_mayavi(points):
#     x = points[:, 0]  # x position of point
#     y = points[:, 1]  # y position of point
#     z = points[:, 2]  # z position of point
#     fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
#     mlab.points3d(x, y, z,
#                   y,  # Values used for Color
#                   mode="point",
#                   colormap='spectral',  # 'bone', 'copper', 'gnuplot'
#                   # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
#                   figure=fig,
#                   )
#     mlab.show()
#
#
# def transform(points):
#     # transformation = [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]
#     transformation = [[0., 0., 1., 0.], [0., 1., 0., 0.], [1., 0., 0., 0.], [0., 0., 0., 1.]]
#     points.transform(transformation)
#
#
# if __name__ == '__main__':
#     path2 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221009145938.ply"
#     path3 = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb/RGBDPoints_20221009145938.ply"
#     source0 = o3d.io.read_point_cloud(path2, format='ply')
#
#
#     # transform(source0)
#     points0 = np.array(source0.points)
#     # viz_mayavi(points0)
#     # o3d.visualization.draw_geometries([source0])
#     transform(source0)
#     # o3d.visualization.draw_geometries([source0])
#     points0_xyz = np.array(source0.points)
#     points0_rgb = np.array(source0.colors)
#     points0_xyzrgb = np.c_[points0_xyz, points0_rgb]
#     # viz_mayavi(points0_xyzrgb)
#     # ply = o3d.geometry.PointCloud()
#     # ply.points = o3d.utility.Vector3dVector(points0_xyz)
#     # ply.colors = o3d.utility.Vector3dVector(points0_rgb)
#     # o3d.visualization.draw_geometries([ply])
#     # points = ply_read(path2)
#     # points = points[8:]
#     # points1 = np.array(list(map(lambda x: ls2n(x), points)))
#
#
#     # points = ply_read(path3)
#     # points = points[8:]
#     # points2 = np.array(list(map(lambda x: ls2n(x), points)))
#
#     # source_temp.transform(transformation)
#     # transform(points2)
#     source1 = o3d.io.read_point_cloud(path3, format='ply')
#     points1_xyz = np.array(source1.points)
#     points1_rgb = np.array(source1.colors)
#     # print(points1.shape)
#     points3_xyz = np.concatenate((points0_xyz, points1_xyz), axis=0)
#     points3_rgb = np.concatenate((points0_rgb, points1_rgb), axis=0)
#     # print(points3.shape)
#     # viz_mayavi(points3)
#
#     ply = o3d.geometry.PointCloud()
#     ply.points = o3d.utility.Vector3dVector(points3_xyz)
#     ply.colors = o3d.utility.Vector3dVector(points3_rgb)
#     o3d.visualization.draw_geometries([ply])
#
#     # ply = o3d.geometry.PointCloud()
#     # ply.points = o3d.utility.Vector3dVector(points3)
#     # o3d.visualization.draw_geometries([ply])