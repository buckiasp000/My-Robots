import numpy as np
import matplotlib.pyplot as m
backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAnglesBL = np.load("data/targetAnglesBL.npy")
targetAnglesFL = np.load("data/targetAnglesFL.npy")
m.plot(backLegSensorValues, label = "back leg", linewidth = 4)
m.plot(frontLegSensorValues, label = "front leg")
m.plot(targetAnglesBL, label = "targetAnglesBL", linewidth = 4)
m.plot(targetAnglesFL, label = "targetAnglesFL")
m.legend()
m.show()