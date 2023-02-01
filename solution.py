import numpy as np
import pyrosim.pyrosim as pyrosim
import random as random
import os as os
import time
import constants as c

class SOLUTION:
    def __init__(self, newID):
        self.weights = self.initialize_weights()
        self.myID = newID
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        
    def initialize_weights(self):
        return (np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2) - 1
    
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI +" " + str(self.myID) + " 2&>1 &")
    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) +".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
            
        f = open(fitnessFileName, "r")
        fit = f.read()
        self.fitness =  float(fit)
        f.close()
        os.system("rm " + fitnessFileName)
        print(self.fitness)
    
    
    def Evaluate(self, directOrGUI):
        
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system("python3 simulate.py " + directOrGUI +" " + str(self.myID) + " &")
        
        fitnessFileName = "fitness" + str(self.myID) +".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
            
        f = open("fitness" + str(self.myID) +".txt", "r")
        fit = f.read()
        self.fitness =  float(fit)
        f.close()
       
    
    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons - 1)
        column = random.randint(0,c.numMotorNeurons - 1)
        self.weights[row][column] = (random.random() * 2) - 1
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = -4
        y = -4
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height]) #move all this to generate body?
        pyrosim.End()
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
        #Upper Legs
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0] , size=[1,.2,.2])
        #Lower Legs
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        
        #sensors
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        
        #upperlegs
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        
        #lowerlegs
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightLowerLeg")
        
        
        #motors
        #upperlegs
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        #lowerlegs
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")


        for currentRow in range(c.numSensorNeurons): 
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName =  currentRow, targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()
        
    def Set_ID(self, newID):
        self.myID = newID
    
    