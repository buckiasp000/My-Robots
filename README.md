# My-Robots
CS-396 Artificial Life My Robots
# Ludobot 3D Creatures - Final Project
## CS-396 Artificial Life My Robots

<img src="https://user-images.githubusercontent.com/58791683/225218785-649ce17b-4a4c-499b-99d4-5987ace03cad.gif" width="400" height="400" />

## Methods
The goal of this final was to create a morphology of robots generated in 3D space that evolve and to run them over many generations. I created a program that generates a kinematic chain (a jointed, motorized, innervated, sensorized snake) with a: random number of randomly shaped links with random sensor placement along the chain. Each segment of the chain was generated in a different direction (x,y,z) and has the potential to fill up 3D space.

Links with and without sensors are colored green and blue, respectively.

<img width="250" alt="image" src="https://user-images.githubusercontent.com/58791683/225210192-e094884f-f173-47b8-9154-000bf96963ef.png">

## How it's Built
You can find the code that builds the creature in solution.py under the Create_Body() function. The creature starts with a static torso of size (1,1,4), the first segment is generated based on that and then every other segment is generated based on the last segment. Segments are jointed along 1 of 3 edges from the last segment and then a cube is generated such that it's corner meets the corner of the last segment next to the joint. The sketches above show the generation process. Each joint is a motor that is connected to every neuron in the brain. Refer to the sketches to see how joints, neurons and sensors are generated. Joint directions are randomly created.

<img width="390" alt="image" src="https://user-images.githubusercontent.com/58791683/220250901-f95cc504-c984-48c0-9c22-c7510018b7ea.png">

## Evolution
The fitness function is a function of distance traveled along the x axis. The mutation that occurs changes the direction that one segment is generated and one synapse within the creature.

This means that the creatures mutate such that their neurons function differently because a synapse has been changed. Their neurons adapt alongside the body changes in which one body segment is chosen at random to move to a different edge of another body segment.

## Example Fitness over Time
Seed 8:

<img width="150" alt="image" src=https://user-images.githubusercontent.com/58791683/225201675-c7b00d62-96e1-4bb3-86ae-1beb4baeb35a.png>


## Running the code
First pull the code into a repository and then navigate to the My-Robots folder in the terminal using "cd"
Type "Python3 search.py" into the command line and hit enter
Wait for all of the text to print in the terminal and then watch as an evolved ludobot wiggles accross the floor

## Modifying the code
Much modification can be done in the "constants.py" file. You can modify the amount of generations and individuals as well as the gravity, power of the motors and other variables that could improve the morphology of the 3D creature. 

## Results
I found that the creatures made large leaps in fitness, but didn't evolve slowly over time. This could have been in part due to the amount of iterations and how fitness was measured. The iterations were relatively low and fitness was measured by distance of the creatures. Evolution got stuck often. The lineages tended to look very similar to the first creature that was created. This shows that the mutations may not have been drastic enough or their was a very low likelyhood that the mutation was beneficial. 

When I dug further I found many creatures followed the "tree" strategy where they would build a body that fell such that the x value was a certain value. With limited iterations, there wasn't much time for the creatures that could move to beat the tree creatures. 

I also qualitatively noticed that creatures with less segments tended to have a higher fitness. Additionally, creatures with more sensors also tended to have a higher fitness.

Seed 7:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202853-4c93c7a6-333f-40d4-984b-79f5cfdf699d.png>
Seed 4:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202900-f4a41ee8-8e70-4b79-b73f-8210e28d13ec.png>
Seed 1:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202954-b9b3fdbc-2874-4edf-86f5-b26b67393c5c.png>
Seed 2:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202972-8d3749a6-3862-4eec-808b-6f96333643fb.png>
Seed 3:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225203013-76ef0056-1c39-4caa-8582-45f14e809a97.png>
Seed 5:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202996-cdc7e2ba-b86c-4d0e-b195-c608346065f0.png>
Seed 9:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225202926-ef58629d-dffb-47fd-810d-63453a0f1bdb.png>
Seed 10:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225203040-2c289a44-514c-4894-b986-33b4ceacab55.png>
Seed 6:
<img width="180" alt="image" src=https://user-images.githubusercontent.com/58791683/225203055-4b125259-ae8c-4d31-96ae-f57efe5c39a2.png>

I had a great idea for the final that would test the best amount of celia that a creature could have and where the optimal placement would be and I was going to do the scientific route. Unfortunately I ran into lots of bugs and after much frustration did not have time to get the code for my science version in a place that could be turned in by the due date. So, I did my best to put something together for the engineering version of the final. Though I did not have time to run 500 gens with every single seed I did so for the most that I could before turning the assignment in! I ran into some last minute bugs with the final and it took an hour to run each 500 generation version. I used 10 seeds (1-10) and each seed can be changed in constants.py using the randomseed variable.

A youtube video of the evolution: https://youtu.be/KNmzMc65zKQ
Citations: r/ludobots reddit page and pyrosim.py
