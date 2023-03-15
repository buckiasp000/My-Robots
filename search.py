import os as os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random as random
import constants as c
import numpy as np

random.seed(c.randomSeed)
np.random.seed(c.randomSeed)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
    