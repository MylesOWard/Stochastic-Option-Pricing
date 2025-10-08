import numpy as np
from scipy.stats import norm

__all__ = ["price_european_mc", "price_asian_mc"]

def price_european_mc(S0, K, r, sigma, T, M, steps, option_type="call"):
    dt = T / steps
    Z = np.random.randn(M, steps)
    S = S0 * np.exp(np.cumsum((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z, axis=1))
    ST = S[:, -1]
    payoff = np.maximum(ST - K, 0) if option_type == "call" else np.maximum(K - ST, 0)
    return np.exp(-r*T)*np.mean(payoff)

def price_asian_mc(S0, K, r, sigma, T, M, steps, option_type="call"):
    dt = T / steps
    Z = np.random.randn(M, steps)
    S = S0 * np.exp(np.cumsum((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z, axis=1))
    S_avg = np.mean(S, axis=1)
    payoff = np.maximum(S_avg - K, 0) if option_type == "call" else np.maximum(K - S_avg, 0)
    return np.exp(-r*T)*np.mean(payoff)