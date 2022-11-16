import numpy as np

# path = 'models/my_test_cloud_1.pcd'
# points = load_pcd_data(path)
# print(points)
import PointCloud


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
        # r = eval(tmp[3])
        # g = eval(tmp[4])
        # b = eval(tmp[5])
        x = eval(tmp[0])
        z = eval(tmp[1])
        y = eval(tmp[2])

        threshold = 835
        mult = 1.3

        if z > threshold:
            continue
        # if r > b and g > b:
        i = i.replace(tmp[1], str(threshold - mult * (threshold-z)))
        f_w.writelines(i)
        print(i)
        print(tmp[1])
        i = i.replace(str(threshold - mult * (threshold-z)), str(2*threshold - (threshold - mult * (threshold-z))))
        print(i)
        f_w.writelines(i)
        count += 2

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
            line = line.replace(num[2],str(count)+"\n")
            file_data += line
    with open(target,"w") as f:
        f.write(file_data)


path = 'models/model2/model2.ply'
count = 0
target = 'models/model2/test_tmp_model.ply'
load_ply(path, target)
pcl = PointCloud.Cloud(target)
