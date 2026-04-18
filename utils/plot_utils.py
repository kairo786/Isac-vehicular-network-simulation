# utils/plot_utils.py

import numpy as np
import matplotlib.pyplot as plt
import config


def plot_full_network(sensing, comm, typical_line, roads):
    """
    Robust visualization:
    - Handles vertical lines properly
    - Plots all roads + typical road + RSUs
    """

    plt.figure(figsize=(8, 8))

    # ---------------------------
    # Plot all roads (light)
    # ---------------------------
    for (theta, p) in roads:

        x_vals = np.linspace(-config.R, config.R, 1000)

        # 🔥 FIX: handle vertical lines
        if abs(np.sin(theta)) > 1e-3:
            y_vals = (p - x_vals * np.cos(theta)) / np.sin(theta)
            plt.plot(x_vals, y_vals, alpha=0.2)
        else:
            # vertical line
            x_const = p / (np.cos(theta) + 1e-9)
            y_vals = np.linspace(-config.R, config.R, 1000)
            plt.plot([x_const]*len(y_vals), y_vals, alpha=0.2)

    # ---------------------------
    # Plot typical road (highlight)
    # ---------------------------
    theta, p = typical_line

    x_vals = np.linspace(-config.R, config.R, 1000)

    if abs(np.sin(theta)) > 1e-3:
        y_vals = (p - x_vals * np.cos(theta)) / np.sin(theta)
        plt.plot(x_vals, y_vals, color='red', linewidth=2, label="Typical Road")
    else:
        x_const = p / (np.cos(theta) + 1e-9)
        y_vals = np.linspace(-config.R, config.R, 1000)
        plt.plot([x_const]*len(y_vals), y_vals, color='red', linewidth=2, label="Typical Road")

    # ---------------------------
    # Plot sensing RSUs
    # ---------------------------
    if sensing:
        xs = [x for x, y in sensing]
        ys = [y for x, y in sensing]
        plt.scatter(xs, ys, s=10, label="Sensing RSUs")

    # ---------------------------
    # Plot communication RSUs
    # ---------------------------
    if comm:
        xc = [x for x, y in comm]
        yc = [y for x, y in comm]
        plt.scatter(xc, yc, s=10, marker='x', label="Comm RSUs")

    # ---------------------------
    # Plot typical user
    # ---------------------------
    plt.scatter(0, 0, color='black', s=80, label="Typical User")

    # ---------------------------
    # Formatting
    # ---------------------------
    plt.xlim(-config.R, config.R)
    plt.ylim(-config.R, config.R)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("PLP + PPP Network Visualization (Stable)")

    plt.legend()
    plt.grid()

    plt.show()