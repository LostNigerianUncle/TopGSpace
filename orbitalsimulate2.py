import numpy as np
from os import name
from orbitalphysics import euler_step
from orbitalconstants import MU_EARTH, R_EARTH, MU_MOON, R_MOON

def circular_orbit_velocity(altitude):
    """
    Calculate the circular orbit velocity at a given altitude above Earth's surface.

    Parameters:
    altitude (float): Altitude above Earth's surface in meters.

    Returns:
    float: Circular orbit velocity in meters per second.
    """
    r = R_EARTH + altitude  # Total distance from Earth's centre
    r = R_MOON + altitude # Total distance from Moon's centre
    return np.sqrt(MU_EARTH / r), np.sqrt(MU_MOON / r)

def run_simulation(initial_altitude, time_step, total_time):
    """
    Run a simulation of a satellite in circular orbit around Earth.

    Parameters:
    initial_altitude (float): Initial altitude above Earth's surface in meters.
    time_step (float): Time step for the simulation in seconds.
    total_time (float): Total simulation time in seconds.

    Returns:
    list: List of positions and velocities at each time step.
    """
    if altitude_km < 0:
        raise ValueError("altitude_km must be non-negative")
    if num_orbits <= 0 or steps_per_orbit <= 0:
        raise ValueError("num_orbits and steps_per_orbit must be positive")
    # Initial conditions
    r = R_EARTH + initial_altitude  # Total distance from Earth's centre
    r = R_MOON + initial_altitude # Total distance from Moon's centre
    v = circular_orbit_velocity(initial_altitude)  # Circular orbit velocity
    position = np.array([earthradius, 0.0])
    velocity = np.array([0.0, v[0]]) # Value error: circular_orbit_velocity returns a tuple, but only the first value is used for Earth. The second value for Moon is ignored.
    positions = np.empty((total_steps + 1, 2))
    
    # Initialize position and velocity vectors
    position = np.array([r, 0])  # Start at (r, 0)
    velocity = np.array([0, v])   # Velocity perpendicular to position

    results = []

    for t in np.arange(0, total_time, time_step):
        results.append((position.copy(), velocity.copy()))
        position, velocity = euler_step(position, velocity, time_step)

    return results

if name == "__main__":
    # Example usage
    initial_altitude = 400e3  # 400 km above Earth's surface
    time_step = 10.0          # 10 seconds
    total_time = 3600.0       # 1 hour

    simulation_results = run_simulation(initial_altitude, time_step, total_time)

    for pos, vel in simulation_results:
        print(f"Position: {pos}, Velocity: {vel}")
