import Context
import Device
import Sensor
from Error import ObException
import re



#判断输入的字符串是否是合理范围的整数或bool [min,max)
def isCorrectInt( num, min, max ):
	value = re.compile( r'^[-+]?[0-9]+$' )
	result = value.match( num )
	if result:
		if int( num ) < min or int( num ) >= max:
			return False
		else:
			return True
	else:
		return False

#判断输入的字符串是否是合理范围的Float [min,max]
def isCorrectFloat( num, min, max ):
	value = re.compile( r'^[-+]?[0-9]+\.[0-9]+$' )
	result = value.match( num )
	if result:
		if float( num ) < min or float( num ) > max:
			return False
		else:
			return True
	else:
		return False

#选择一个设备，这里会打印设备的名称、pid、vid、uid，选择后会创建相应的设备对象
def selectDevice( deviceList ) :
	devCount = deviceList.deviceCount()
	print( "Device list: " )
	for i in range( devCount ):
		print( "%d. name:%s, vid: %#x, pid: %#x, uid: 0x%s" \
			%( i, deviceList.name( i ), deviceList.vid( i ), deviceList.pid( i ), deviceList.uid( i ) ) )

	inputInfo = input( "Select a device: " )
	while isCorrectInt( inputInfo, 0, devCount ) == False:
		inputInfo = input( "Your select is out of range, please reselect: " )
	devIndex = int( inputInfo )
	print( devIndex )
	return deviceList.getDevice( devIndex )

def selectSensor( device ):
	sensors = device.getSensorList()
	print( "Sensor list: " )
	for i in range( sensors.count() ):
		if sensors.type( i ) == Sensor.PY_SENSOR_COLOR:
			sensorType = "Color Sensor"
		elif sensors.type( i ) == Sensor.PY_SENSOR_DEPTH:
			sensorType = "Depth Sensor"
		elif sensors.type( i ) == Sensor.PY_SENSOR_IR:
			sensorType = "IR Sensor"
		else:
			continue
		print( "%d. sensor type: %s" %( i, sensorType ) )

	inputInfo = input( "Select a sensor: " )
	while isCorrectInt( inputInfo, 0, sensors.count() ) == False:
		inputInfo = input( "Your select is out of range, please reselect: " )
	sensorIndex = int( inputInfo )

	return sensors.getSensorByIndex( sensorIndex )
	
#选择带操作的属性，这里会显示sensor所支持的所有属性
def selectPropertyItem( sensorOrDevice ):
	size = sensorOrDevice.getSupportedPropertyCount()
	if size == 0:
		print( "No supported property !" )
		propertyItem = {}
		return propertyItem

	for i in range( size ):
		propertyItem = sensorOrDevice.getSupportedProperty( i )
		if propertyItem.get( "type" ) != Sensor.PY_STRUCT_PROPERTY :
			print( "%d. property: %s" %( i, propertyItem.get( "name" ) ) )
			
	inputInfo = input( "Select a property item: " )
	while isCorrectInt( inputInfo, 0, size ) == False:
		inputInfo = input( "Your select is out of range, please reselect: " )
	propertyIndex = int( inputInfo )
	print( propertyIndex )
	ret = sensorOrDevice.getSupportedProperty( propertyIndex )
	return ret

