import open3d as o3d
import numpy as np

path_up = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb_temp/test_tmp1u.ply"
path_left = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb_temp/test_tmp1w.ply"

FOR1 = o3d.geometry.TriangleMesh.create_coordinate_frame(size=15, origin=[0, 0, 0])
# 估计的
FOR2 = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=15, origin=[-0.85524881, -0.17872652, -9.14765595])
# transformation = np.loadtxt('match_305.txt')

# gt
# FOR2 = o3d.geometry.TriangleMesh.create_coordinate_frame(
#     size=15, origin=[-(171.824-171.292), -(0.124252-0.168724), -(78.0105-68.9384)])
# transformation = np.array([[1, 0, 0, (171.292-171.824)],
#                            [0, 1, 0, (0.168724-0.124252)],
#                            [0, 0, 1, (68.9384-78.0105)],
#                            [0, 0, 0, 1]])

src_pcd = o3d.io.read_point_cloud(path_up)
tgt_pcd = o3d.io.read_point_cloud(path_left)

src_pcd.paint_uniform_color([1, 0.706, 0])  # 黄色
tgt_pcd.paint_uniform_color([0, 0.651, 0.929])  # 蓝色

# src_pcd.transform(transformation)

# o3d.visualization.draw_geometries([tgt_pcd, src_pcd])
# o3d.visualization.draw_geometries([FOR1, tgt_pcd])
# o3d.visualization.draw_geometries([FOR2, src_pcd])
o3d.visualization.draw_geometries([FOR1, tgt_pcd, FOR2, src_pcd])
