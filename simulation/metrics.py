import numpy as np
import config

from simulation.network import generate_network
from simulation.sir import (
    compute_sensing_interference,
    compute_comm_interference,
    compute_sir_sensing,
    compute_sir_comm
)

from utils.helpers import nearest_rsu


def run_trial():

    sensing_RSUs, comm_RSUs, typical_line, roads = generate_network()

    theta, _ = typical_line

    serving_s, d_s = nearest_rsu(sensing_RSUs, theta)
    serving_c, d_c = nearest_rsu(comm_RSUs, theta)

    if serving_s is None:
        return 0, 0

    if serving_c is None:
        serving_c = serving_s
        d_c = d_s

    sensing_interferers = [pt for pt in sensing_RSUs if pt != serving_s]
    comm_interferers = [pt for pt in comm_RSUs if pt != serving_c]

    I_s = compute_sensing_interference(sensing_interferers)
    I_c = compute_comm_interference(comm_interferers)

    gamma_s = compute_sir_sensing(d_s, I_s, I_c)
    gamma_c = compute_sir_comm(d_c, I_s, I_c)

    success_s = (gamma_s > config.tau_sensing)
    success_c = (gamma_c > config.epsilon_comm)

    return int(success_s), int(success_s and success_c)


def compute_metrics(num_trials):

    sensing_success = 0
    joint_success = 0

    for _ in range(num_trials):
        s, j = run_trial()
        sensing_success += s
        joint_success += j

    Ps = sensing_success / num_trials
    Pc = joint_success / sensing_success if sensing_success > 0 else 0
    Pj = joint_success / num_trials

    return Ps, Pc, Pj