import reload_Femto as reload
import ICP
import open3d as o3d
# source = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb"
# temp = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb_temp"
# judge = 'left'
# path1 = ""
# path2 = ""
# path3 = ""
# path5 = source + "/RGBDPoints_20221012220045.ply"
# if judge == 'right':
#     path1 =   source + '/RGBDPoints_20221011220237r2.ply'
#     path2 =   temp + '/test_tmp1r.ply'
#     path3 =   temp + '/test_tmp2r.ply'
#     path3_1 = temp + '/test_tmp2r_1.ply'
#     path4 =   temp + '/test_tmp3r.ply'
# elif judge == "left":
#     path1 = source + '/RGBDPoints_20221018165101left.ply'
#     path2 = temp + '/test_tmp1l.ply'
#     path3 = temp + '/test_tmp2l.ply'
#     path3_1 = temp + '/test_tmp2l_1.ply'
#     path4 = temp + '/test_tmp3l.ply'
# elif judge == "up":
#     path1 =   source + '/RGBDPoints_20221018165123up.ply'
#     path2 =   temp + '/test_tmp1u.ply'
#     path3 =   temp + '/test_tmp2u.ply'
#     path3_1 = temp + '/test_tmp2u_1.ply'
#     path4 =   temp + '/test_tmp3u.ply'
# elif judge == "other":
#     path1 = source + "/RGBDPoints_20221012223343.ply"
#     path2 = temp + '/test_tmp1o.ply'
#     path3 = temp + '/test_tmp2o.ply'
#     path3_1 = temp + '/test_tmp2o_1.ply'
#     path4 = temp + '/test_tmp3o.ply'
# elif judge == "white":
#     path1 = source + "/RGBDPoints_20221013092916.ply"
#     path2 = temp + '/test_tmp1w.ply'
#     path3 = temp + '/test_tmp2w.ply'
#     path3_1 = temp + '/test_tmp2w_1.ply'
#     path4 = temp + '/test_tmp3w.ply'
# elif judge == "ballone":
#     path1 = source + "/RGBDPoints_20221018163113ball.ply"
#     path2 = temp + '/test_tmp1b.ply'
#     path3 = temp + '/test_tmp2b.ply'
#     path3_1 = temp + '/test_tmp2b_1.ply'
#     path4 = temp + '/test_tmp3b.ply'
# elif judge == "balltwo":
#     path1 = source + "/RGBDPoints_20221018163136ball.ply"
#     path2 = temp + '/test_tmp1bb.ply'
#     path3 = temp + '/test_tmp2bb.ply'
#     path3_1 = temp + '/test_tmp2bb_1.ply'
#     path4 = temp + '/test_tmp3bb.ply'

# show4 = ICP.o3d.io.read_point_cloud(path5, format='ply')
# o3d.visualization.draw_geometries([show4])

# # path1 = 'models/model/test_tmp_model.ply'
# # path2 = 'models/model/test_tmp_model.ply_at_origin'
# path0 = 'models/model/test_tmp_model.ply_at_origin'
# path1 = 'models/kinect5/test2.ply_at_origin'
# path2 = 'models/kinect6/test2.ply_at_origin'
# path0_0 = 'models/model/test_tmp_model.ply'
# path1_0 = 'models/kinect5/test2.ply'
# path2_0 = 'models/kinect6/test2.ply'
# # path2 = 'models/kinect6/test2.ply_at_origin'
# # path2 = 'models/kinect6/test2.ply'
# show0 = ICP.o3d.io.read_point_cloud(path0, format='ply')
# show1 = ICP.o3d.io.read_point_cloud(path1, format='ply')
# show2 = ICP.o3d.io.read_point_cloud(path2, format='ply')
#
# show0_0 = ICP.o3d.io.read_point_cloud(path0_0, format='ply')
# show1_0 = ICP.o3d.io.read_point_cloud(path1_0, format='ply')
# show2_0 = ICP.o3d.io.read_point_cloud(path2_0, format='ply')
#
# o3d.visualization.draw_geometries([show0, show1, show2])

# show2 = ICP.o3d.io.read_point_cloud(path3, format='ply')
# o3d.visualization.draw_geometries([show2])

path0 = 'models/kinect7/test2_1.ply'
show0 = ICP.o3d.io.read_point_cloud(path0, format='ply')
o3d.visualization.draw_geometries([show0])