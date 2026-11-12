import numpy as np
from orbitalconstants import MU_EARTH

def gravitational_acceleration(altitude):
    """
    Calculate the gravitational acceleration at a given altitude above Earth's surface.
    """
    radius_earth = 6371000  # Average radius of Earth in meters
    distance_from_center = radius_earth + altitude
    g = MU_EARTH / (distance_from_center ** 2)
    return g

def euler_step(position, velocity, acceleration, dt):
    """
    Perform a single Euler integration step.
    """
    new_position = position + velocity * dt
    new_velocity = velocity + acceleration * dt
    return new_position, new_velocity

def hohmann_transfer_velocity(r1, r2):
    """
    Calculate the delta-v required for a Hohmann transfer between two circular orbits.
    """
    mu = MU_EARTH
    v1 = np.sqrt(mu / r1)
    v2 = np.sqrt(mu / r2)
    a_transfer = (r1 + r2) / 2
    v_transfer1 = np.sqrt(mu * (2 / r1 - 1 / a_transfer))
    v_transfer2 = np.sqrt(mu * (2 / r2 - 1 / a_transfer))
    
    delta_v1 = v_transfer1 - v1
    delta_v2 = v2 - v_transfer2
    
    return delta_v1, delta_v2

def on_press(key):
    """
    Handle key press events for the simulation.
    """
    if key == 'up':
        print("Increase altitude")
    elif key == 'down':
        print("Decrease altitude")
    elif key == 'left':
        print("Rotate left")
    elif key == 'right':
        print("Rotate right")

def on_release(key):
    """
    Handle key release events for the simulation.
    """
    print(f"Key released: {key}")
