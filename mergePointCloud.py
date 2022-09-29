from mayavi import mlab
import numpy as np


def ply_read(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


# 将每一行数据分割后转为数字
def ls2n(line):
    line = line.strip().split(' ')
    return list(map(float, line))


def viz_mayavi(points):
    x = points[:, 0]  # x position of point
    y = points[:, 1]  # y position of point
    z = points[:, 2]  # z position of point
    fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mlab.points3d(x, y, z,
                  y,  # Values used for Color
                  mode="point",
                  colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                  # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                  figure=fig,
                  )
    mlab.show()


if __name__ == '__main__':
    file_path = 'models/dataTwoKinect/test_tmp1.ply'
    points = ply_read(file_path)
    points = points[10:(10 + 40256)]
    points1 = np.array(list(map(lambda x: ls2n(x), points)))

    file_path = 'models/dataTwoKinect1/test_tmp1.ply'
    points = ply_read(file_path)
    points = points[24:(24 + 40097)]
    points2 = np.array(list(map(lambda x: ls2n(x), points)))

    print(points1.shape)
    points3 = np.concatenate((points1, points2), axis=0)
    print(points3.shape)
    viz_mayavi(points3)