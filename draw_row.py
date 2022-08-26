import numpy as np


def calculate(dx, dy, dz):
    return 10*dx, 10*dy, 10*dz

def change_dly(path, target, rows, center):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
    c = np.copy(center)
    f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")
    for i in range(180):
        c[0] += rows[0][0]
        c[1] += rows[0][1]
        c[2] += rows[0][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = np.copy(center)
    for i in range(180):
        c[0] += rows[1][0]
        c[1] += rows[1][1]
        c[2] += rows[1][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = np.copy(center)
    for i in range(180):
        c[0] += rows[2][0]
        c[1] += rows[2][1]
        c[2] += rows[2][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    f.close()
    f_w.close()

    f_tr = open(target, 'r')
    # f_tw = open(target, 'w')
    data = f_tr.readlines()
    for i in data[0:]:
        if i.__contains__("element vertex"):
            num = i.split(" ")
            # i = i.replace(num[2], str(count))
            # f_tw.write(i)
            f_tr.close()
            break

    file_data = ""
    with open(target, "r") as f:
        for line in f:
            line = line.replace(num[2], str(int(num[2])+541) + "\n")
            file_data += line
    with open(target, "w") as f:
        f.write(file_data)

# path = "models/test2.ply"
# target = "models/test3.ply"
# # change_dly(path, target,
# #            [[-0.95904315,0.18228981,-0.21681015], [-0.2807001,-0.7142776,0.6411045], [-0.03799582,0.6757055,0.7361918]],
# #            [104.980019, 661.220642, -56.666531])
#
# # change_dly(path, target,
# #            [[0.05186973,-0.107306,0.99287206], [-0.6400982,-0.7667018,-0.04942226], [0.76654017,-0.6329721,-0.10845499]],
# #            [-43.763203, 626.944336, 15.824592])
#
# change_dly(path, target,
#            [[-0.39963213,0.38350046,0.8325993], [-0.8028637,-0.5847656,-0.11601292], [0.4423844,-0.7148263,0.54158974]],
#            [164.091751, 672.851196, -61.135433])


def draw_only_row(path, target, rows, center):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:8]:
        f_w.writelines(i)
    c = np.copy(center)
    f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")
    for i in range(480):
        c[0] += rows[0][0]
        c[1] += rows[0][1]
        c[2] += rows[0][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")


    for i in range(300):
        c = np.copy(center)
        c[0] += rows[1][0] * i
        c[1] += rows[1][1] * i
        c[2] += rows[1][2] * i
        for j in range(480):
            c[0] += rows[0][0]
            c[1] += rows[0][1]
            c[2] += rows[0][2]
            f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = np.copy(center)
    for i in range(240):
        c[0] += rows[1][0]
        c[1] += rows[1][1]
        c[2] += rows[1][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    for i in range(100):
        c = np.copy(center)
        c[0] += rows[2][0] * i
        c[1] += rows[2][1] * i
        c[2] += rows[2][2] * i
        for j in range(240):
            c[0] += rows[1][0]
            c[1] += rows[1][1]
            c[2] += rows[1][2]
            f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = np.copy(center)
    for i in range(120):
        c[0] += rows[2][0]
        c[1] += rows[2][1]
        c[2] += rows[2][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    f.close()
    f_w.close()

    f_tr = open(target, 'r')
    # f_tw = open(target, 'w')
    data = f_tr.readlines()
    for i in data[0:]:
        if i.__contains__("element vertex"):
            num = i.split(" ")
            # i = i.replace(num[2], str(count))
            # f_tw.write(i)
            f_tr.close()
            break

    file_data = ""
    with open(target, "r") as f:
        for line in f:
            line = line.replace(num[2], str(168840) + "\n")
            file_data += line
    with open(target, "w") as f:
        f.write(file_data)