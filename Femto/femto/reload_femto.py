import math

import numpy as np
from pyntcloud import PyntCloud

def distance(x,y,z, data_mean):
    return math.sqrt(pow((x - data_mean[0]), 2)+pow((y - data_mean[2]),2)+pow((z - data_mean[1]),2))



def load_ply(path, target):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
        if i == "end_header\n":
            break

    for i in data[11:]:
        tmp = i.split(" ")
        r = eval(tmp[3])
        g = eval(tmp[4])
        b = eval(tmp[5])
        x = eval(tmp[0])
        y = eval(tmp[1])
        z = eval(tmp[2])


        if x==0 and y==0 and z==0:
            continue
        if z < 300:
            continue
        if x > 300 or y > 275:
            continue
        if x < -300 or y < -275:
            continue
        if r < 150 and g < 150 and b < 150:
            continue
        if z > 760:
            continue
        f_w.writelines(i)
        count += 1

    f.close()
    f_w.close()

# 生成一个z轴相同的点云
def remove_unreliable_point(path, target):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
        if i == "end_header\n":
            break

    for i in data[11:]:
        tmp = i.split(" ")
        z = eval(tmp[2])
        j1 = i.replace(str(z), str(750) )#data8
        f_w.writelines(j1)
        count += 1

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
            line = line.replace(num[2], str(count) + "\n")
            file_data += line
    with open(target, "w") as f:
        f.write(file_data)

#传入remove_unreliable_point生成z轴相同的点云，算出来该平面最远的点从而来算轴
def findxy(path, target):
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
        y = eval(tmp[1])
        z = eval(tmp[2])

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
    row = [[(max_x - data_mean[0])/max, (max_y - data_mean[2])/max, 0],
           [0, 0, -1],
           [-(max_y - data_mean[2])/max, (max_x - data_mean[0])/max, 0]]
    return row


def remove_color(path, target):
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:6]:
        f_w.writelines(i)
    f_w.writelines("end_header\n")
    for i in data[11:]:
        tmp = i.split(" ")
        i = " ".join(tmp[:3])
        i += '\n'
        f_w.writelines(i)

