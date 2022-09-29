# from mayavi import mlab
import numpy as np
import open3d as o3d
import copy

print(o3d.__version__)


def ply_read(file_path):
    lines = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines


# 将每一行数据分割后转为数字
def ls2n(line):
    line = line.strip().split(' ')
    return list(map(float, line))


def viz_mayavi_3(points1, points2, points3):
    x = points1[:, 0]  # x position   of point
    y = points1[:, 1]  # y position   of point
    z = points1[:, 2]  # z position   of point
    fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mlab.points3d(x, y, z, z, mode="point", color=(0, 1, 0), figure=fig)

    x = points2[:, 0]  # x position   of point
    y = points2[:, 1]  # y position   of point
    z = points2[:, 2]  # z position   of point
    mlab.points3d(x, y, z, z, mode="point", color=(1, 0, 0), figure=fig)

    x = points1[:, 0]  # x position   of point
    y = points1[:, 1]  # y position   of point
    z = points1[:, 2]  # z position   of point
    mlab.points3d(x, y, z, z, mode="point", color=(0, 0, 1), figure=fig)

    mlab.show()

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


if __name__ == '__main__':
    # demo_icp_pcds = o3d.data.DemoICPPointClouds()
    source = o3d.io.read_point_cloud('models/data7/test_tmp_model.ply_only_row', format='ply')
    target1 = o3d.io.read_point_cloud('models/data9/test_tmp2.ply_only_row', format='ply')
    # target2 = o3d.io.read_point_cloud('models/data10/test_tmp2.ply', format='ply')
    threshold = 100000
    trans_init = np.asarray([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
    draw_registration_result(source, target1, trans_init)

    print("Initial alignment")
    evaluation = o3d.pipelines.registration.evaluate_registration(
        source, target1, threshold, trans_init)
    print(evaluation)


    target1.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.02, max_nn=30))



    reg_p2p = o3d.pipelines.registration.registration_icp(
        source, target1, threshold,[[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]],
        o3d.pipelines.registration.TransformationEstimationPointToPlane(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100000)
    )
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)
    draw_registration_result(source, target1, reg_p2p.transformation)
    tmp = reg_p2p.transformation

    # for i in range(10) :
    #     threshold /= 10
    #     reg_p2p = o3d.pipelines.registration.registration_icp(
    #         source, target1, threshold, tmp,
    #         o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    #         o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=10000)
    #     )
    #     print(reg_p2p)
    #     print("Transformation is:")
    #     print(reg_p2p.transformation)
    #     draw_registration_result(source, target1, reg_p2p.transformation)
    #     tmp = reg_p2p.transformation

    # reg_p2p1 = o3d.pipelines.registration.registration_icp(
    #     source, target1, threshold,reg_p2p.transformation,
    #     o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    #     # o3d.pipelines.registration.TransformationEstimationForColoredICP(),
    #     # o3d.pipelines.registration.TransformationEstimationForGeneralizedICP(),
    #     # o3d.pipelines.registration.TransformationEstimationPointToPlane(),
    #     o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=10000)
    # )
    # print(reg_p2p1)
    # print("Transformation is:")
    # print(reg_p2p1.transformation)
    # draw_registration_result(source, target1, reg_p2p1.transformation)


    # target2.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.02, max_nn=30))
    #
    # evaluation = o3d.pipelines.registration.evaluate_registration(
    #     source, target2, threshold, trans_init)
    # print(evaluation)
    # reg_p2p = o3d.pipelines.registration.registration_icp(
    #     source, target2, threshold,[[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]],
    #     o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    #     # o3d.pipelines.registration.TransformationEstimationForColoredICP(),
    #     o3d.pipelines.registration.ICPConvergenceCriteria(relative_fitness= 1e-06, relative_rmse = 1e-06, max_iteration= 10000)
    # )
    # print(reg_p2p)
    # print("Transformation is:")
    # print(reg_p2p.transformation)
    # draw_registration_result(source, target2, reg_p2p.transformation)