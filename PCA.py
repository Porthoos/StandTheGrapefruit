import open3d as o3d
import os
import numpy as np
from pyntcloud import PyntCloud

def PCA(data, correlation=False, sort=True):
    data = data.transpose()
    data = data - data.mean(axis=1, keepdims=True)
    data_T = data.transpose()
    H = np.matmul(data, data_T)
    eigenvectors, eigenvalues, _ = np.linalg.svd(H, full_matrices=True)
    if sort:
        sort = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[sort]
        eigenvectors = eigenvectors[:, sort]

    return eigenvalues, eigenvectors


def main():
    point_cloud_pynt = PyntCloud.from_file("models/mate/lyy1.ply")
    point_cloud_o3d = point_cloud_pynt.to_instance("open3d", mesh=False)
    o3d.visualization.draw_geometries([point_cloud_o3d])
    points = np.array(point_cloud_pynt.points)

    # print('total points number is:', points.shape[0])
    w, v = PCA(points)
    point_cloud_vector = v[:, 1]
    print('the main orientation of this pointcloud is: ', point_cloud_vector)

    projected_points = np.dot(points, v[:, :2])
    ##np.vstack()
    # np.hstack()
    projected_points = np.hstack([projected_points, np.zeros((projected_points.shape[0], 1))])

    projected_point_cloud_o3d = o3d.geometry.PointCloud()
    projected_point_cloud_o3d.points = o3d.utility.Vector3dVector(projected_points)
    o3d.visualization.draw_geometries([projected_point_cloud_o3d])

    pcd_tree = o3d.geometry.KDTreeFlann(point_cloud_o3d)
    normals = []

    cloud_range = points.max(axis=0) - points.min(axis=0)
    # dadius: set to 5% of the cloud's max range
    radius = cloud_range.max() * 0.05
    for point in point_cloud_o3d.points:
        cnt, idxs, dists = pcd_tree.search_radius_vector_3d(point, radius)
        # print("count",cnt)
        # print("dists",len(dists))
        # v:3*3 matrix
        w, v = PCA(points[idxs])
        # v[:,-1]:3*1 matrix
        normal = v[:, -1]
        normals.append(normal)
    normals = np.array(normals, dtype=np.float64)
    print("normals", normals)
    # TODO: 此处把法向量存放在了normals中
    point_cloud_o3d.normals = o3d.utility.Vector3dVector(normals)
    # o3d.visualization.draw_geometries([point_cloud_o3d])

    o3d.visualization.draw_geometries([point_cloud_o3d], "Open3D normal estimation", width=800, height=600, left=50, top=50,
                                      point_show_normal=True, mesh_show_wireframe=False,
                                      mesh_show_back_face=False)

    normal_point1 = o3d.utility.Vector3dVector(point_cloud_o3d.normals)
    normals1 = o3d.geometry.PointCloud()
    normals1.points = normal_point1
    normals1.paint_uniform_color((0, 1, 0))  # 点云法向量的点都以绿色显示
    o3d.visualization.draw_geometries([point_cloud_o3d, normals1], "Open3D noramls points", width=800, height=600, left=50, top=50,
                                      point_show_normal=False, mesh_show_wireframe=False,
                                      mesh_show_back_face=False)


if __name__ == '__main__':
    main()