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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
        #Upper Legs
        pyrosim.Send_Joint( name = "Torso_FrontLeg0" , parent= "Torso" , child = "FrontLeg0" , type = "revolute", position = [0,.5,1], jointAxis = "-1 0 0")
        pyrosim.Send_Cube(name="FrontLeg0", pos=[0,.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg0" , parent= "Torso" , child = "BackLeg0" , type = "revolute", position = [0,-.5,1], jointAxis = "-1 0 0")
        pyrosim.Send_Cube(name="BackLeg0", pos=[0,-.5,0] , size=[.2,1,.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg0" , parent= "Torso" , child = "LeftLeg0" , type = "revolute", position = [-.5,0,1], jointAxis = "0 -1 0")
        pyrosim.Send_Cube(name="LeftLeg0", pos=[-.5, 0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg0" , parent= "Torso" , child = "RightLeg0" , type = "revolute", position = [.5,0,1], jointAxis = "0 -1 0")
        pyrosim.Send_Cube(name="RightLeg0", pos=[.5,0,0] , size=[1,.2,.2])
        
        #Lower Legs
        if c.numSegments > 1:
            for i in range(1,c.numSegments):
                pyrosim.Send_Joint( name = ("FrontLeg" + str(i-1) + "_FrontLeg" + str(i)) , parent= ("FrontLeg" + str(i-1)), child = ("FrontLeg" + str(i)) , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
                pyrosim.Send_Cube(name="FrontLeg" + str(i), pos=[0,.5,0] , size=[.2,1,.2])
                pyrosim.Send_Joint( name = "BackLeg" + str(i-1) + "_BackLeg" + str(i), parent= "BackLeg" + str(i-1) , child = "BackLeg" + str(i), type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
                pyrosim.Send_Cube(name="BackLeg" + str(i), pos=[0,-.5,0] , size=[.2,1,.2])
                pyrosim.Send_Joint( name = "LeftLeg" + str(i-1) + "_LeftLeg" + str(i), parent= "LeftLeg" + str(i-1), child = "LeftLeg" + str(i), type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
                pyrosim.Send_Cube(name="LeftLeg" + str(i), pos=[-.5, 0 ,0] , size=[1,.2,.2])
                pyrosim.Send_Joint( name = "RightLeg" + str(i-1) + "_RightLeg" + str(i), parent= "RightLeg" + str(i-1), child = "RightLeg" + str(i) , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
                pyrosim.Send_Cube(name="RightLeg" + str(i), pos=[.5,0, 0] , size=[1,.2,.2])
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        #sensors
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        
        #legs
        
        temp = 0
        for k in range(0,c.numSegments):
            pyrosim.Send_Sensor_Neuron(name = temp + 1, linkName = "BackLeg" + str(k))
            pyrosim.Send_Sensor_Neuron(name = temp + 2, linkName = "FrontLeg" + str(k))
            pyrosim.Send_Sensor_Neuron(name = temp + 3, linkName = "LeftLeg" + str(k))
            pyrosim.Send_Sensor_Neuron(name = temp + 4, linkName = "RightLeg" + str(k))
            temp = temp + 4
            
        
        #motors torso
        if c.numSegments > 0:
            pyrosim.Send_Motor_Neuron( name = temp + 1, jointName = "Torso_BackLeg0")
            pyrosim.Send_Motor_Neuron( name = temp + 2, jointName = "Torso_FrontLeg0")
            pyrosim.Send_Motor_Neuron( name = temp + 3, jointName = "Torso_LeftLeg0")
            pyrosim.Send_Motor_Neuron( name = temp + 4, jointName = "Torso_RightLeg0")
            temp = temp + 4
        
        #legs
        if c.numSegments > 1:
            for j in range(0,c.numSegments-1):
                pyrosim.Send_Motor_Neuron( name = temp + 1, jointName = "BackLeg" + str(j) + "_BackLeg" + str(j + 1))
                pyrosim.Send_Motor_Neuron( name = temp + 2, jointName = "FrontLeg" + str(j) + "_FrontLeg" + str(j + 1))
                pyrosim.Send_Motor_Neuron( name = temp + 3, jointName = "LeftLeg" + str(j) + "_LeftLeg" + str(j + 1))
                pyrosim.Send_Motor_Neuron( name = temp + 4, jointName = "RightLeg" + str(j) + "_RightLeg" + str(j + 1))
                temp = temp + 4
        
        #legs
        for currentRow in range(c.numSensorNeurons): 
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName =  currentRow, targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
        
    def Set_ID(self, newID):
        self.myID = newID
    
    