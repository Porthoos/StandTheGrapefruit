import Pipeline
import StreamProfile
from Error import ObException
import cv2
import numpy as np


try:
    #创建一个Pipeline，Pipeline是整个高级API的入口，通过Pipeline可以很容易的打开和关闭
    #多种类型的流并获取一组帧数据
    camera_factor = 1000
    camera_cx = 322.274
    camera_cy = 243.305
    camera_fx = 490.007
    camera_fy = 490.007
    pipe = Pipeline.Pipeline( None )

    #获取深度相机的所有流配置，包括流的分辨率，帧率，以及帧的格式
    profiles = pipe.getStreamProfileList( Pipeline.PY_SENSOR_DEPTH)

    #通过遍历深度流的配置来获取要使用的帧格式，这里将使用YUYV格式来打开流
    count = profiles.count( )
    for i in range( count ):
        profile = profiles.getProfile( i )
        videoProfile = profile.toViedo()
        if videoProfile.format() == StreamProfile.PY_FORMAT_YUYV or videoProfile.format() == StreamProfile.PY_FORMAT_Y16:
            depthProfle = videoProfile
            break

    #通过创建Config来配置Pipeline要启用或者禁用哪些流，这里将启用深度流
    config = Pipeline.Config()
    config.enableStream( depthProfle )

    #启动在Config中配置的流，如果不传参数，将启动默认配置启动流
    pipe.start( config )

    width = depthProfle.width()
    height = depthProfle.height()

    while True:
        #以阻塞的方式等待一帧数据，该帧是一个复合帧，里面包含配置里启用的所有流的帧数据，
        #并设置帧的等待超时时间为100ms
        frameSet = pipe.waitForFrames( 100 )
        if frameSet == None:
            continue
        else:
            #在窗口中渲染一组帧数据，这里只渲染深度帧
            depthFrame = frameSet.depthFrame()
            if depthFrame != None:
                size = depthFrame.dataSize()
                data = depthFrame.data()
                if size != 0:
                    #将帧数据16bit转8bit
                    p = []
                    newData = data.astype( np.uint8 )
                    #将帧数据大小调整为(height,width,1)
                    newData.resize( (height,width,1) )
                    newData.reshape( (height,width,1) )
                    num = 0
                    for m in range(height):
                        for n in range(width):
                            if newData[m][n] == 0:
                                num += 1
                                continue
                            pz = newData[m][n] / camera_factor
                            p.append(((n - camera_cx) * pz / camera_fx,
                                           (m - camera_cy) * pz / camera_fy, pz))

                    header_lines = ["ply",
                                    "format ascii 1.0",
                                    "comment generated by: python",
                                    # "element vertex {}".format(int(len(data))),
                                    "element vertex {}".format(height*width-num),
                                    "property float x",
                                    "property float y",
                                    "property float z",
                                    "end_header"]
                    # convert to string
                    data = '\n'.join(
                        '{} {} {}'.format('%f' % i[0], '%f' % i[1], '%f' % i[2]) for i
                        in p)
                    header = '\n'.join(line for line in header_lines) + '\n'
                    # write file
                    path = "C:/Users/jdy/Documents/GitHub/StandTheGrapefruit/Femto/img/test_Femto.ply"
                    file = open(path, 'w')
                    file.write(header)
                    file.write(data)
                    # for i in p:
                    #     data = '\n'.join(
                    #         '{} {} {} {} {} {}'.format('%.2f' % p[0], '%.2f' % p[1], '%.2f' % p[2]) for p
                    #         in data)
                    #     file.write(i[0])

                    # file.write(data)
                    file.close()

                    #创建窗口
                    cv2.namedWindow( "DepthViewer", cv2.WINDOW_NORMAL )

                    #显示图像
                    cv2.imshow( "DepthViewer", newData )

                    key = cv2.waitKey( 1 )
                    #按 ESC 或 'q' 关闭窗口
                    if key & 0xFF == ord( 'q' ) or key == 27:
                        cv2.destroyAllWindows()
                        break

    pipe.stop()

except ObException as e:
    print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d"
           %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )