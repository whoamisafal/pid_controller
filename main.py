import matplotlib.pyplot as plt
import matplotlib.animation as animation
from drone import Drone
from pid import PIDController

# Simulation parameters
dt = 0.01
simulation_time = 100  # seconds

# Initialize drone and PID controller
drone = Drone(weight=2)
pid = PIDController(Kp=5, Ki=1, Kd=3, setPoint=10)

# Lists to store time, altitude, and thrust for plotting
time_list = []
altitude_list = []
thrust_list = []

# Set up the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
ax1.set_ylabel('Altitude (m)')
ax1.set_title('Drone Altitude Control with PID')
ax1.grid()
line1, = ax1.plot([], [], label='Altitude')
ax1.legend()

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Thrust (N)')
ax2.grid()
line2, = ax2.plot([], [], label='Thrust', color='r')
ax2.legend()

# Initialize the data to be plotted
def init():
    ax1.set_xlim(0, simulation_time)
    ax1.set_ylim(0, 15)  # Assuming altitude will not exceed 15 meters
    ax2.set_xlim(0, simulation_time)
    ax2.set_ylim(0, 50)  # Assuming thrust will not exceed 50 N
    return line1, line2

# Update the plot with new data
def update_plot(frame):
    global time_list, altitude_list, thrust_list
    
    time = frame * dt
    thrust = pid.update(drone.altitude, dt)
    drone.update(thrust=thrust, dt=dt)
    
    time_list.append(time)
    altitude_list.append(drone.altitude)
    thrust_list.append(thrust)
    
    line1.set_data(time_list, altitude_list)
    line2.set_data(time_list, thrust_list)
    
    return line1, line2

# Create the animation
ani = animation.FuncAnimation(fig, update_plot, frames=range(int(simulation_time / dt)),
                              init_func=init, blit=True, interval=10, repeat=False)

plt.tight_layout()
plt.show()
