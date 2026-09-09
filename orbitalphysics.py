import numpy as np
from orbitalconstants import MU_EARTH

def gravitational_acceleration(altitude):
    """
    Calculate the gravitational acceleration at a given altitude above Earth's surface.

    Parameters:
    altitude (float): Altitude above Earth's surface in meters.

    Returns:
    float: Gravitational acceleration in m/s^2.
    """
    radius_earth = 6371000  # Average radius of Earth in meters
    distance_from_center = radius_earth + altitude
    g = MU_EARTH / (distance_from_center ** 2)
    return g

def euler_step(position, velocity, acceleration, dt):
    """
    Perform a single Euler integration step.

    Parameters:
    position (numpy.ndarray): Current position vector.
    velocity (numpy.ndarray): Current velocity vector.
    acceleration (numpy.ndarray): Current acceleration vector.
    dt (float): Time step in seconds.

    Returns:
    tuple: Updated position and velocity vectors.
    """
    new_position = position + velocity * dt
    new_velocity = velocity + acceleration * dt
    return new_position, new_velocity

