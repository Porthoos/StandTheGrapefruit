import math
import numpy as np
from pyntcloud import PyntCloud
import PCA1
import ICP
import PointCloud
import draw_row
import move_to_origin
import R2euler as r

camera_center_X = -0.1146
camera_center_Y = 0.5678
camera_center_Z = 0.5855

# angle = [angle_0, angle_1, angle_2]
#弧度转成度
def angle_trans(angle):
    angle_x = angle[0] / math.pi * 180
    angle_y = angle[1] / math.pi * 180
    angle_z = angle[2] / math.pi * 180
    print('angle is: (' + str(angle_x) + ', ' + str(angle_y) + ', ' + str(angle_z) + ')')
    # return angle_x, angle_y, angle_z


def xyz_trans(data, angle):
    x = camera_center_X - data[0]/1000
    y = camera_center_Y + data[2]/1000
    z = camera_center_Z - data[1]/1000
    angle_x = 0 -angle[0] / math.pi * 180
    angle_y = 180 + angle[2] / math.pi * 180
    angle_z = 90 -angle[1] / math.pi * 180
    return x, y, z, angle_x, angle_y, angle_z


path1 = 'models/model/test_tmp_model.ply'
path2 = 'models/kinect6/test3.ply'

point_cloud_pynt1 = PyntCloud.from_file(path1)
points1 = point_cloud_pynt1.points
w1, rows1, center1 = PCA1.PCA(points1)

point_cloud_pynt2 = PyntCloud.from_file(path2)
points2 = point_cloud_pynt2.points
w2, rows2, center2 = PCA1.PCA(points2)

path1 = 'models/model/test_tmp_model.ply'
path2 = 'models/kinect6/test2.ply'

point_cloud_pynt1 = PyntCloud.from_file(path1)
points1 = point_cloud_pynt1.points
w1, rows1, center1 = PCA1.PCA(points1)

point_cloud_pynt2 = PyntCloud.from_file(path2)
points2 = point_cloud_pynt2.points
w2, rows2, center2 = PCA1.PCA(points2)

#-----------------------------
def distance(x,y,z, data_mean):
    return math.sqrt(pow((x - data_mean[0]), 2)+pow((y - data_mean[2]),2)+pow((z - data_mean[1]),2))

def findDirection(path, target):
    point_cloud_pynt1 = PyntCloud.from_file(path)
    print(path)
    print(target)
    points = point_cloud_pynt1.points
    data_mean = np.mean(points, axis=0)
    # print(data_mean)
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
        if i == "end_header\n":
            break

    max = 0
    max_x = 0
    max_y = 0
    for i in data[11:]:
        tmp = i.split(" ")
        x = eval(tmp[0])
        z = eval(tmp[1])
        y = eval(tmp[2])

        if distance(x,y,z, data_mean) > max:
            ##垂直不能用这样切割1！！！
            max = distance(x,y,z, data_mean)
            max_x = x
            max_y = y
            print(x, y)
            print("distance:" + str(distance(x,y,z, data_mean)))


        f_w.writelines(i)
        count += 1

    f.close()
    f_w.close()

    f_tr = open(target, 'r')
    data = f_tr.readlines()
    for i in data[0:]:
        if i.__contains__("element vertex"):
            num = i.split(" ")
            f_tr.close()
            break

    file_data = ""
    with open(target, "r") as f:
        for line in f:
            line = line.replace(num[2],str(count)+"\n")
            file_data += line
    with open(target,"w") as f:
        f.write(file_data)
    # row = [[(max_x - data_mean[0])/max, (max_y - data_mean[2])/max, 0], [0, 0, 1], [-(max_y - data_mean[2])/max, (max_x - data_mean[0])/max, 0]]
    print("###################3")
    print(max_x, max_y)
    print(data_mean)
    row = [[(max_x - data_mean[0])/max, 0, (max_y - data_mean[2])/max],
           [0, -1, 0],
           [-(max_y - data_mean[2])/max, 0, (max_x - data_mean[0])/max]]
    return row
temp = 'models/kinect6'
path333 = temp + '/test2_1.ply'
path444 =   temp + '/test3.ply'
rows2 = findDirection(path333, path444)
#rows2是拍摄出来的点云的特征值

print('--------------------------')

print(rows2)
print(center2)

print('--------------------------')

# print(type(rows1))
print(rows1)
print()

print(np.matmul(rows2, np.transpose(rows1)))
R = np.matmul(rows2, np.transpose(rows1))
R1 = np.matmul([[1, 0, 0], [0, 1, 0], [0, 0, 1]], np.transpose(rows2))
print(center1)
print(center2)

matrix1 = [[R1[0][0], R1[1][0], R1[2][0], 0],
           [R1[0][1], R1[1][1], R1[2][1], 0],
           [R1[0][2], R1[1][2], R1[2][2], 0],
           [0, 0, 0, 1]]
matrix2 = [[R1[0][0], R1[0][1], R1[0][2], 0],
           [R1[1][0], R1[1][1], R1[1][2], 0],
           [R1[2][0], R1[2][1], R1[2][2], 0],
           [0, 0, 0, 1]]
