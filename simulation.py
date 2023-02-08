from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time as t

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if(directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        self.solutionID = solutionID
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0, c.gravity)
        self.robotId = p.loadURDF("body.urdf")
        self.world = WORLD()
        self.robot = ROBOT(self.robotId, self.solutionID)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        self.directOrGUI = directOrGUI
        
        
    def Run(self):
        for i in range(c.iterations): 
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            self.robot.CalculateFitness(i)
            if(self.directOrGUI != "DIRECT"):
                t.sleep(c.timeToSleep)
    def __del__(self):
        p.disconnect()
        
    def Get_Fitness(self):
        self.robot.Get_Fitness()