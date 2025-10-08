import numpy as np
import matplotlib.pyplot as plt

__all__ = ["plot_paths", "antithetic_sampling"]

def plot_paths(S, T, N, title="Simulated Paths"):
    time = np.linspace(0, T, N+1)
    plt.figure(figsize=(10,6))
    plt.plot(time, S[:,:10])
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def antithetic_sampling(Z):
    return np.vstack([Z, -Z])