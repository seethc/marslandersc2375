#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;

int main() {

    // Record the start time
    auto start_time = std::chrono::high_resolution_clock::now();

    // declare variables
    double m, k, x, v, t_max, dt, t, a, a_new, x_new;
    vector<double> t_list, x_list, v_list;

    // mass, spring constant, initial position and velocity
    m = 1;
    k = 1;
    x = 0;
    v = 1;

    // simulation time and timestep
    t_max = 100;
    dt = 0.1;

    // Euler integration
    for (t = 0; t <= t_max; t = t + dt) {

        // append current state to trajectories
        t_list.push_back(t);
        x_list.push_back(x);
        v_list.push_back(v);

        // calculate new position and velocity
        a = -k * x / m;
        x_new = x + dt * v + 0.5 * dt * dt * a;
        a_new = -k * x_new / m;
        v = v + 0.5 * dt * (a + a_new);
        x = x_new;

    }

    
    // Write the trajectories to file
    ofstream fout;
    fout.open("trajectories.txt");
    if (fout) { // file opened successfully
      for (int i = 0; i < t_list.size(); i = i + 1) {
        fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
      }
    } else { // file did not open successfully
      cout << "Could not open trajectory file for writing" << endl;
    }

    /* The file can be loaded and visualised in Python as follows:

    import numpy as np
    import matplotlib.pyplot as plt
    results = np.loadtxt('trajectories.txt')
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(results[:, 0], results[:, 1], label='x (m)')
    plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
    plt.legend()
    plt.show()

    */

    // Record the end time
    auto end_time = std::chrono::high_resolution_clock::now();

    // Calculate the execution time in milliseconds
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);

    // Print the execution time
    std::cout << "Execution Time: " << duration.count() << " microseconds" << std::endl;

    return 0;
}
