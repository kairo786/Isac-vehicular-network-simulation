import numpy as np
import config


def distance(x, y):
    return np.sqrt(x**2 + y**2)



# Distance Override (IMPORTANT)
def get_distance(default_d):
    if hasattr(config, "fixed_distance"):
        return config.fixed_distance
    return default_d



# Antenna gain
def random_gain(main_gain, side_gain, beamwidth):
    q = beamwidth / (2 * np.pi)
    return main_gain if np.random.rand() < q else side_gain


# SENSING INTERFERENCE
def compute_sensing_interference(rsus):

    I_s = 0.0

    for (x, y) in rsus:
        l = distance(x, y) + 1e-9

        sigma = np.random.exponential(scale=1.0)  # FIXED scale

        Mt = random_gain(config.M_s_T, config.m_s_T, config.theta_s)
        Mr = random_gain(config.M_s_R, config.m_s_R, config.theta_s)

        A_s = (Mr * config.lambda_wave**2) / (4*np.pi)
        P_d = (config.P_tx * Mt) / (4*np.pi)

        I_s += A_s * P_d * sigma * (l ** -config.alpha)

    return I_s



# COMM INTERFERENCE
def compute_comm_interference(rsus):

    I_c = 0.0

    for (x, y) in rsus:
        l = distance(x, y) + 1e-9

        G = np.random.gamma(shape=1.0, scale=1.0)

        Ct = random_gain(config.M_c_T, config.m_c_T, config.theta_c)
        Cr = random_gain(config.M_c_R, config.m_c_R, config.theta_c)

        I_c += config.P_tx * Ct * Cr * G * (l ** -config.alpha)

    return I_c



# SIGNAL POWER
def sensing_signal_power(d):

    d = get_distance(d)

    sigma = np.random.exponential(scale=1.0)

    Pe = (config.P_tx *
          config.M_s_T *
          config.M_s_R *
          (config.lambda_wave**2) *
          sigma) / ((4*np.pi)**3 * (d ** (2 * config.alpha)) + 0.00000000001)

    return Pe


def comm_signal_power(d):

    d = get_distance(d)

    G = np.random.gamma(shape=1.0, scale=1.0)

    S = config.P_tx * config.M_c_T * G * (d ** -config.alpha)

    return S


# SIR
def compute_sir_sensing(d, I_s, I_c):
    return sensing_signal_power(d) / (I_s + I_c + 1e-12)


def compute_sir_comm(d, I_s, I_c):
    return comm_signal_power(d) / (I_s + I_c + 1e-12)