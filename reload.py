import numpy as np
from pyntcloud import PyntCloud

def load_pcd_data(file_path):
    pts = []
    f = open(file_path, 'r')
    data = f.readlines()
    f.close()
    line = data[9]
    # print line
    line = line.strip('\n')
    i = line.split(' ')
    pts_num = eval(i[-1])
    for line in data[11:]:
        line = line.strip('\n')
        xyzrgba = line.split(' ')
        x, y, z = [eval(i) for i in xyzrgba[:3]]
        rgba = xyzrgba[-1]
        # print type(bgra)
        rgba = bin(eval(rgba))[2:]
        r, g, b = [int(rgba[8*i:8*i+8], 2) for i in range(3)]
        pts.append([x, y, z, r, g, b])
        # pts.append()
    assert len(pts) == pts_num
    res = np.zeros((pts_num, len(pts[0])), dtype=np.float)
    for i in range(pts_num):
        res[i] = pts[i]
    return res

# path = 'models/my_test_cloud_1.pcd'
# points = load_pcd_data(path)
# print(points)


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
        z = eval(tmp[1])
        y = eval(tmp[2])

        # if r < 200 and g < 200 and b > 50:
        #     continue
        # f_w.writelines(i)
        # count += 1

        # if r < 80 and g < 80 and b < 80:
        #     continue
        # elif r < 80 and g < 80 and b > 200:
        #     continue
        # elif r < 80 and g > 200 and b < 80:
        #     continue
        # f_w.writelines(i)
        # count += 1

        if x > 650 or y > 675:
            continue
        if r < 150 and g < 150 and b < 150:
            continue
        if z > 900:
            continue
        if r > b and g > b:
            f_w.writelines(i)
            count += 1
        # if r>=150 and g>=1 and b<=100:
        #     f_w.writelines(i)
        #     count += 1
        # if r >= 150 and g >= 1 and b <= 100:
        #     f_w.writelines(i)
        #     count += 1

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


def load_ply_gemini(path, target):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
        if i == "end_header\n":
            break

    for i in data[15:]:
        tmp = i.split(" ")
        r = eval(tmp[3])
        g = eval(tmp[4])
        b = eval(tmp[5])
        x = eval(tmp[0])
        z = eval(tmp[1])
        y = eval(tmp[2])

        # if r < 200 and g < 200 and b > 50:
        #     continue
        # f_w.writelines(i)
        # count += 1

        # if r < 80 and g < 80 and b < 80:
        #     continue
        # elif r < 80 and g < 80 and b > 200:
        #     continue
        # elif r < 80 and g > 200 and b < 80:
        #     continue
        # f_w.writelines(i)
        # count += 1

        # if x > 650 or y > 675:
        #     continue
        # if r < 150 and g < 150 and b < 150:
        #     continue
        # if z > 900:
        #     continue
        # if r > b and g > b:
        #     f_w.writelines(i)
        #     count += 1

        if z == 0 or x == 0 or y == 0:
            continue
        if y > 0.52:
            continue
        f_w.writelines(i)
        count += 1
        # if r>=150 and g>=1 and b<=100:
        #     f_w.writelines(i)
        #     count += 1
        # if r >= 150 and g >= 1 and b <= 100:
        #     f_w.writelines(i)
        #     count += 1

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


def remove_unreliable_point(path, target):
    points = PyntCloud.from_file(path).points
    # max = np.max(points[1])
    print(type(points))
    print(points.shape)
    print(np.max(points['x'], axis = 0))
    print(np.max(points['y'], axis = 0))
    print(np.max(points['z'], axis = 0))
    max = np.max(points['y'], axis = 0) - 50
    print(max,"nababab")
    min = np.min(points['y'], axis = 0)
    print(min, "nababab")

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
        x = eval(tmp[0])
        z = eval(tmp[1])
        y = eval(tmp[2])

        # if z > max - 10:
        #     continue
        if z > max:
            continue
        j1 = i.replace(str(z), str(max - 0.9*(max-z))) #data8
        # j2 = i.replace(str(z), str(max + 0.6*(max-z)))
        # i = i.replace(str(z), str(max - 1 * (max - z)))  # data9
        f_w.writelines(j1)
        # f_w.writelines(j2)
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

def remove_color(path, target):
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:7]:
        f_w.writelines(i)
    f_w.writelines("end_header\n")
    for i in data[11:]:
        tmp = i.split(" ")
        # print(tmp)
        # print(type(i))
        # i = i.replace(tmp[3], "")
        # i = i.replace(tmp[4], "")
        # i = i.replace(tmp[5], "")
        # i = str(tmp[:3])

        i = " ".join(tmp[:3])
        i += '\n'
        # i = i.join("\n")
        f_w.writelines(i)


def remove_color_gemini(path, target):
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:7]:
        f_w.writelines(i)
    f_w.writelines("end_header\n")
    for i in data[14:]:
        tmp = i.split(" ")
        # print(tmp)
        # print(type(i))
        # i = i.replace(tmp[3], "")
        # i = i.replace(tmp[4], "")
        # i = i.replace(tmp[5], "")
        # i = str(tmp[:3])

        i = " ".join(tmp[:3])
        i += '\n'
        # i = i.join("\n")
        f_w.writelines(i)



# path = 'models/test.ply'
# count = 0
# target = 'models/test1.ply'
# target1 = 'models/test2.ply'
# load_ply(path, target)
# remove_color(target, target1)
