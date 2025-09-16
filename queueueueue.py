import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_rate = 3.0  # Arrival rate (customers per unit time)
mu_rate = 4.0      # Service rate (customers per unit time)
simulation_time = 100  # Total simulation time

# Initialize variables
time = 0
queue = []
server_busy = False
next_arrival = np.random.exponential(1/lambda_rate)
next_departure = float('inf')
num_customers = 0
total_wait_time = 0
total_service_time = 0

# Lists to store data for analysis
arrival_times = []
departure_times = []
wait_times = []

# Simulation loop
while time < simulation_time:
    if next_arrival < next_departure:
        # Arrival event
        time = next_arrival
        arrival_times.append(time)
        num_customers += 1
        if server_busy:
            queue.append(time)
        else:
            server_busy = True
            next_departure = time + np.random.exponential(1/mu_rate)
        next_arrival = time + np.random.exponential(1/lambda_rate)
    else:
        # Departure event
        time = next_departure
        departure_times.append(time)
        num_customers -= 1
        if queue:
            arrival_time = queue.pop(0)
            wait_time = time - arrival_time
            wait_times.append(wait_time)
            total_wait_time += wait_time
            next_departure = time + np.random.exponential(1/mu_rate)
        else:
            server_busy = False
            next_departure = float('inf')

# Calculate performance metrics
if arrival_times and departure_times:
    # Use the minimum length to avoid index errors
    min_length = min(len(arrival_times), len(departure_times))
    utilization = sum([departure_times[i] - arrival_times[i] for i in range(min_length)]) / simulation_time
    average_wait_time = total_wait_time / len(arrival_times)
else:
    utilization = 0
    average_wait_time = 0

# Output results
print(f"Average wait time: {average_wait_time:.2f}")
print(f"Server utilization: {utilization:.2f}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(wait_times, bins=20, edgecolor='black')
plt.title('Distribution of Wait Times')
plt.xlabel('Wait Time')
plt.ylabel('Frequency')
plt.savefig("Result.png")