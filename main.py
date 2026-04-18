# main.py

import config
import numpy as np
from simulation.metrics import compute_metrics
from simulation.network import generate_network
from simulation.sir import (
    compute_sensing_interference,
    compute_comm_interference,
    compute_sir_sensing,
    compute_sir_comm,
    sensing_signal_power,
    comm_signal_power
)

from utils.helpers import nearest_rsu
from utils.plot_utils import plot_full_network


#  DEBUG MODE (Single Trial)
def debug_single_trial():

    sensing_RSUs, comm_RSUs, typical_line, roads = generate_network()

   
    
    theta, _ = typical_line

    # nearest RSUs
    serving_s, d_s = nearest_rsu(sensing_RSUs, theta)
    serving_c, d_c = nearest_rsu(comm_RSUs, theta)

    if serving_s is None:
        print("❌ No sensing RSU on typical line")
        return

    if serving_c is None:
        serving_c = serving_s
        d_c = d_s

    # remove serving
    sensing_interferers = [pt for pt in sensing_RSUs if pt != serving_s]
    comm_interferers = [pt for pt in comm_RSUs if pt != serving_c]

    # interference
    I_s = compute_sensing_interference(sensing_interferers)
    I_c = compute_comm_interference(comm_interferers)

    # signal
    Pe = sensing_signal_power(d_s)
    S = comm_signal_power(d_c)

    # SIR
    gamma_s = Pe / (I_s + I_c + 1e-12)
    gamma_c = S / (I_s + I_c + 1e-12)

    print("\n===== 🔍 DEBUG SINGLE TRIAL =====")
    print(f"d_s (distance sensing): {d_s:.4f}")
    print(f"d_c (distance comm):    {d_c:.4f}")

    print("\n--- SIGNAL ---")
    print(f"Sensing Signal (Pe): {Pe:.6e}")
    print(f"Comm Signal (S):     {S:.6e}")

    print("\n--- INTERFERENCE ---")
    print(f"I_s (sensing): {I_s:.6e}")
    print(f"I_c (comm):    {I_c:.6e}")
    print(f"Total I:       {(I_s+I_c):.6e}")

    print("\n--- SIR ---")
    print(f"Sensing SIR: {gamma_s:.6e}")
    print(f"Comm SIR:    {gamma_c:.6e}")

    print("\n--- CONDITIONS ---")
    print(f"Sensing Success: {gamma_s > config.tau_sensing}")
    print(f"Comm Success:    {gamma_c > config.epsilon_comm}")
    plot_full_network(sensing_RSUs, comm_RSUs, typical_line, roads)


# 🚀 MAIN (Monte Carlo)
from simulation.metrics import compute_metrics

def run_full_simulation():

    Ps, Pc, Pj = compute_metrics(config.num_trials)

    print("\n===== RESULTS =====")
    print(f"PSP (P_s): {Ps:.4f}")
    print(f"CCP (P_c): {Pc:.4f}")
    print(f"JPISAC (P_j): {Pj:.4f}")



# ENTRY
if __name__ == "__main__":

    # 🔁 पहले debug run करो
    debug_single_trial()

    # 🔁 फिर full simulation
    #run_full_simulation()