# My-Robots
CS-396 Artificial Life My Robots
# Ludobot 3D Creatures - A Fitnessed Morphology of 3D Creatures
## CS-396 Artificial Life My Robots

<img width="390" alt="image" src="https://user-images.githubusercontent.com/58791683/220250901-f95cc504-c984-48c0-9c22-c7510018b7ea.png">

## Background
The goal of this assignment was to create a morphology of robots generated in 3D space. I created a program that generates a kinematic chain (a jointed, motorized, innervated, sensorized snake) with a: random number of randomly shaped links with random sensor placement along the chain. Each segment of the chain was generated in a different direction (x,y,z) and has the potential to fill up 3D space.

Links with and without sensors are colored green and blue, respectively.

<img width="220" alt="image" src="https://user-images.githubusercontent.com/58791683/220250771-22cff8b6-c8c7-4de0-8891-14183991b1b2.png">
<img width="250" alt="image" src="https://user-images.githubusercontent.com/58791683/220250804-d3155f26-fdde-40f0-8c9e-f92ebf5cf05a.png">

## How it's Built
The creature starts with a static torso of size (1,1,4), the first segment is generated based on that and then every other segment is generated based on the last segment. Segments are jointed along 1 of 3 edges from the last segment and then a cube is generated such that it's corner meets the corner of the last segment next to the joint. The sketches above show the generation process. Each joint is a motor that is connected to every neuron in the brain. Refer to the sketches to see how joints are generated

## Evolution
The fitness function is a function of distance traveled along the y axis. The mutation that occurs changes the direction that one segment is generated and one synapse within the creature.

## Example Fitness over Time
Seed 8:
<img width="150" alt="image" src=https://user-images.githubusercontent.com/58791683/225201675-c7b00d62-96e1-4bb3-86ae-1beb4baeb35a.png>



## Running the code
First pull the code into a repository and then navigate to the My-Robots folder in the terminal using "cd"
Type "Python3 search.py" into the command line and hit enter
Wait for all of the text to print in the terminal and then watch as an evolved ludobot wiggles accross the floor

## Modifying the code
Much modification can be done in the "constants.py" file. You can modify the amount of generations and individuals as well as the gravity, power of the motors and other variables that could improve the morphology of the 3D creature. 

A youtube video of the evolution:https://youtu.be/wDYjDOrQMZY

Citations: r/ludobots reddit page and pyrosim.py and https://chart-studio.plotly.com/create/#/

## Data


