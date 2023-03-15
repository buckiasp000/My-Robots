from solution import SOLUTION
import numpy as np
import constants as c
import copy as copy
import os
import pickle
import matplotlib.pyplot as plt

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
        self.Plot_Fitness()
           
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
        self.fitnessArray = np.append(self.fitnessArray, [np.zeros(c.populationSize)], 0)
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
            if (i == len(self.parents) -1):
                self.Start_Simulation(f, "GUI")
            if(f.fitness < self.parents[i].fitness):
                f = self.parents[i]
        file = open("pickled_best_creature with randomSeed: " + str(c.randomSeed), "wb")
        pickle.dump(f, file, protocol = 3)
        file.close()
        
    
    def Plot_Fitness(self):
        for i in range(c.populationSize):
            arrayToPlot = []
            for j in range(c.numberOfGenerations+1):
                if(j !=0):
                    arrayToPlot.append(self.fitnessArray[j][i])
            plt.plot(arrayToPlot)
        
        plt.ylabel("fitness: distance in x direction")
        plt.xlabel("generations")
        plt.title("Evolved Creature's Distance Moved After " + str(c.iterations) + " Timesteps")
        plt.show()
