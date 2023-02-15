import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class SENSOR:
    def __init__(self, link):
        self.linkName = link
        self.Prepare_To_Sense()
    def GetValue(self,timeStep):
        self.values[timeStep-1] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            
    def Prepare_To_Sense(self):
        self.values = np.zeros(c.iterations)
        
   #def Save_Values(self):
       # np.save("data/SensorValuesTwo.npy", self.values)