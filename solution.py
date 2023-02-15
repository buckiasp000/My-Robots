import numpy as np
import pyrosim.pyrosim as pyrosim
import random as random
import os as os
import time
import constants as c

class SOLUTION:
    def __init__(self, newID):
        self.weights = {}
        self.segments = round(c.maxSegments * random.random()) + 2
        self.sensorNeurons = 0
        self.sensorLinks = self.initialize_sensorLinks() #0 for no sensor, 1 for sensor
        self.myID = newID
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        
    def initialize_weights(self,x,y):
        return (np.random.rand(x,y) * 2) - 1
    
    def initialize_sensorLinks(self):
        temp = []
        for i in range(self.segments):
            if random.random() < .5:
                temp.append(0)
            else:
                temp.append(1)
        return temp
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI +" " + str(self.myID))# + " 2&>1 &")
    
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
        if(self.sensorNeurons > 0):
            row = random.randint(0,self.sensorNeurons - 1)
            column = random.randint(0,self.segments - 2)
            self.weights[row][column] = (random.random() * 2) - 1
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = -4
        y = -4
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height], colorName="Green", rgb="") #move all this to generate body?
        pyrosim.End()
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        lastYVal = 0
        jointRotations = ["1 0 0", "0 1 0", "0 0 1"]
        currentLink = 0
        for i in range(self.segments):
            length = c.maxLength * random.random()
            width = c.maxWidth * random.random()
            height = c.maxHeight * random.random()
            lastWidth = 0
            print(self.sensorLinks)
            if self.sensorLinks[currentLink] == 1:
                color = "Green"
            else:
                color = "Blue"
            
            if (i == 0):
                pyrosim.Send_Cube(name= "0", pos=[0,0,3] , size=[length,width,height],colorName = color,rgb= "")
                pyrosim.Send_Joint( name = str(i) + "_" + str(i + 1), parent= str(i) , child = str(i+1) , type = "revolute", position = [0,width/2,3], jointAxis = jointRotations[random.randint(0,2)])
                #print("made cube 0")
            elif (i<self.segments - 1):
                pyrosim.Send_Cube(name= str(i), pos=[0, width/2,0] , size=[length,width,height],colorName= color,rgb= "")
                pyrosim.Send_Joint( name = str(i) + "_" + str(i + 1), parent= str(i) , child = str(i +1) , type = "revolute", position = [0,width,0], jointAxis = jointRotations[random.randint(0,2)])
                #print("made more cube: " + str(i))
            else:
                pyrosim.Send_Cube(name= str(i), pos=[0, width/2,0] , size=[length,width,height], colorName= color,rgb="")
            currentLink = currentLink + 1
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
      #  print("making brain")
        neuronNum = 0
        self.sensorNeurons = 0
        numMotors = self.segments -1
        for i in range(self.segments):
            if self.sensorLinks[i] == 1:    
                pyrosim.Send_Sensor_Neuron(name = neuronNum, linkName = str(i))
                neuronNum = neuronNum + 1
                self.sensorNeurons = self.sensorNeurons + 1
               # print("sensor:" + str(self.sensorNeurons) + " links: " + str(i))
       # print(str(neuronNum )+ " total")
       # print(str(self.sensorNeurons) + " sensors")
       # print(str(numMotors) + "motors")
        for i in range(self.segments):
            if i != 0:
                pyrosim.Send_Motor_Neuron( name = neuronNum , jointName = str(i-1) + "_" + str(i))
                neuronNum = neuronNum + 1
      #  print(self.sensorNeurons)
      #  print(numMotors)
        self.weights = self.initialize_weights(self.sensorNeurons,numMotors)
       # print(self.weights)
        
        if(self.sensorNeurons > 0):
            for currentRow in range(self.sensorNeurons): 
               for currentColumn in range(numMotors):
                    #print("row: " + str(currentRow) + " col: " + str(currentColumn))
                    pyrosim.Send_Synapse( sourceNeuronName =  currentRow, targetNeuronName = currentColumn + self.sensorNeurons , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()
        
        
    def Set_ID(self, newID):
        self.myID = newID
    
    