neg_matrix2 = [[-R1[0][0], -R1[0][1], -R1[0][2], 0],
               [-R1[1][0], -R1[1][1], -R1[1][2], 0],
               [-R1[2][0], -R1[2][1], -R1[2][2], 0],
               [0, 0, 0, 1]]
print(matrix1)

draw_row.change_dly(path1, path1+"_with_row", rows1, center1)
draw_row.change_dly(path2, path2+"_with_row", rows2, center2)

draw_row.draw_only_row(path1, path1+"_only_row", rows1, center1)
draw_row.draw_only_row(path2, path2+"_only_row", rows2, center2)

move_to_origin.move(path1, path1+"_at_origin", [[1,0,0],[0,1,0],[0,0,1]], center1)
move_to_origin.move(path2, path2+"_at_origin", rows2, center2)

source = ICP.o3d.io.read_point_cloud(path1+"_at_origin", format='ply')
target = ICP.o3d.io.read_point_cloud(path2+"_at_origin", format='ply')

show0 = ICP.o3d.io.read_point_cloud(path2+"_at_origin", format='ply')
ICP.draw_registration_result(source, target, [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
# ICP.draw_registration_result(source, target, matrix1)
# ICP.draw_registration_result(target, source, matrix1)
ICP.draw_registration_result(source, target, matrix2)
ICP.draw_registration_result(source, target, neg_matrix2)
# ICP.draw_registration_result(target, source, matrix2)
print(111)
threshold = 10
reg_p2p = ICP.o3d.pipelines.registration.registration_icp(
    source, target, threshold, matrix2,
    ICP.o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    ICP.o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100000)
)
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
ICP.draw_registration_result(source, target, reg_p2p.transformation)
tmp = reg_p2p.transformation
print('第一次转置矩阵的角度')
angle_0, angle_1, angle_2 = r.r2euler(reg_p2p.transformation)
print("Angle about x is {}".format(angle_0))
print("Angle about y is {}".format(angle_1))
print("Angle about z is {}".format(angle_2))
ICP.draw_registration_result(source, target, reg_p2p.transformation)
angle = [angle_0, angle_1, angle_2]
x0, y0, z0, angle_x, angle_y, angle_z= xyz_trans(center2, angle)
angle_trans(angle)
# print("position is: (" + str(x0) + ', ' + str(y0) + ', ' + str(z0) + ')')
# print('angle is: (' + str(angle_x) + ', ' + str(angle_y) + ', ' + str(angle_z) + ')')

print(222)
# threshold = 10
# reg_p2p = ICP.o3d.pipelines.registration.registration_icp(
#     source, target, threshold, neg_matrix2,
#     ICP.o3d.pipelines.registration.TransformationEstimationPointToPoint(),
#     ICP.o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100000)
# )
# print(reg_p2p)
# print("Transformation is:")
# print(reg_p2p.transformation)


angle_0, angle_1, angle_2 = r.r2euler(reg_p2p.transformation)
print("Angle about x is {}".format(angle_0))
print("Angle about y is {}".format(angle_1))
print("Angle about z is {}".format(angle_2))
ICP.draw_registration_result(source, target, reg_p2p.transformation)

tmp = reg_p2p.transformation

# source = ICP.o3d.io.read_point_cloud(path1+"_with_row", format='ply')
# target = ICP.o3d.io.read_point_cloud(path2+"_with_row", format='ply')
# # target2 = ICP.o3d.io.read_point_cloud('models/data10/test_tmp2.ply', format='ply')
# threshold = 10
# ICP.draw_registration_result(source, target, [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
# ICP.draw_registration_result(source, target, matrix1)
# ICP.draw_registration_result(target, source, matrix1)
# ICP.draw_registration_result(source, target, matrix2)
# ICP.draw_registration_result(target, source, matrix2)


#-------------------------------------------坐标转移部分
#TODO: 确定标准柚子模型的初始位姿
# (-0.1146, 0.5014, 0.5516)
# camera_center_X = -0.1146
# camera_center_Y = 0.5678
# camera_center_Z = 0.5855
#
angle = [angle_0, angle_1, angle_2]
# def xyz_trans(data, angle):
#     x = camera_center_X - data[0]/1000
#     y = camera_center_Y + data[2]/1000
#     z = camera_center_Z - data[1]/1000
#     angle_x = 0 -angle[0] / math.pi * 180
#     angle_y = 180 + angle[1] / math.pi * 180
#     angle_z = 90 -angle[2] / math.pi * 180
#     return x, y, z, angle_x, angle_y, angle_z

angle = [angle_0, angle_1, angle_2]
x0, y0, z0, angle_x, angle_y, angle_z= xyz_trans(center2, angle)
print("position is: (" + str(x0) + ', ' + str(y0) + ', ' + str(z0) + ')')
print('angle is: (' + str(angle_x) + ', ' + str(angle_y) + ', ' + str(angle_z) + ')')

#----------------------------------------------------------------
