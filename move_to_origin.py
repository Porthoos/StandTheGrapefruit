import numpy as np

def move(path, target, rows, center):
    count = 0
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:8]:
        f_w.writelines(i)
    c = [0,0,0]
    f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")
    for i in data[8:]:
        num = i.split(" ")
        f_w.writelines(str(float(num[0])-center[0])+" "+str(float(num[1])-center[1])+" "+str(float(num[2])-center[2])+"\n")

    for i in range(360):
        c[0] += rows[0][0]
        c[1] += rows[0][1]
        c[2] += rows[0][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = [0,0,0]
    for i in range(180):
        c[0] += rows[1][0]
        c[1] += rows[1][1]
        c[2] += rows[1][2]
        f_w.writelines(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + "\n")

    c = [0,0,0]
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
            line = line.replace(num[2], str(int(num[2])+721) + "\n")
            file_data += line
    with open(target, "w") as f:
        f.write(file_data)