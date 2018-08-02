from utilities import *

class DeviceListener(object):
    def handle_data(self, data):
        if data.cls != 4 and data.command != 5:
	    return
	connection, attribute, data_type = unpack('BHB', data.payload[:4])
        payload = data.payload[5:]
        if attribute == 39:
            temp = unpack('8h', payload[:-1])
            self.emgData(temp)
	elif attribute == 0x23:
            print "her"
            data_type, value, address, x, y, z= unpack('6B', payload)
            print data_type
            if data_type == 3:
                self.on_pose(value )

    def on_pose(self, pose ):
        pass
    def emgData(self,Data):
        pass
