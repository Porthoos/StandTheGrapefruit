import Version
import Context
import Device
import Sensor
from Error import ObException
import sys
import msvcrt

try:
	#打印SDK的版本号，SDK版本号分为主版本号，副版本号和修订版本号
	version= Version.Version()
	print( "SDK version: %d.%d.%d" \
		%( version.getMajor(), version.getMinor(), version.getPatch() ) )

	#创建一个Context，与Pipeline不同，Context是底层API的入口，在开关流等常用操作上
	#使用低级会稍微复杂一些，但是底层API可以提供更多灵活的操作，如获取多个设备，读写
	#设备及相机的属性等
	ctx = Context.Context( None )

	#查询已经接入设备的列表
	devList = ctx.queryDeviceList()

	#获取接入设备的数量
	devCount = devList.deviceCount()
	if devCount == 0:
		print( "Device not found!" )
		sys.exit()

	#创建设备，0表示第一个设备的索引
	dev = devList.getDevice( 0 )

	#获取设备信息
	devInfo = dev.getDeviceInfo()

	#获取设备的名称
	print( "Device name:: %s" %( devInfo.name() ) )

	#获取设备的pid, vid, uid
	print( "Device pid: %#x vid: %#x uid: 0x%s" \
		%( devInfo.pid(), devInfo.vid(), devInfo.uid() ) )

	#通过获取设备的固件版本号
	fwVer = devInfo.firmwareVersion()
	print( "Firmware version: %s" %( fwVer ) )

	#通过获取设备的序列号
	sn = devInfo.serialNumber()
	print( "Serial number: %s" %( sn ) )

	#获取支持的传感器列表
	print("Sensor types: ")

	sensors = dev.getSensorList()
	for i in range( sensors.count() ):
		msensor = sensors.getSensorByIndex( i )
		sensorType = msensor.type()
		if sensorType == Sensor.PY_SENSOR_COLOR :
			print( "\tColor sensor" )
		elif sensorType == Sensor.PY_SENSOR_DEPTH :
			print( "\tDepth sensor" )
		elif sensorType == Sensor.PY_SENSOR_IR :
			print( "\tIR sensor" )
		elif sensorType == Sensor.PY_SENSOR_GYRO :
			print( "\tGyro sensor" )
		elif sensorType == Sensor.PY_SENSOR_ACCEL :
			print( "\tAccel sensor" )
		else:
			print( "\tUNKNOWN" )

	print( "Press ESC to exit! " )
	while True:
		if ord( msvcrt.getch() ) == 27:
			break

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )