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
            try:
                motor_left=Motor(Port.E, Direction.COUNTERCLOCKWISE)
                motor_right=Motor(Port.A, Direction.CLOCKWISE)
                drive_base=DriveBase(motor_left, motor_right, 56, 113)
                color_sensor_left=ColorSensor(Port.F)
                color_sensor_right=ColorSensor(Port.B)
                #alias names from old PortMap for compatibility
                MotorLeft=motor_left
                MotorRight=motor_right
                driveBase=drive_base
                colorSensorLeft=color_sensor_left
                colorSensorRight=color_sensor_right
            except:
                pass
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