#操作每个属性，支持的操作有set/get
def controlProperty( sensorOrDevice,  propertyItem ):
	isControlProperty = True
	while isControlProperty == True:
		print( "Actions:\n\
			0. Set property\n\
			1. Get property\n\
			Select an action: " )
		inputInfo = input()
		while isCorrectInt( inputInfo, 0, 2 ) == False:
			inputInfo = input( "Your select is out of range, please reselect: " )
		action = int( inputInfo )
		try:
			if action == 0:
				if propertyItem.get( "type" ) == Sensor.PY_BOOL_PROPERTY:
					inputInfo = input( "Input a bool value(0/1):" )
					while isCorrectInt( inputInfo, 0, 2 ) == False:
						inputInfo = input( "Your select is out of range, please reselect: " )
					boolValue = int( inputInfo )
					sensorOrDevice.setBoolProperty( propertyItem.get( "id" ), boolValue )
				elif propertyItem.get( "type" ) == Sensor.PY_INT_PROPERTY:
					intRange = sensorOrDevice.getIntPropertyRange( propertyItem.get( "id" ) )
					print( "Input a int value([ %d - %d ],step:%d )" %( intRange.get( "min" ), intRange.get( "max" ), intRange.get( "step" ) ) )
					inputInfo = input()
					while isCorrectInt( inputInfo, intRange.get( "min" ), intRange.get( "max" )+1 ) == False:
						inputInfo = input( "Your select is out of range, please reselect: " )
					intValue = int( inputInfo )
					sensorOrDevice.setIntProperty( propertyItem.get( "id" ), intValue )
				elif propertyItem.get( "type" ) == Sensor.PY_FLOAT_PROPERTY:
					floatRange = sensorOrDevice.getFloatPropertyRange( propertyItem.get( "id" ) )
					print( "Input a float value([ %f - %f ],step:%f )" %( floatRange.get( "min" ), floatRange.get( "max" ), floatRange.get( "step" ) ) )
					inputInfo = input()
					while isCorrectFloat( inputInfo, floatRange.get( "min" ), floatRange.get( "max" ) ) == False:
						inputInfo = input( "Your select is out of range, please reselect: " )
					floatValue = float( inputInfo )
					sensorOrDevice.setFloatProperty( propertyItem.get( "id" ), floatValue )
				else:
					print( "UNKNOW PROPERTY" )
			else :
				if propertyItem.get( "type" ) == Sensor.PY_BOOL_PROPERTY:
					boolRet = sensorOrDevice.getBoolProperty( propertyItem.get( "id" ) )
					print( "value:%d" %( boolRet ) )
				elif propertyItem.get( "type" ) == Sensor.PY_INT_PROPERTY:
					intRet = sensorOrDevice.getIntProperty( propertyItem.get( "id" ) )
					print( "value:%d" %( intRet ) )
				elif propertyItem.get( "type" ) == Sensor.PY_FLOAT_PROPERTY:
					floatRet = sensorOrDevice.getFloatProperty( propertyItem.get( "id" ) )
					print( "value:%f" %( floatRet ) )
				else:
					print( "UNKNOW PROPERTY" )
		except ObException as e:
			print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )
			print( "Set/Get property %s failed !" %( propertyItem.get( "name" ) ) )
		finally:
			pass
		isControlProperty = continueOrBack( "control property" )

def continueOrBack( msg ):
	print( "Continue %s again[y/n]: " %( msg ) )
	choise = input()
	
	if choise == 'n' or choise == 'N':
		print( "choise is n!" )
		return False
	return True

#选择设备的property进行操作还是sensor进行操作
def selectDevicePropertyOrSensor( device ):
	print( "Options: \n\
		0. Select device property\n\
		1. select sensor\n\
		Please select your option:" )
	
	inputInfo = input( "Select a property item: " )
	while isCorrectInt( inputInfo, 0, 2 ) == False:
		inputInfo = input( "Your selection is out of range, please reselect: " )
	option = int( inputInfo )
	
	if option == 0:
		isSelectProperty = True
		while isSelectProperty == True:
			propertyItem = selectPropertyItem( device ) 
			if propertyItem.get( "name" ) != None:
				controlProperty( device, propertyItem )
				
			isSelectProperty = continueOrBack( "select property" )
	else:
		isSelectSensor = True
		while isSelectSensor == True:
			mSensor = selectSensor( device )
			
			isSelectProperty = True
			while isSelectProperty == True:
				#选择一个属性进行操作
				propertyItem = selectPropertyItem( mSensor ) 

				#对对应的属性进行具体的操作
				if propertyItem.get( "name" ) != None :
					controlProperty( mSensor, propertyItem )

				isSelectProperty = continueOrBack( "select property" )
				
			isSelectSensor = continueOrBack( "select sensor" )
try:
	#main
	#创建一个Context，与Pipeline不同，Context是底层API的入口，在开关流等常用操作上
	#使用低级会稍微复杂一些，但是底层API可以提供更多灵活的操作，如获取多个设备，读写
	#设备及相机的属性等
	ctx = Context.Context( None )

	#查询已经接入设备的列表
	deviceList = ctx.queryDeviceList();

	isSelectDevice = True
	while isSelectDevice == True:
		#选择一个设备进行操作
		device = selectDevice( deviceList )

		isSelectDevicePropertyOrSensor = True
		while isSelectDevicePropertyOrSensor == True:
			#选择设备属性或者是sensor进行操作
			selectDevicePropertyOrSensor( device )
			isSelectDevicePropertyOrSensor = continueOrBack( "select device property or sensor" )

		isSelectDevice = continueOrBack( "select device" )

except ObException as e:
	print( "function: %s\nargs: %s\nmessage: %s\ntype: %d\nstatus: %d" %( e.getName(), e.getArgs(), e.getMessage(), e.getExceptionType(), e.getStatus() ) )