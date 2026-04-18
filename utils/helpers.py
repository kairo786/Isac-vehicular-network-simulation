# utils/helpers.py

import numpy as np

def is_on_line(x, y, theta, p=0, tol=1e-2):
    return abs(x*np.cos(theta) + y*np.sin(theta) - p) < tol


def nearest_rsu(rsus, theta):
    """
    Find nearest RSU on the typical road (passing through origin)
    """

    candidates = [
        (x, y) for (x, y) in rsus
        if is_on_line(x, y, theta)
    ]

    if not candidates:
        return None, None

    nearest = min(candidates, key=lambda pt: np.sqrt(pt[0]**2 + pt[1]**2))

    d = np.sqrt(nearest[0]**2 + nearest[1]**2)

    return nearest, d