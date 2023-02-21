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
timeToSleep = 1/1000000000000

#evolution
numberOfGenerations = 6
populationSize = 6

#
maxSegments = 12
maxHeight = 10
maxWidth = 8
maxLength = 8

motorJointRange = 2

