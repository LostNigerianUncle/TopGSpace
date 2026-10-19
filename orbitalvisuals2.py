import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D

from orbitalsimulate2 import run_simulation
from orbitalconstants import R_EARTH, R_MOON

def plot_orbit(positions, title = "2D Orbital Simulation (Euler Integration)"):
    fig, ax = plt.subplots(figsize = (6, 6)) 

    earth = plt.circle((0, 0), R_EARTH, color = 'dodgerblue', label = "Earth", alpha = 0.5, zorder = 2)
    ax.add_patch(earth)

    moon = plt.Circle((38430000, 0), R_MOON, color = 'lightgray', label = "Moon", alpha = 0.5, zorder = 2)
    ax.add_patch(moon)

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

class verts:
    """Convenient polygon representation for the spacecraft body"""
    def __init__(self, size = 500000):
        self.size = float(size)
        self._points = np.array([
            (0.0, self.size),
            (self.size * 0.4, -self.size * 0.6),
            (0.0, -self.size * 0.3),
            (-self.size * 0.4, -self.size * 0.6),
            (0.0, self.size),
        ], dtype = float)

    @property
    def points(self):
        return self._points.copy()

    def as_list(self):
        return self._points.tolist()

    def __iter__(self):
        return iter(self._points.tolist())

    def __len__(self):
        return len(self._points)

    def __getitem__(self, index):
        return self._points[index]

def make_spacecraft_patch(x, y, heading_deg, size = 300000):
    spacecraft_verts = verts(size)
    path = Path(spacecraft_verts.as_list())
    transform = Affine2D().rotate_deg(heading_deg - 90).translate(x, y) + ax.transData
    return PathPatch(path, transform = transform, color = 'orangered', zorder = 4)
    


if __name__ == "__main__":
    positions, dt = run_simulation(altitude_km = 400, num_orbits = 2, steps_per_orbit = 1000)
    fig = plot_orbit(positions)
    fig.savefig("orbit_output.png", dpi = 150)
    print("Saved plot to orbit_output.png")

    ax = fig.axes[0]

    def update(frame):
        ax.clear()
        plot_orbit(positions[:frame + 1], ax = ax)

matplotlib.animation.FuncAnimation(
    fig, update, frames = lens(positions), interval = dt * 200, repeat = False
)
plt.show()
