import sys
sys.path.append('lib/')

from device_listener import DeviceListener
from pose_type import PoseType
import pinDriver as pd

class PrintPoseListener(DeviceListener):
    def __init__(self) :
        pd.init_drivers()
    def on_pose(self, pose):
        pose_type = PoseType(pose)
	self.makeMovement(pose_type.name)

    def makeMovement(self , cmd):
        if ( cmd == "REST" ):
            pd.hand_rest()
        elif ( cmd == "FINGERS_SPREAD" ):
            set_angle(90)
	    sleep(3)
            pd.hand_open()
        elif ( cmd == "FIST" ):
            set_angle(50)
	    sleep(3)
            pd.hand_close()
	elif ( cmd == "WAVE_OUT" ):
            set_angle(90)
            pd.thump_open()
	elif ( cmd == "WAVE_IN" ):
            set_angle(0)
            pd.hold_pen()
	else:
	    pd.hand_rest()
    def emgData(self,Data):
        pass



















		
   
