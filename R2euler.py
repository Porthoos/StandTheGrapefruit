

import math
import sys

import numpy as np
from scipy.spatial.transform import Rotation as R

#绕X轴逆时针旋转角度θ
def transform_x(x):
    sin = math.sin(x)
    cos = math.cos(x)
    transformation = [
        [1.,  0.,   0., 0 ],
        [0., cos, -sin, 0 ],
        [0., sin,  cos, 0 ],
        [0.,  0.,   0., 1 ]
    ]
    return transformation

#绕Y轴逆时针旋转角度θ
def transform_y(y):
    sin = math.sin(y)
    cos = math.cos(y)
    transformation = [
        [ cos, 0., sin, 0 ],
        [  0., 1.,  0., 0 ],
        [-sin, 0., cos, 0 ],
        [  0., 0.,  0., 1.]
    ]
    return transformation

#绕Z轴逆时针旋转角度θ
def transform_z(z):
    sin = math.sin(z)
    cos = math.cos(z)
    transformation = [
        [cos, -sin, 0., 0 ],
        [sin,  cos, 0., 0 ],
        [0. ,   0., 1., 0 ],
        [0. ,   0., 0., 1.]
    ]
    return transformation

def r2euler(R):
    R = np.array(R)
    err = float(0.001)

    if np.shape(R) != (4, 4):
        print("The size of R matrix is wrong")
        sys.exit(0)
    else:
        pass

    beta = math.atan2(R[0, 2], math.sqrt((R[1, 2]) ** 2 + (R[2, 2]) ** 2))

    if beta >= math.pi / 2 - err and beta <= math.pi / 2 + err:
        beta = math.pi / 2
        # alpha + gamma is fixed
        alpha = 0.0
        gamma = math.atan2(R[1, 0], R[1, 1])
    elif beta >= -(math.pi / 2) - err and beta <= -(math.pi / 2) + err:
        beta = -math.pi / 2
        # alpha - gamma is fixed
        alpha = 0.0
        gamma = math.atan2(R[1, 0], R[1, 1])
    else:
        alpha = math.atan2(-(R[1, 2]) / (math.cos(beta)), (R[2, 2]) / (math.cos(beta)))
        gamma = math.atan2(-(R[0, 1]) / (math.cos(beta)), (R[0, 0]) / (math.cos(beta)))
    return alpha, beta, gamma


if __name__ == "__main__":
    RM = [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]
    angle_0, angle_1, angle_2 = r2euler(RM)
    print("Intrinsic")
    print("Angle about x is {}".format(angle_0))
    print("Angle about y is {}".format(angle_1))
    print("Angle about z is {}".format(angle_2))
    result = np.dot(transform_x(angle_0), np.dot(transform_y(angle_1) , transform_z(angle_2)))
    print(result)



