# simulation/network.py

import numpy as np
import config

from models.plp import generate_roads
from models.ppp import generate_points_on_line

def generate_network():
    """
    Generate full network:
    - PLP roads
    - PPP RSUs on each road
    """

    roads = generate_roads() # har ek line ke liye (0,p) return krta hai
    
    #print("total no of roads = " , len(roads));
    
    # Add typical road (must pass origin)
    theta0 = np.random.uniform(0, 2*np.pi)
    typical_line = (theta0, 0)

    roads.append(typical_line)

    sensing_RSUs = []
    comm_RSUs = []

    for (theta, p) in roads:

        # sensing RSUs
        pts_s = generate_points_on_line(theta, p, config.lambda_s) # cordinates return karta hai
        sensing_RSUs.extend(pts_s)

        # communication RSUs
        pts_c = generate_points_on_line(theta, p, config.lambda_c) # cordinates return karta hai
        comm_RSUs.extend(pts_c)
        # print(f"Road (theta={theta:.2f}, p={p:.2f}) -> sensing points = {len(pts_s)} , communication points = {len(pts_c)}")

    return sensing_RSUs, comm_RSUs, typical_line,roads