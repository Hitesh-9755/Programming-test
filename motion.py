import numpy as np  
import matplotlib.pyplot as plt  

# Simulation settings  
arena_size = 10  
speed = 0.1  
direction = np.random.uniform(0, 2 * np.pi)  
iterations = 1000  

# Starting position of the robot  
robot_position = np.array([arena_size / 2, arena_size / 2])  

# Set up the plot  
fig, ax = plt.subplots()  
ax.set_xlim(0, arena_size)  
ax.set_ylim(0, arena_size)  
robot, = ax.plot([], [], 'ro', markersize=8)  

def move_robot():  
    global robot_position, direction  
    
    # Update position based on movement direction  
    robot_position[0] += speed * np.cos(direction)  
    robot_position[1] += speed * np.sin(direction)  
    
    # Collision handling (bounce off walls)  
    if robot_position[0] <= 0 or robot_position[0] >= arena_size:  
        direction = np.pi - direction  
        robot_position[0] = np.clip(robot_position[0], 0, arena_size)  
    
    if robot_position[1] <= 0 or robot_position[1] >= arena_size:  
        direction = -direction  
        robot_position[1] = np.clip(robot_position[1], 0, arena_size)  
    
    # Update robot's location on the plot  
    robot.set_data([robot_position[0]], [robot_position[1]])  

# Run the simulation  
for _ in range(iterations):  
    move_robot()  
    plt.pause(0.01)  

plt.show()