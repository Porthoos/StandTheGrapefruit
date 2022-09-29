import Pipeline
import StreamProfile
from Error import ObException
import cv2
import numpy as np

#函数：将帧数据16bit转8bit
def mapUint16ToUint8( img, lowerBound = None, upperBound = None ):
	if lowerBound == None:
		lowerBound = np.min( img )
	if upperBound == None:
		upperBound = np.max( img )
	lut = np.concatenate([
		np.zeros( lowerBound, dtype=np.uint16 ),
		np.linspace( 0, 255, upperBound - lowerBound ).astype( np.uint16 ),
		np.ones( 2**16 - upperBound, dtype = np.uint16 ) * 255
	])
	return lut[ img ].astype( np.uint8 )

try:
	#创建一个Pipeline，Pipeline是整个高级API的入口，通过Pipeline可以很容易的打开和关闭
	#多种类型的流并获取一组帧数据
	pipe = Pipeline.Pipeline( None )

	#获取红外相机的所有流配置，包括流的分辨率，帧率，以及帧的格式
	profiles = pipe.getStreamProfileList( Pipeline.PY_SENSOR_IR)

	#通过遍历红外流的配置来获取要使用的帧格式，这里将使用YUYV格式来打开流
	count = profiles.count( )
	for i in range(count):
		profile = profiles.getProfile( i )
		videoProfile = profile.toViedo()
		if videoProfile.format() == StreamProfile.PY_FORMAT_YUYV or videoProfile.format() == StreamProfile.PY_FORMAT_Y16:
			irProfle = videoProfile
			break

	#通过创建Config来配置Pipeline要启用或者禁用哪些流，这里将启用红外流
	config = Pipeline.Config()
	config.enableStream( irProfle )

	#启动在Config中配置的流，如果不传参数，将启动默认配置启动流
	pipe.start( config )

	width = irProfle.width()
	height = irProfle.height()

	while True:
		#以阻塞的方式等待一帧数据，该帧是一个复合帧，里面包含配置里启用的所有流的帧数据，
		#并设置帧的等待超时时间为100ms
		frameSet = pipe.waitForFrames( 100 )
		if frameSet == None:
			continue
		else:
			#在窗口中渲染一组帧数据，这里只渲染红外帧
			irFrame = frameSet.irFrame()
			if irFrame != None:
				size = irFrame.dataSize()
				data = irFrame.data()

				if size != 0:
					#将帧数据16bit转8bit
					newData = mapUint16ToUint8( data )

					#将帧数据大小调整为(height,width,1)
					newData.resize( (height,width,1) )
					newData.reshape( (height,width,1) )
					#创建窗口
					cv2.namedWindow( "InfraredViewer", cv2.WINDOW_NORMAL )

					#显示图像
					cv2.imshow( "InfraredViewer", newData )

					key = cv2.waitKey( 1 )
					#按 ESC 或 'q' 关闭窗口
					if key & 0xFF == ord( 'q' ) or key == 27:
						cv2.destroyAllWindows()
						break

	pipe.stop()

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )