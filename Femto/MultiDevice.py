import Context
import Pipeline
import StreamProfile
import Device
from Error import ObException
import cv2
import numpy as np

#函数：打开所有设备的深度流和彩色流
def StartStream( pipes ):
	#创建Config
	config = Pipeline.Config()
	for pipe in pipes:
		#获取深度相机配置列表
		depthProfileList = pipe.getStreamProfileList( Pipeline.PY_SENSOR_DEPTH )
		for  j in range( depthProfileList.count() ):
			depthProfile = depthProfileList.getProfile( j )
			videoProfile = depthProfile.toViedo()
			if  videoProfile.format() == StreamProfile.PY_FORMAT_Y16 and \
				( videoProfile.width() == 640 and videoProfile.height() == 480 ):
				config.enableStream( videoProfile )
				break
		#获取彩色相机配置列表
		colorProfileList = pipe.getStreamProfileList( Pipeline.PY_SENSOR_COLOR )
		for  j in range( colorProfileList.count() ):
			colorProfile = colorProfileList.getProfile( j )
			videoProfile = colorProfile.toViedo()
			if  videoProfile.format() == StreamProfile.PY_FORMAT_MJPG and \
				( videoProfile.width() == 640 and videoProfile.height() == 480 ):
				config.enableStream( videoProfile )
				break		
		pipe.start( config )

try:
	#主函数入口
	pipes = []
	key = -1

	#创建一个Context，用于获取设备列表
	ctx = Context.Context( None )

	#查询已经接入设备的列表
	devList = ctx.queryDeviceList()

	#获取接入设备的数量
	devCount = devList.deviceCount()

	#遍历设备列表并创建pipe
	for i in range( devCount ):
		#获取设备并创建Pipeline
		dev  = devList.getDevice( i )
		pipe = Pipeline.Pipeline( dev )
		pipes.append( pipe )

	#打开所有设备的深度流和彩色流
	StartStream( pipes )

	while True:
		index = 0
		#初始化colorDatas和depthDatas列表，用于存储彩色、深度帧数据
		zeroNp = np.zeros( (480,640,3), dtype = np.uint8 )
		colorDatas = [zeroNp]*len( pipes )
		depthDatas = [zeroNp]*len( pipes )

		for pipe in pipes:
			#以阻塞的方式等待一帧数据，该帧是一个复合帧，里面包含配置里启用的所有流的帧数据，
			#并设置帧的等待超时时间为100ms
			frameSet = pipe.waitForFrames( 100 )
			if frameSet == None:
				continue
			else:
				#在窗口中渲染一组帧数据，这里将渲染彩色帧及深度帧
				colorframe = frameSet.colorFrame()
				depthframe = frameSet.depthFrame()
				if colorframe != None and depthframe != None:
					#获取帧的大小和数据
					colorSize = colorframe.dataSize()
					colorData = colorframe.data()
					depthSize = depthframe.dataSize()
					depthData = depthframe.data()

					if colorSize != 0 and depthSize != 0 :
						#将colorData的MJPG转换成RGB888
						newColorData = cv2.imdecode( colorData, cv2.IMREAD_COLOR )
						#将depthData 16位转换成8位
						newDepthData = depthData.astype( np.uint8 )

						#将newDepthData帧数据(307200,)大小调整为(480, 640, 1)
						newDepthData.resize( (480,640,1) )
						newDepthData.reshape( (480,640,1) )

						#将newDepthData一通道转换成三通道
						newDepthData3d = cv2.cvtColor( newDepthData, cv2.COLOR_GRAY2RGB )

						#列表存储彩色帧及深度帧，用于渲染
						colorDatas[index] = newColorData
						depthDatas[index] = newDepthData3d

						windowName = "MultiDevice dev" + str( index )
						#按垂直顺序堆叠彩色帧及深度帧
						Datas = np.vstack( [colorDatas[index], depthDatas[index]] )
						
						#创建窗口
						cv2.namedWindow( windowName, cv2.WINDOW_NORMAL )

						#显示图像
						cv2.imshow( windowName, Datas )
						
						key = cv2.waitKey( 1 )
			index += 1

		# 按 ESC 或 'q' 关闭窗口
		if key & 0xFF == ord( 'q' ) or key == 27:
			cv2.destroyAllWindows()
			break
			
	for pipe in pipes:
		pipe.stop()

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )