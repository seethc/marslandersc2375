# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
G = 6.6743e-11
M = 6.42e23

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# Initial conditions
position = np.array([1, 0, 0])  # initial position
velocity = np.array([0, 1, 0])  # initial velocity

# initialise empty lists to record trajectories
position_list = []
velocity_list = []



# Euler integration
for t in t_array:

    # append current state to trajectories
    position_list.append(position)
    velocity_list.append(velocity)

    # Calculate new position and velocity
    r = np.linalg.norm(position)  # distance from the center
    a = -G * M * position / r**3  # acceleration
    velocity_new = velocity + a * dt
    position = position + velocity_new * dt
    velocity = velocity_new


# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
position_array = np.array(position_list)
velocity_array = np.array(velocity_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.plot(t_array, x_anal_array, label='x analy (m)')
plt.plot(t_array, v_anal_array, label='v analy (m/s)')
plt.legend()
plt.show()