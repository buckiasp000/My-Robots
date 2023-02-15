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
timeToSleep = 1/100000000

#evolution
numberOfGenerations = 3
populationSize = 3

#
maxSegments = 10
maxHeight = 4
maxWidth = 4
maxLength = 4

motorJointRange = 2

