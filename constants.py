import numpy as np
import random

#motor control

randomSeed = 8
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
iterations = 5000
timeToSleep = 1/100000

#evolution
numberOfGenerations = 500
populationSize = 10

#
maxSegments = 5
maxHeight = 10
maxWidth = 8
maxLength = 8

motorJointRange = 2

