import Pipeline
import StreamProfile
import Device
from Error import ObException
import cv2
import numpy as np


D = 68
d = 100
F = 70
f = 102
S = 83
s = 115
add = 43
reduce = 45
FEMTO  =0x0635

sync  = True
hd2c  = True
sd2c  = False
alpha = 0.5
keyRecord  = -1

frameSet = None
colorFrame = None
depthFrame = None

try:
	#创建一个Pipeline，Pipeline是整个高级API的入口，通过Pipeline可以很容易的打开和关闭
	#多种类型的流并获取一组帧数据
	pipe = Pipeline.Pipeline( None )

	#获取彩色相机的所有流配置，包括流的分辨率，帧率，以及帧的格式
	colorProfiles = pipe.getStreamProfileList( Pipeline.PY_SENSOR_COLOR )
	#通过遍历彩色流的配置来获取要使用的帧格式，这里将使用MJPG格式来打开流
	count = colorProfiles.count()
	for i in range( count ):
		profile = colorProfiles.getProfile( i )
		videoProfile = profile.toViedo()
		if videoProfile.format() == StreamProfile.PY_FORMAT_MJPG and videoProfile.width() == 640 and videoProfile.height() == 480:
			colorProfile = videoProfile
			break

	#获取深度相机的所有流配置，包括流的分辨率，帧率，以及帧的格式
	depthProfiles = pipe.getStreamProfileList( Pipeline.PY_SENSOR_DEPTH )
	#通过遍历深度流的配置来获取要使用的帧格式，这里将使用YUYV格式来打开流
	count = depthProfiles.count( )
	for i in range( count ):
		profile = depthProfiles.getProfile( i )
		videoProfile = profile.toViedo()
		if ( videoProfile.format() == StreamProfile.PY_FORMAT_YUYV or videoProfile.format() == StreamProfile.PY_FORMAT_Y16 ) and \
			( videoProfile.width() == 640 and videoProfile.height() == 480 ):
			depthProfle = videoProfile
			break

	#通过创建Config来配置Pipeline要启用或者禁用哪些流，这里将启用彩色流
	config = Pipeline.Config()
	config.enableStream( colorProfile )
	config.enableStream( depthProfle )


	#要控制彩色流和深度流的对齐，可以通过Pipeline中获取当前正在使用的设备，
	#然后通过设置设备的属性开进行控制
	mdevice = pipe.getDevice()
	pid = mdevice.getDeviceInfo().pid()
	if mdevice.isPropertySupported( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_HARDWARE_BOOL ):
		mdevice.setBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_HARDWARE_BOOL, hd2c )
	elif mdevice.isPropertySupported( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_SOFTWARE_BOOL ) :
		mdevice.setBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_SOFTWARE_BOOL, sd2c )

	#启动在Config中配置的流，如果不传参数，将启动默认配置启动流
	pipe.start( config )

	width = colorProfile.width()
	height = colorProfile.height()

	while True:
		frameSet = None
		colorFrame = None
		depthFrame = None
		key = cv2.waitKey(1)
		#按+键增加alpha
		if keyRecord != key and key == add :
			alpha += 0.01
			if alpha >= 1.0 :
				alpha = 1.0

		#按-键减少alpha
		if keyRecord != key and key == reduce :
			alpha -= 0.01
			if alpha <= 0.0 :
				alpha = 0.0
		
		#按D键开关硬件D2C
		if keyRecord != key and ( key == D or key == d ) :
			try:
				if pid == FEMTO:
					#设置硬件D2C，首先获取硬件D2C的值，取反后再进行设置，需要注意的是对然这里将
					sd2c = mdevice.getBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_SOFTWARE_BOOL )
					sd2c = bool( 1 - sd2c )
					mdevice.setBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_SOFTWARE_BOOL, sd2c )
				else:
					pipe.stop()
					hd2c = mdevice.getBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_HARDWARE_BOOL )
					hd2c = bool( 1 - hd2c )
					mdevice.setBoolProperty( Device.PY_DEVICE_PROPERTY_DEPTH_ALIGN_HARDWARE_BOOL, hd2c )
					pipe.start( config )
			except ObException as e:
				print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )
				print( "Property not support" )
			finally:
				pass

		#按F键开关同步
		if keyRecord != key and ( key == F or key == f ) :
			sync = bool( 1 - sync )
			if sync :
				#开启同步功能
				pipe.enableFrameSync()
			else :
				#关闭同步功能
				pipe.disableFrameSync()
		
		keyRecord = key

		#以阻塞的方式等待一帧数据，该帧是一个复合帧，里面包含配置里启用的所有流的帧数据，
		#并设置帧的等待超时时间为100ms
		frameSet = pipe.waitForFrames( 100 )

		if frameSet == None:
			continue
		else:
			#在窗口中渲染一组帧数据，这里将渲染彩色帧及深度帧，将彩色帧及深度帧叠加显示
			colorFrame = frameSet.colorFrame()
			depthFrame = frameSet.depthFrame()
			if colorFrame != None and depthFrame != None:
				#获取帧的大小和数据
				colorSize = colorFrame.dataSize()
				colorData = colorFrame.data()
				depthSize = depthFrame.dataSize()
				depthData = depthFrame.data()
				
				if colorSize !=0 and depthSize !=0 :
					#将colorData的MJPG转换成RGB888
					newColorData = cv2.imdecode( colorData, cv2.IMREAD_COLOR )
					#将depthData 16位转换成8位
					newDepthData = depthData.astype( np.uint8 )

					#将newDepthData帧数据大小调整为(height,width,1)
					newDepthData.resize( (height,width,1) )
					newDepthData.reshape( (height,width,1) )

					#将newDepthData一通道转换成三通道
					newDepthData3d = cv2.cvtColor( newDepthData, cv2.COLOR_GRAY2RGB )

					#将彩色帧及深度帧叠加显示
					datas = cv2.addWeighted( newColorData, (1 - alpha), newDepthData3d, alpha, 0 )

					#创建窗口
					cv2.namedWindow( "SyncAlignViewer", cv2.WINDOW_NORMAL )


					#显示图像
					cv2.imshow( "SyncAlignViewer", datas )

					# 按 ESC 或 'q' 关闭窗口
					if key & 0xFF == ord( 'q' ) or key == 27:
						cv2.destroyAllWindows()
						break

	pipe.stop()

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )