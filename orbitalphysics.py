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

def hohmann_transfer_velocity(r1, r2):
    """
    Calculate the delta-v required for a Hohmann transfer between two circular orbits.

    Parameters:
    r1 (float): Radius of the initial orbit in meters.
    r2 (float): Radius of the final orbit in meters.

    Returns:
    tuple: Delta-v for the first burn and second burn in m/s.
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

