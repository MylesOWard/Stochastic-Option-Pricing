import numpy as np

__all__ = ["simulate_heston_paths"]

def simulate_heston_paths(S0, v0, rho, kappa, theta, sigma, T, N, M, r):
    dt = T / N
    S = np.full((N+1, M), S0)
    V = np.full((N+1, M), v0)
    cov = np.array([[1, rho], [rho, 1]])
    Z = np.random.multivariate_normal([0, 0], cov, (N, M))
    for i in range(1, N+1):
        S[i] = S[i-1] * np.exp((r - 0.5*V[i-1])*dt + np.sqrt(V[i-1]*dt)*Z[i-1,:,0])
        V[i] = np.maximum(V[i-1] + kappa*(theta - V[i-1])*dt + sigma*np.sqrt(V[i-1]*dt)*Z[i-1,:,1], 0)
    return S, V