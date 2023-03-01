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
        self.sensorLinks = self.initialize_sensorLinks() #0 for no sensor, 1 for sensor
        self.initialize_sensorNeurons()
        self.directionLinks = self.initialize_directionLinks()
        self.myID = newID
        self.weights = self.initialize_weights(self.sensorNeurons, self.segments-1)
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        
    def initialize_weights(self,x,y):
        return (np.random.rand(x,y) * 2) - 1
    
    def append_weights(self):
        x = [np.random.rand(self.segments-1)]
        return np.append(self.weights, x, 1)
    
    def remove_weights(self):
        return np.delete(self.weights,len(self.weights)-1, 1)
        
    def initialize_sensorLinks(self):
        temp = []
        for i in range(self.segments):
            if random.random() < .5:
                temp.append(0)
            else:
                temp.append(1)
        return temp
    
    def initialize_sensorNeurons(self):
        self.sensorNeurons = 0
        for i in range(self.segments):
            if self.sensorLinks[i] == 1:    
                self.sensorNeurons = self.sensorNeurons + 1
    
    def initialize_directionLinks(self):
        temp = []
        for i in range(self.segments):
            f = random.random()
            if f < .33:
                temp.append(1)
            elif f < .66:
                temp.append(2)
            else:
                temp.append(3)
        return temp
    
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI +" " + str(self.myID)+ " 2&>1 &")
    
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
        
       # print("beginning")
       # print(self.weights)
        #mutate direction of one segment
        directionLinksIndex = random.randint(0,len(self.directionLinks) - 1)
        directionLinksRandomDirection = random.randint(1,3)
        self.directionLinks[directionLinksIndex] = directionLinksRandomDirection
        
        #add or remove one sensor
       # sensorLinksIndex = random.randint(0,len(self.sensorLinks) - 1)
        #remove sensor
      #  if (self.sensorLinks[sensorLinksIndex] == 1):
      #      self.sensorLinks[sensorLinksIndex] = 0
      #      self.sensorNeurons = self.sensorNeurons - 1
      #      self.weights = self.remove_weights()
            #print("removing")
            #print(self.weights)
        #add sensor
      #  else:      
      #      self.sensorLinks[sensorLinksIndex] = 1
      #      self.sensorNeurons = self.sensorNeurons + 1
      #      if(self.sensorNeurons == 1):
       #         self.weights = self.initialize_weights(self.sensorNeurons,self.segments-1)
       #     else:
       #         self.weights = self.append_weights()
           # print("adding")
            #print(self.weights)
            
        
        #mutate one sensor neuron weight
        if(self.sensorNeurons > 0):
           # print("sensors")
           # print(self.weights)
            if self.sensorNeurons == 1:
                row = 0
                column = random.randint(0,len(self.weights)-1)
            else:
                row = random.randint(0,len(self.weights)-1)
                column = random.randint(0,len(self.weights[0])-1)
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
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        lastYVal = 0
        lastXVal = 0
        lastZVal = 10
        
        jointx = 0
        jointy = 0
        jointz = 0
        
        x = 0
        y = 0
        z = 0
        
        jointRotations = ["1 0 0", "0 1 0", "0 0 1"]
        currentLink = 0
        
        #print(self.directionLinks)
        for i in range(self.segments):
            length = random.randint(1, c.maxLength) * .5
            width = random.randint(1, c.maxWidth) * .5
            height = random.randint(1, c.maxHeight) * .5
            
            
            #Torso link
            if i == 0:
                #edge 1
                if self.directionLinks[i] == 1:
                    jointx = -2
                    jointy = -.5
                    jointz = 10
                #edge 2
                if self.directionLinks[i] == 2:
                    jointx = -2
                    jointy = 0
                    jointz = 9.5
                #edge 3
                if self.directionLinks[i] == 3:
                    jointx = -2
                    jointy = .5
                    jointz = 10
                length = 4
                width = 1
                height = 1
                x = 0
                y = 0
                z = 10
            
            #generated joints
            else:
                #edge 1
                jointx = -1 * length
                if self.directionLinks[i-1] == 1:
                    if self.directionLinks[i] == 1:
                        jointy = -width
                        jointz = 0
                    if self.directionLinks[i] == 2:
                        jointy = -.5 * width
                        jointz = -.5 * height
                    if self.directionLinks[i] == 3:
                        jointy = 0
                        jointz = 0
                #edge 2
                if self.directionLinks[i-1] == 2:
                    if self.directionLinks[i] == 1:
                        jointy = -.5 * width
                        jointz = -.5 * height
                    if self.directionLinks[i] == 2:
                        jointy = 0
                        jointz = -height
                    if self.directionLinks[i] == 3:
                        jointy = .5 * width
                        jointz = -.5 * height
                #edge 3
                if self.directionLinks[i-1] == 3:
                   if self.directionLinks[i] == 1:
                       jointy = 0
                       jointz = 0
                   if self.directionLinks[i] == 2:
                       jointy = .5 * width
                       jointz = -.5 * height
                   if self.directionLinks[i] == 3:
                       jointy = width
                       jointz = 0
            
            #generate link posns
            if i > 0:
                x = -.5 * length
                
                #edge 1
                if self.directionLinks[i -1] == 1:
                    y = -.5 * width
                    z = 0
                #edge 2
                if self.directionLinks[i -1] == 2:
                    y = 0
                    z = -.5 *height
                #edge 3
                if self.directionLinks[i -1] == 3:
                    y = .5 * width
                    z = 0
            
            #color of links
            if self.sensorLinks[currentLink] == 1:
                color = "Green"
            else:
                color = "Blue"
            
            
            if (i == 0):
                pyrosim.Send_Cube(name= "0", pos=[x,y,z] , size=[length,width,height],colorName = color,rgb= "")
                pyrosim.Send_Joint( name = str(i) + "_" + str(i + 1), parent= str(i) , child = str(i+1) , type = "revolute", position = [jointx,jointy,jointz], jointAxis = jointRotations[random.randint(0,2)])
            elif (i<self.segments - 1):
                pyrosim.Send_Cube(name= str(i), pos=[x, y,z] , size=[length,width,height],colorName= color,rgb= "")
                pyrosim.Send_Joint( name = str(i) + "_" + str(i + 1), parent= str(i) , child = str(i +1) , type = "revolute", position = [jointx,jointy,jointz], jointAxis = jointRotations[random.randint(0,2)])
            else:
                pyrosim.Send_Cube(name= str(i), pos=[x, y,z] , size=[length,width,height], colorName= color,rgb="")
            currentLink = currentLink + 1
            
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        neuronNum = 0
        numMotors = self.segments -1
        for i in range(self.segments):
            if self.sensorLinks[i] == 1:    
                pyrosim.Send_Sensor_Neuron(name = neuronNum, linkName = str(i))
                neuronNum = neuronNum + 1

        for i in range(self.segments):
            if i != 0:
                pyrosim.Send_Motor_Neuron( name = neuronNum , jointName = str(i-1) + "_" + str(i))
                neuronNum = neuronNum + 1

        
        if(self.sensorNeurons > 0):
            for currentRow in range(self.sensorNeurons): 
               for currentColumn in range(numMotors):
                    #print("row: " + str(currentRow) + " col: " + str(currentColumn))
                    pyrosim.Send_Synapse( sourceNeuronName =  currentRow, targetNeuronName = currentColumn + self.sensorNeurons , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()
        
        
    def Set_ID(self, newID):
        self.myID = newID
    
    