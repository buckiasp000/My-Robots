import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class MOTOR:
    def __init__(self,joint):
        self.jointName = joint
    
    
    def SetValue(self,robot,desiredAngle, timeStep):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForceBL)
       # if(timeStep == c.iterations - 1):
            #self.SaveValues()