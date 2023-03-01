from solution import SOLUTION
import numpy as np
import constants as c
import copy as copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm body*.urdf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.fitnessArray = [np.zeros(c.populationSize)]
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
            
    def Evaluate(self, solutions,directOrGUI):
        
        for i in range(c.populationSize):
            self.Start_Simulation(solutions[i],directOrGUI)
        for i in range(c.populationSize):
            self.Wait_For_End(solutions[i])
            
    def Evolve(self):
        self.Evaluate(self.parents,"DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.Show_Best()
           
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children,"DIRECT")
        self.Print()
        self.Select()
        
        
    def Spawn(self):
        self.children =  {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
    
    def Mutate(self):
        for i in range(len(self.children)):   
            self.children[i].Mutate()
    
    def Select(self):
        print(self.fitnessArray)
        print("fitness array")
        self.fitnessArray = np.append(self.fitnessArray, [np.zeros(c.populationSize)], 0)
        print(self.fitnessArray)
        print("fitness array after append")
        for i in range(len(self.parents)):
            self.fitnessArray[len(self.fitnessArray)-1][i] = self.parents[i].fitness
            if(self.parents[i].fitness < self.children[i].fitness):
                self.parents[i] = self.children[i]
        
            
    def Print(self):
        print()
        
        for i in range(len(self.parents)):
            print("parent: " + str(self.parents[i].fitness) + " child: " + str(self.children[i].fitness))
        print()
        
    def Start_Simulation(self, parent,directOrGUI):
        parent.Start_Simulation(directOrGUI)
        
    def Wait_For_End(self, parent):
        parent.Wait_For_Simulation_To_End()
    
    def Show_Best(self):
        f = self.parents[0]
        for i in range(len(self.parents)):
            if(f.fitness < self.parents[i].fitness):
                f = self.parents[i]
        self.Start_Simulation(f, "GUI")