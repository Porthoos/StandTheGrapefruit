import Pipeline
import StreamProfile
from Error import ObException
import cv2

try:
	#创建一个Pipeline，Pipeline是整个高级API的入口，通过Pipeline可以很容易的打开和关闭
	#多种类型的流并获取一组帧数据
	pipe = Pipeline.Pipeline( None )

	#获取彩色相机的所有流配置，包括流的分辨率，帧率，以及帧的格式
	profiles = pipe.getStreamProfileList( Pipeline.PY_SENSOR_COLOR )

	#通过遍历彩色流的配置来获取要使用的帧格式，这里将使用MJPG格式来打开流
	count = profiles.count()
	for i in range( count ):
		profile = profiles.getProfile( i )
		videoProfile = profile.toViedo()
		if videoProfile.format() == StreamProfile.PY_FORMAT_MJPG:
			colorProfile = videoProfile
			break

	#通过创建Config来配置Pipeline要启用或者禁用哪些流，这里将启用彩色流
	config = Pipeline.Config()
	config.enableStream( colorProfile )

	#启动在Config中配置的流，如果不传参数，将启动默认配置启动流
	pipe.start( config )

	width = colorProfile.width()
	height = colorProfile.height()

	while True:
		#以阻塞的方式等待一帧数据，该帧是一个复合帧，里面包含配置里启用的所有流的帧数据，
		#并设置帧的等待超时时间为100ms
		frameSet = pipe.waitForFrames( 100 )
		if frameSet == None:
			continue
		else:
			#在窗口中渲染一组帧数据，这里只渲染彩色帧
			colorFrame = frameSet.colorFrame()
			if colorFrame != None:
				#获取帧的大小和数据
				size = colorFrame.dataSize()
				data = colorFrame.data()

				if size != 0:
					#将MJPG转换成RGB888
					newData = cv2.imdecode( data, cv2.IMREAD_COLOR )
					#创建窗口
					cv2.namedWindow( "ColorViewer", cv2.WINDOW_NORMAL )

					#显示图像
					cv2.imshow( "ColorViewer", newData )

					key = cv2.waitKey( 1 )
					# 按 ESC 或 'q' 关闭窗口
					if key & 0xFF == ord( 'q' ) or key == 27:
						cv2.destroyAllWindows()
						break

	pipe.stop()

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )