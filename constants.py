import numpy as np


#motor control

#Back Leg
amplitudeBL = np.pi/4
frequencyBL = 10
phaseOffsetBL = np.pi/3
maxForceBL = 500

#Front Leg
amplitudeFL = np.pi/4
frequencyFL = 5
phaseOffsetFL = 0
maxForceFL = 500

#world
gravity = -200


#time
iterations = 1000
timeToSleep = 1/240