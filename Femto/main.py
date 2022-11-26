import time

import robotcontrol as rc
import Femto.getTransInit as gt
import run_mzy as run
import sys

def main():
    start = time.time()
    robot = rc.Auboi5Robot()
    speed = 0.5
    rc.init_robot(robot, speed)
    i = 0
    while True:
        print("num: "+ str(i))
        time1 = time.time()
        print("time1"+str(time1))
        if time.time() - start > 200:
            break
        run.shoot()
        print("finish shoot")
        time2 = time.time()-time1
        print("time2"+str(time2))
        run.reload_total()
        print("finish reload")
        time3 = time.time()-time2
        print("time3"+str(time3))
        x, y, z, angle_final = gt.getTransInit_final()
        print("finish gettransInit")
        time4 = time.time()-time3
        print("time4"+str(time4))
        rc.move2Target(robot, x, y, z, angle_final)
        print("finish move")
        time5 = time.time()-time4
        print("time5"+str(time5))
        i+=1

    sys.exit()



if __name__ == '__main__':
    main()