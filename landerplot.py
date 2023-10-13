import matplotlib.pyplot as plt
import numpy as np

# Load the data from the .txt file
file_path = 'telemetryX5.txt'
height_list = []
descent_rate_list = []

# Load data from the .txt file
data = np.loadtxt('telemetryX5.txt', delimiter=' ')
height_list, descent_rate_list = data[:, 0], data[:, 1]

# Define different values of Kh
kh_values = [0.018, 0.018993, 0.02]

plt.figure(figsize=(8, 6))

# Plot target descent rates for different Kh values
for kh in kh_values:
    target_rate = -0.5 - kh * height_list
    plt.plot(height_list, target_rate, '--', label=f'Target (Kh={kh})')

# Load data from the .txt file
data = np.loadtxt('telemetryX5.txt', delimiter=' ')
data = sorted(data, key=lambda x: x[0])
# height_list, descent_rate_list = data[:, 0], data[:, 1]
height_list, descent_rate_list = zip(*data)

# Create the plot
plt.plot(height_list, descent_rate_list,label='Descent Rate')
plt.xlabel('Height (m)')
plt.ylabel('Vertical Velocity (m/s)')
plt.title('Vertical Velocity vs. Height')
plt.grid(True)
plt.legend()
plt.gca().invert_xaxis()  # Invert the x-axis to make it descending
plt.show()
