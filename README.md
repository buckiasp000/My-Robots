# Ludbot Spot - A Crawling Gait
## CS-396 Artificial Life My Robots
<img width="446" alt="image" src="https://user-images.githubusercontent.com/58791683/217708483-50725982-06d4-4e9a-9fca-759fd732e8ae.png">

## Background
The goal of this assignment was to create a robot with a unique shape that learned to do a task. I was inspired by Boston Dynamics "Spot" and set out to make a robot that could mimic its gait. Unfortunately my results weren't on par with Boston Dynamics, but they did train the robot to crawl along the ground at a somewhat regular gait.

## Background
The fitness function is a function of distance traveled, but there are also built in gaits that effect the evolution of the creature. This is from the "Marching to the Beat" section of the final project of the ludobots Reddit course. Math.sin(timeStep) is used to create a gait that effects the rest of the neurons
<img width="693" alt="image" src="https://user-images.githubusercontent.com/58791683/217710495-8f96f5df-6686-4368-b403-bf7c67f9391b.png">

## Running the code
First pull the code into a repository and then navigate to the My-Robots folder in the terminal using "cd"
Type "Python3 search.py" into the command line and hit enter
Wait for all of the text to print in the terminal and then watch as an evolved ludobot scampers accross the floor

## Modifying the code
Much modification can be done in the "constants.py" file. You can modify the amount of generations and individuals as well as the gravity, power of the motors and other variables that could improve the morphology of the dog. 

A youtube video of the evolution: https://youtu.be/VFDnW-rOVwA
