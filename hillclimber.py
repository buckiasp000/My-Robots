from solution import SOLUTION
import numpy as np
import constants as c
import copy as copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        
        
    def Evolve(self):
        self.Show_Best()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.Show_Best()
           
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
        
    def Spawn(self):
        self.child =  copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child
            
    def Print(self):
        print("parent: " + str(self.parent.fitness) + " child: " + str(self.child.fitness))
        
    def Show_Best(self):
        self.parent.Evaluate("GUI")