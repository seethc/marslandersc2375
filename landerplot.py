import matplotlib.pyplot as plt
import numpy as np

# Load the data from the .txt file
file_path = 'telemetry.txt'
height_list = []
descent_rate_list = []

# Load data from the .txt file (assuming it's named telemetry.txt)
data = np.loadtxt('telemetry.txt', delimiter=' ')
height_list, descent_rate_list = data[:, 0], data[:, 1]

# Define different values of Kh
kh_values = [0.03, 0.035, 0.04]

plt.figure(figsize=(8, 6))

# Plot target descent rates for different Kh values
for kh in kh_values:
    target_rate = -0.5 - kh * height_list
    plt.plot(height_list, target_rate, label=f'Target (Kh={kh})')


# Create the plot
plt.plot(height_list, descent_rate_list, '--',label='Descent Rate')
plt.xlabel('Height (m)')
plt.ylabel('Vertical Velocity (m/s)')
plt.title('Vertical Velocity vs. Height')
plt.grid(True)
plt.legend()
plt.gca().invert_xaxis()  # Invert the x-axis to make it descending
plt.show()
