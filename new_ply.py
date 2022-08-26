path = 'models/data1/test_tmp2.ply'
target = 'models/data1/test_tmp55.ply'

def load(path, target):
    f = open(path, 'r')
    f_w = open(target, 'w')
    data = f.readlines()
    for i in data[0:]:
        f_w.writelines(i)
        if i == "end_header\n":
            break

    for i in data[11:]:
        tmp = i.split(" ")

        z = eval(tmp[1])

        i = i.replace(str(z), str(z+500))
        f_w.writelines(i)

    f.close()
    f_w.close()

load(path, target)