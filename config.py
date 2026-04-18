# config.py

import numpy as np

# Geometry
R = 200

# Densities
lambda_l = 0.0125  #  0.01
lambda_r = 2*0.005 #0.005

beta = 0.5
lambda_s = beta * lambda_r
lambda_c = (1 - beta) * lambda_r

sigma_scale = 100000
# Physics
alpha = 2.2 #2.5
P_tx = 1   #0.1   # increased

# Antenna gains
M_s_T = 1000
M_s_R = 1000
m_s_T = 0.63
m_s_R = 0.63

M_c_T = 1000
M_c_R = 1000
m_c_T = 0.63
m_c_R = 0.63

# Beamwidth (NEW)
theta_s = np.pi / 6   # 30 deg
theta_c = np.pi / 6

# Wavelength
c = 3e8
f_c = 76.5e9
lambda_wave = c / f_c

# Thresholds
tau_sensing = 0.01
epsilon_comm = 0.1

# Simulation
num_trials = 1000