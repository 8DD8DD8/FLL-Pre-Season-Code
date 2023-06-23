from pybricks.hubs import *
from pybricks.iodevices import *
from pybricks.parameters import *
from pybricks.pupdevices import *
from pybricks.robotics import *
from pybricks.tools import *
try:
    hub=CityHub()
except:
    try:
        hub=MoveHub()
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