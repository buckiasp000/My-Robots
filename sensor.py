import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class SENSOR:
    def __init__(self, link):
        self.linkName = link
        self.Prepare_To_Sense()
    def GetValue(self,timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if(timeStep == c.iterations - 1):
            self.SaveValues()
            
    def Prepare_To_Sense(self):
        self.values = np.zeros(c.iterations)
        
    def Save_Values(self):
        np.save("data/SensorValuesTwo.npy", self.values)