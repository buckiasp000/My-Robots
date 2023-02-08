import numpy as np


#motor control

#Back Leg
amplitudeBL = np.pi/4
frequencyBL = 10
phaseOffsetBL = np.pi/3
maxForceBL = 500

#world
gravity = -10


#time
iterations = 2000
timeToSleep = 1/1000000000000000000

#evolution
numberOfGenerations = 10
populationSize = 5

#body
numSegments = 10

#neurons
numSensorNeurons = 5 + numSegments * 4
numMotorNeurons = 4 + numSegments * 4

motorJointRange = 1.25

