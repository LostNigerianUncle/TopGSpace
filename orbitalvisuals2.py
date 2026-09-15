import matplotlib.pyplot as plt
from orbitalsimulate2 import run_simulation
from orbitalconstants import R_EARTH

def plot_orbit(positions, title = "2D Orbital Simulation (Euler Integration)"):
    fig, ax = plt.subplots(figsize = (6, 6)) 

    earth = plt.circle((0, 0), R_EARTH, color = 'dodgerblue', label = "Earth", alpha = 0.5, zorder = 2)
    ax.add_patch(earth)

    ax.plot(positions[:, 0], positions[:, 1], color = 'orangered',
            linewidth = 1.2, label = "Spacecraft Trajectory", zorder = 1)
    ax.scatter(positions[0, 0], positions[0, 1], color = 'black',
               s = 25, zorder = 3, label = "Start Position")

    ax.set_aspect("equal")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    positions, dt = run_simulation(altitude_km = 400, num_orbits = 2, steps_per_orbit = 1000)
    fig = plot_orbit(positions)
    fig.savefig("orbit_output.png", dpi = 150)
    print("Saved plot to orbit_output.png")

matplotlib.animation.FuncAnimation(
    fig, update, frames = lens(positions), interval = dt * 1000, repeat = False
)
plt.show()
