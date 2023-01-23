from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time as t

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0, c.gravity)
        self.robotId = p.loadURDF("body.urdf")
        self.world = WORLD()
        self.robot = ROBOT(self.robotId)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        
        
    def Run(self):
        for i in range(c.iterations):
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            #print(i)
            t.sleep(c.timeToSleep)
    def __del__(self):
        p.disconnect()
        