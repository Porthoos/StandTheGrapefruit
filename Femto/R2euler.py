"""
FileName: r2euler_self.py
File to caluculate euler from rotation matrix
Method of using basic matrix equations
Input str in upper -- intrinsic
Input str in lower -- extrinsic
"""

import math
import sys

import numpy as np
from scipy.spatial.transform import Rotation as R


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



