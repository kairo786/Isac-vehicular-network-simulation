import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib.pyplot as plt
import config
from simulation.metrics import compute_metrics



# CORE RUN
def run_sim():
    return compute_metrics(config.num_trials)



# SAFE CONFIG BACKUP (NO deepcopy)
def backup_config():
    backup = {}
    for k, v in config.__dict__.items():
        if not k.startswith("__") and not callable(v):
            backup[k] = v
    return backup


def restore_config(backup):
    # remove newly added keys (like fixed_distance)
    current_keys = list(config.__dict__.keys())

    for k in current_keys:
        if not k.startswith("__") and not callable(getattr(config, k)):
            if k not in backup:
                delattr(config, k)

    # restore original values
    for k, v in backup.items():
        setattr(config, k, v)


def safe_run_sim(modify_fn):
    backup = backup_config()

    try:
        modify_fn()
        return run_sim()
    finally:
        restore_config(backup)



# 1. PSP vs Distance
def plot_psp_vs_distance():
    d_vals = np.linspace(5, 15, 10)
    res = []

    for d in d_vals:
        def modify():
            config.fixed_distance = d

        Ps, _, _ = safe_run_sim(modify)
        res.append(Ps)

    plt.plot(d_vals, res, '--o')
    plt.title("PSP vs Distance")
    plt.xlabel("d")
    plt.ylabel("PSP")
    plt.grid()
    plt.show()



# 2. PSP vs Tau
def plot_psp_vs_tau():
    tau_vals = np.linspace(0.01, 1.11, 10)
    res = []

    for t in tau_vals:
        vals = []

        for _ in range(5):
            def modify():
                config.tau_sensing = t

            Ps, _, _ = safe_run_sim(modify)
            vals.append(Ps)

        res.append(np.mean(vals))

    plt.plot(tau_vals, res, '--o')
    plt.title("PSP vs Tau")
    plt.xlabel("Tau")
    plt.ylabel("PSP")
    plt.grid()
    plt.show()



# 3. PSP vs Lambda
def plot_psp_vs_lambda():
    lam_vals = np.linspace(0.001, 0.01, 10)
    res = []

    for lam in lam_vals:
        def modify():
            config.lambda_r = lam
            config.lambda_s = config.beta * lam
            config.lambda_c = (1 - config.beta) * lam

        Ps, _, _ = safe_run_sim(modify)
        res.append(Ps)

    plt.plot(lam_vals, res, '--o')
    plt.title("PSP vs Lambda")
    plt.xlabel("Lambda_r")
    plt.ylabel("PSP")
    plt.grid()
    plt.show()


# 4. CCP vs Epsilon
def plot_ccp_vs_epsilon():
    eps_vals = np.linspace(-30, 100, 15)
    res = []

    for e in eps_vals:
        def modify():
            config.epsilon_comm = e

        _, Pc, _ = safe_run_sim(modify)
        res.append(Pc)

    plt.plot(eps_vals, res, '--o')
    plt.title("CCP vs Epsilon")
    plt.xlabel("Epsilon")
    plt.ylabel("CCP")
    plt.grid()
    plt.show()


# 5. CCP vs Lambda
def plot_ccp_vs_lambda():
    lam_vals = np.linspace(0.002, 0.06, 8)
    res = []

    for lam in lam_vals:
        vals = []

        for _ in range(5):
            def modify():
                config.lambda_r = lam
                config.lambda_s = config.beta * lam
                config.lambda_c = (1 - config.beta) * lam

            _, Pc, _ = safe_run_sim(modify)
            vals.append(Pc)

        res.append(np.mean(vals))

    plt.plot(lam_vals, res, '--o')
    plt.title("CCP vs Lambda")
    plt.xlabel("Lambda_r")
    plt.ylabel("CCP")
    plt.grid()
    plt.show()


# 6. JPISAC vs Distance
def plot_jpisac_vs_distance():
    d_vals = np.linspace(0, 15, 8)
    res = []

    for d in d_vals:
        def modify():
            config.fixed_distance = d

        _, _, Pj = safe_run_sim(modify)
        res.append(Pj)

    plt.plot(d_vals, res, '--o')
    plt.title("JPISAC vs Distance")
    plt.xlabel("d")
    plt.ylabel("JPISAC")
    plt.grid()
    plt.show()


# 7. JPISAC vs Tau
def plot_jpisac_vs_tau():
    tau_vals = np.linspace(0.01, 0.2, 8)
    res = []

    for t in tau_vals:
        def modify():
            config.lambda_l = t

        _, _, Pj = safe_run_sim(modify)
        res.append(Pj)

    plt.plot(tau_vals, res, '--o')
    plt.title("JPISAC vs Tau")
    plt.xlabel("Tau")
    plt.ylabel("JPISAC")
    plt.grid()
    plt.show()


# 8. Tradeoff PSP vs CCP
def plot_tradeoff():
    beta_vals = np.linspace(0.2, 0.9, 10)

    Ps_list = []
    Pc_list = []

    for b in beta_vals:
        Ps_vals = []
        Pc_vals = []

        for _ in range(5):
            def modify():
                config.beta = b
                config.lambda_s = b * config.lambda_r
                config.lambda_c = (1 - b) * config.lambda_r
                config.epsilon_comm = 10

            Ps, Pc, _ = safe_run_sim(modify)
            Ps_vals.append(Ps)
            Pc_vals.append(Pc)

        Ps_list.append(np.mean(Ps_vals))
        Pc_list.append(np.mean(Pc_vals))

    plt.plot(Ps_list, Pc_list[::-1], '--o')
    plt.xlabel("PSP")
    plt.ylabel("CCP")
    plt.title("Tradeoff")
    plt.grid()
    plt.show()


# 9. PSP & CCP vs Beta
def plot_beta():
    beta_vals = np.linspace(0.1, 0.9, 8)

    Ps_list = []
    Pc_list = []

    for b in beta_vals:
        Ps_vals = []
        Pc_vals = []

        for _ in range(5):
            def modify():
                config.beta = b
                config.lambda_s = b * config.lambda_r
                config.lambda_c = (1 - config.beta) * config.lambda_r

            Ps, Pc, _ = safe_run_sim(modify)
            Ps_vals.append(Ps)
            Pc_vals.append(Pc)

        Ps_list.append(np.mean(Ps_vals))
        Pc_list.append(np.mean(Pc_vals))

    plt.plot(beta_vals, sorted(Pc_list)[::-1], '--o', label="CCP")
    plt.plot(beta_vals, Ps_list, '--s', label="PSP")

    plt.legend()
    plt.xlabel("Beta")
    plt.ylabel("Probability")
    plt.title("Beta Effect")
    plt.grid()
    plt.show()