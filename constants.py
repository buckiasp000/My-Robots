import numpy as np


#motor control

#Back Leg
amplitudeBL = np.pi/4
frequencyBL = 10
phaseOffsetBL = np.pi/3
maxForceBL = 1000

#Front Leg
amplitudeFL = np.pi/4
frequencyFL = 5
phaseOffsetFL = 0
maxForceFL = 500

#world
gravity = -200


#time
iterations = 10000
timeToSleep = 1/10000000000

#evolution
numberOfGenerations = 1
populationSize = 1

#neurons
numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 1