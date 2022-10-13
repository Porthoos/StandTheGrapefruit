import pcl
import numpy as np
import open3d as o3d
# # p = pcl.PointCloud(np.array(data, dtype=np.float32))
# # filter_vox = p.make_voxel_grid_filter()   # 体素滤波器
# # filter_vox.set_leaf_size(0.005, 0.005, 0.005)
# # cloud_filtered = filter_vox.filter() # 滤波，得到的数据类型为点云
# temp = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/xyzrgb_temp"
# path3 = temp + '/test_tmp1r.ply'
# path4 = temp + '/test_tmp1r.pcd'
#
# show2 = o3d.io.read_point_cloud(path3, format='ply')
# # o3d.io.write_point_cloud(path4,show2,True)
#
#
# # ## 数据读取
# # np.set_printoptions(suppress=True) # 取消默认的科学计数法
# # Data1 = np.loadtxt('xxxxx.txt',dtype=np.float,skiprows=1,
# #                    delimiter=' ',usecols=(0,1,2),unpack=False)
# ## open3d数据转换
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(show2.points)
# # print(np.asarray(pcd.points))
# o3d.visualization.draw_geometries([pcd])
# # ## 保存成ply数据格式
# # o3d.io.write_point_cloud('xxx.ply',pcd,write_ascii=True) # ascii编码
# # o3d.io.write_point_cloud('xxx.ply',pcd,write_ascii=False) # 非ascii编码
# ## 保存成pcd数据化格式
# o3d.io.write_point_cloud( path4, pcd, write_ascii=True) # ascii编码
# # o3d.io.write_point_cloud('xxx.pcd',pcd,write_ascii=True) # 非ascii编码


p = pcl.PointCloud(np.array(data, dtype=np.float32))
filter_vox = p.make_voxel_grid_filter()   # 体素滤波器
filter_vox.set_leaf_size(0.005, 0.005, 0.005)
cloud_filtered = filter_vox.filter() # 滤波，得到的数据类型为点云

