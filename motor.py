import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class MOTOR:
    def __init__(self,joint):
        self.jointName = joint
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        print(self.jointName)
        if self.jointName == b'Torso_FrontLeg':
            self.amplitude = c.amplitudeBL
            self.frequency = c.frequencyBL
            self.phaseOffset = c.phaseOffsetBL
        else:
            self.amplitude = c.amplitudeFL
            self.frequency = c.frequencyFL
            self.phaseOffset = c.phaseOffsetFL
        self.values = self.amplitude * np.sin(self.frequency * np.linspace(-np.pi, np.pi, c.iterations) + np.ones(c.iterations) * self.phaseOffset)
    
    def SetValue(self,robot,timeStep):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.values[timeStep], maxForce = c.maxForceBL)
        if(timeStep == c.iterations - 1):
            self.SaveValues()
        
    def SaveValues(self):   
        np.save("data/motorValuesTwo.npy", self.values)