from pybricks.hubs import *
from pybricks.parameters import *
from pybricks.pupdevices import *
from pybricks.robotics import *
from pybricks.tools import *
try:
    hub=CityHub()
except:
    try:
        hub=MoveHub()
        motor_left=Motor(Port.B, Direction.COUNTERCLOCKWISE)
        motor_right=Motor(Port.A, Direction.CLOCKWISE)
        drive_base=DriveBase(motor_left, motor_right, 50, 50)
        try:
            motor_external=Motor(Port.C)
            color_distance_sensor=ColorDistanceSensor(Port.D)
        except:
            pass
    except:
        try:
            hub=PrimeHub()
        except:
            try:
                hub=TechnicHub()
            except:
                try:
                    hub=InventorHub()
                except:
                    try:
                        hub=EssentialHub()
                    except:
                        hub=None