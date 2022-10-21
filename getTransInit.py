import math
import numpy as np
from pyntcloud import PyntCloud
import PCA1
import ICP
import draw_row
import move_to_origin
import R2euler as r2e

# Angle_X = 0
# Angle_Y = 0
# Angle_Z = 0
#
# matrix_X = [[1, 0, 0],
#             [0, math.cos(Angle_X), math.sin(Angle_X)],
#             [0, -math.sin(Angle_X), math.cos(Angle_X)]]
#
# matrix_Y = [[math.cos(Angle_Y), 0, -math.sin(Angle_Y)],
#             [0, 1, 0],
#             [math.sin(Angle_Y), 0, math.cos(Angle_Y)]]
#
# matrix_Z = [[math.cos(Angle_Z), math.sin(Angle_Z), 0],
#             [-math.sin(Angle_Z), math.cos(Angle_Z), 0],
#             [0, 0, 1]]
#
# matrix = np.dot(np.dot(matrix_X, matrix_Y), matrix_Z)
#
# matrix1 = [[math.cos(Angle_Z)*math.cos(Angle_Y), math.sin(Angle_Y)*math.cos(Angle_X)+math.cos(Angle_Z)*math.sin(Angle_Y)*math.sin(Angle_X), math.sin(Angle_Z)*math.sin(Angle_X)-math.cos(Angle_Z)*math.sin(Angle_Y)*math.cos(Angle_X)],
#            [-math.sin(Angle_Z)*math.cos(Angle_Y), math.cos(Angle_Z)*math.cos(Angle_X)-math.sin(Angle_Z)*math.sin(Angle_Y)*math.sin(Angle_X), math.cos(Angle_Z)*math.sin(Angle_X)+math.sin(Angle_Z)*math.sin(Angle_Y)*math.cos(Angle_X)],
#            [math.sin(Angle_Y), -math.cos(Angle_Y)*math.sin(Angle_X), math.cos(Angle_Y)*math.cos(Angle_X)]]

# path1 = 'models/data7/test_tmp_model.ply'
# path2 = 'models/data9/test_tmp2.ply'

path1 = 'models/model/test_tmp_model.ply'
path2 = 'models/data10/test_tmp2.ply'

point_cloud_pynt1 = PyntCloud.from_file(path1)
points1 = point_cloud_pynt1.points
w1, rows1, center1 = PCA1.PCA(points1)

point_cloud_pynt2 = PyntCloud.from_file(path2)
points2 = point_cloud_pynt2.points
w2, rows2, center2 = PCA1.PCA(points2)

# print(type(rows1))
print(rows1)
print()
# print(np.transpose(rows1))
# print()
print(rows2)
print()
# print(np.transpose(rows2))

print(np.matmul(rows2, np.transpose(rows1)))
R = np.matmul(rows2, np.transpose(rows1))
R1 = np.matmul([[1,0,0],[0,1,0],[0,0,1]], np.transpose(rows2))
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

# p, q
# p = R * q
# p * qT = R * q * qT
# p * qT = R

# p,I,q
# I = R1 * p
# R1 = I * pT
# q = R2 * I
# R2 = q * I
# R = R2 * R1 = q * pT
# q = R * p = R2 * R1 * p = R2 * I

for i in range(12) :
    if i == 0 or i == 7:
        continue
    path1 = 'models/model/test_tmp_model.ply'
    path2 = 'models/data' + str(i) + '/test_tmp2.ply'

    point_cloud_pynt1 = PyntCloud.from_file(path1)
    points1 = point_cloud_pynt1.points
    w1, rows1, center1 = PCA1.PCA(points1)

    point_cloud_pynt2 = PyntCloud.from_file(path2)
    points2 = point_cloud_pynt2.points
    w2, rows2, center2 = PCA1.PCA(points2)

    # print(type(rows1))
    print(rows1)
    print()
    # print(np.transpose(rows1))
    # print()
    print(rows2)
    print()
    # print(np.transpose(rows2))

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

    ICP.draw_registration_result(source, target, [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
    # ICP.draw_registration_result(source, target, matrix1)
    # ICP.draw_registration_result(target, source, matrix1)
    ICP.draw_registration_result(source, target, matrix2)
    ICP.draw_registration_result(source, target, neg_matrix2)
    # ICP.draw_registration_result(target, source, matrix2)

    threshold = 10
    reg_p2p = ICP.o3d.pipelines.registration.registration_icp(
        source, target, threshold, matrix2,
        ICP.o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        ICP.o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100000)
    )
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)
    print("Eluer is:")
    angle_0, angle_1, angle_2 = r2e.r2euler(reg_p2p.transformation)
    print("Angle about x is {}".format(angle_0))
    print("Angle about y is {}".format(angle_1))
    print("Angle about z is {}".format(angle_2))
    result = np.dot(r2e.transform_x(angle_0), np.dot(r2e.transform_y(angle_1), r2e.transform_z(angle_2)))
    print(result)
    ICP.draw_registration_result(source, target, reg_p2p.transformation)
    tmp = reg_p2p.transformation

    threshold = 10
    reg_p2p = ICP.o3d.pipelines.registration.registration_icp(
        source, target, threshold, neg_matrix2,
        ICP.o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        ICP.o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100000)
    )
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)
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
