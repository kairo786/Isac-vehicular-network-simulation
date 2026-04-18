# models/plp.py

import numpy as np
import config

def generate_roads():
    """
    Generate random roads using PLP approximation
    Returns: list of (theta, p)
    """

    # Number of roads ~ Poisson
    N = np.random.poisson(2 * config.R * config.lambda_l)
    #print("total no of roads = " , N);
    roads = []

    for _ in range(N):
        theta = np.random.uniform(0, 2*np.pi)
        p = np.random.uniform(-config.R, config.R)

        roads.append((theta, p))

    return roads

