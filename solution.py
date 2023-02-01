import numpy as np
import pyrosim.pyrosim as pyrosim
import random as random
import os as os

class SOLUTION:
    def __init__(self):
        self.weights = self.initialize_weights()
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        
    def initialize_weights(self):
        return (np.random.rand(3,2) * 2) - 1
    
    def Evaluate(self, directOrGUI):
        
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system('python3 simulate.py ' + directOrGUI)
        
        f = open("fitness.txt", "r")
        fit = f.read()
        self.fitness =  float(fit)
        f.close()
    
    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
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
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height])
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        
        #sensorNeurons = [0, 1, 2]
       # motorNeurons = [3, 4]
        for currentRow in range(3): 
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName =  currentRow, targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()
    
    