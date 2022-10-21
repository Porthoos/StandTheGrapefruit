import ICP
import open3d as o3d
import delete_remote as dr
def transform(points, x, y, z):
    transformation = [
        [1., 0., 0., x ],
        [0., 1., 0., y ],
        [0., 0., 1., z ],
        [0., 0., 0., 1.]
    ]
    points.transform(transformation)


# source = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/test"
# path1 =   source + '/RGBDPoints_20221020172417.ply'
# path2 =   source + '/RGBDPoints_20221020172428.ply'
# path3 =   source + '/RGBDPoints_20221020172455.ply'
# path4 =   source + '/RGBDPoints_20221020172506.ply'
# path5 =   source + '/RGBDPoints_20221020172518.ply'
# path1_1 =   source + '/RGBDPoints_20221020172417_n.ply'
# path2_1 =   source + '/RGBDPoints_20221020172428_n.ply'
# path3_1 =   source + '/RGBDPoints_20221020172455_n.ply'
# path4_1 =   source + '/RGBDPoints_20221020172506_n.ply'
# path5_1 =   source + '/RGBDPoints_20221020172518_n1.ply'
# path1_2 =   source + '/RGBDPoints_20221020172417_n1.ply'
# path2_2 =   source + '/RGBDPoints_20221020172428_n1.ply'
# path3_2 =   source + '/RGBDPoints_20221020172455_n1.ply'
# path4_2 =   source + '/RGBDPoints_20221020172506_n1.ply'
# path5_2 =   source + '/RGBDPoints_20221020172518_n1.ply'
#
# # dr.load_ply(path1, path1_1)
# # dr.load_ply(path2, path2_1)
# # dr.load_ply(path3, path3_1)
# # dr.load_ply(path4, path4_1)
# # dr.load_ply(path5, path5_1)
#
# # dr.load_plyn(path1, path1_2)
# # dr.load_plyn(path2, path2_2)
# # dr.load_plyn(path3, path3_2)
# # dr.load_plyn(path4, path4_2)
# # dr.load_plyn(path5, path5_2)
#
# show1 = ICP.o3d.io.read_point_cloud(path1_1, format='ply')
# show2 = ICP.o3d.io.read_point_cloud(path2_1, format='ply')
# show3 = ICP.o3d.io.read_point_cloud(path3_1, format='ply')
# show4 = ICP.o3d.io.read_point_cloud(path4_1, format='ply')
# show5 = ICP.o3d.io.read_point_cloud(path5_1, format='ply')
# # dr.load_ply(path3, path3_1)
# show2_1 = ICP.o3d.io.read_point_cloud(path3_1, format='ply')
# o3d.visualization.draw_geometries([show2])
# # o3d.visualization.draw_geometries([show1, show5, show2])
# #1 4 5


source = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/test1"
path0 =   source + '/RGBDPoints_20221020175652.ply'
path1 =   source + '/RGBDPoints_20221020175723.ply'
path2 =   source + '/RGBDPoints_20221020175736.ply'
path3 =   source + '/RGBDPoints_20221020175804.ply'

path0_1 =   source + '/RGBDPoints_20221020175652_new.ply'
path1_1 =   source + '/RGBDPoints_20221020175723_new.ply'
path2_1 =   source + '/RGBDPoints_20221020175736_new.ply'
path3_1 =   source + '/RGBDPoints_20221020175804_new.ply'
# dr.load_ply(path0, path0_1)
# dr.load_ply(path1, path1_1)
# dr.load_ply(path2, path2_1)
# dr.load_plyn(path3, path3_1)

show0 = ICP.o3d.io.read_point_cloud(path0_1, format='ply')
show1 = ICP.o3d.io.read_point_cloud(path1_1, format='ply')
show2 = ICP.o3d.io.read_point_cloud(path2_1, format='ply')
show3 = ICP.o3d.io.read_point_cloud(path3_1, format='ply')

# show2_1 = ICP.o3d.io.read_point_cloud(path3_1, format='ply')
# o3d.visualization.draw_geometries([show2_1])
o3d.visualization.draw_geometries([show3])





# source = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/test2"
# path0 =   source + '/RGBDPoints_20221020181533.ply'
# path1 =   source + '/RGBDPoints_20221020181603.ply'
#
#
# # path0_1 =   source + '/RGBDPoints_20221020175652_new.ply'
# # path1_1 =   source + '/RGBDPoints_20221020175723_new.ply'
# # path2_1 =   source + '/RGBDPoints_20221020175736_new.ply'
# # path3_1 =   source + '/RGBDPoints_20221020175804_new.ply'
# # dr.load_ply(path0, path0_1)
# # dr.load_ply(path1, path1_1)
# # dr.load_ply(path2, path2_1)
# # dr.load_ply(path3, path3_1)
#
# show0 = ICP.o3d.io.read_point_cloud(path0, format='ply')
# show1 = ICP.o3d.io.read_point_cloud(path1, format='ply')
# axis_left = o3d.geometry.TriangleMesh.create_coordinate_frame(size=15, origin=[0, 0, 0])
#
# # show2_1 = ICP.o3d.io.read_point_cloud(path3_1, format='ply')
# # o3d.visualization.draw_geometries([show2_1])
# transform(show1,120,0,-50)
# o3d.visualization.draw_geometries([show0,show1,axis_left])