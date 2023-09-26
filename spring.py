# uncomment the next line if running in a notebook
# %matplotlib inline

import time

# Record the start time
start_time = time.time()
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# initialise start conditions for analytical check
x_anal = x
v_anal = v

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
x_anal_list = []
v_anal_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    v_new = v + a * dt
    x = x + v_new * dt
    v = v_new

    # analytical check
    x_anal_list.append(x_anal)
    v_anal_list.append(v_anal)

    x_anal = np.sqrt(m/k) * np.sin(np.sqrt(k/m)*t)
    v_anal = np.cos(np.sqrt(k/m)*t)



# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)
x_anal_array = np.array(x_anal_list)
v_anal_array = np.array(v_anal_list)

"""# plot the position-time graph
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

print(x_list)"""

# Record the end time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time
print(f"Total Execution Time: {execution_time} seconds")