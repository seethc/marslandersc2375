import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # gravitational constant
M = 6.42e23  # mass of Mars
t_max = 1e4
dt = 0.1
t_array = np.arange(0, t_max, dt)

# Scenarios
scenarios = ['descent', 'circular', 'elliptical', 'escape']

for scenario in scenarios:
    # Initial conditions
    position = np.array([4e6, 0, 0])  # initial position
    if scenario == 'descent':
        velocity = np.array([0, 0, 0])  # initial velocity
    else:
        r = np.linalg.norm(position)
        if scenario == 'circular':
            speed = np.sqrt(G * M / r)
        elif scenario == 'elliptical':
            speed = 0.8 * np.sqrt(G * M / r)
        else:  # scenario == 'escape'
            speed = np.sqrt(2 * G * M / r)
        velocity = np.array([0, speed, 0])  # initial velocity

    # Lists to record trajectories
    position_list = []
    velocity_list = []

    # Euler integration
    for t in t_array:
        # Append current state to trajectories
        position_list.append(position)
        velocity_list.append(velocity)

        # Calculate new position and velocity
        r = np.linalg.norm(position)  # distance from the center
        a = -G * M * position / r**3  # acceleration
        velocity_new = velocity + a * dt
        position = position + velocity_new * dt
        velocity = velocity_new

    # Convert trajectory lists into arrays
    position_array = np.array(position_list)
    velocity_array = np.array(velocity_list)

    # Plotting
    if scenario == 'descent':
        # Plot altitude as a function of time
        plt.figure()
        plt.plot(t_array, np.linalg.norm(position_array, axis=1))
        plt.xlabel('Time (s)')
        plt.ylabel('Altitude (m)')
        plt.title('Straight down descent')
        plt.grid(True)
        plt.xlim(0, 1e3)
        plt.show()
    else:
        # Plot the trajectory in the orbital plane
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(position_array[:, 0], position_array[:, 1], position_array[:, 2])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([-5e6, 5e6])  # adjust plot limits
        ax.set_ylim([-5e6, 5e6])  # adjust plot limits
        ax.set_zlim([-5e6, 5e6])  # adjust plot limits
        ax.set_title(scenario.capitalize() + ' orbit')
        plt.show()
