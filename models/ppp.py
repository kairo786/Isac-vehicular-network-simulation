# models/ppp.py

import numpy as np
import config

def generate_points_on_line(theta, p, intensity):
    """
    Generate RSUs on a given line
    Returns list of (x, y)
    """

    points = []

    # direction vector of line
    dx = -np.sin(theta)
    dy = np.cos(theta)

    # pick a center point on line
    x0 = p * np.cos(theta)
    y0 = p * np.sin(theta)

    # length of line inside square (approx)
    L = 2 * config.R

    # number of points
    N = np.random.poisson(intensity * L)
    
    for _ in range(N):
        t = np.random.uniform(-config.R, config.R)

        x = x0 + t * dx
        y = y0 + t * dy

        # keep only inside region
        if abs(x) <= config.R and abs(y) <= config.R:
            points.append((x, y))

    return points