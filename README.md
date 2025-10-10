# Stochastic-Option-Pricing

### Quantitative Derivatives Modelling with Python

This repository implements and compares stochastic models for option pricing, ranging from the analytical Black–Scholes framework to Monte Carlo simulation and stochastic volatility models such as Heston.  

It’s structured as a modular, research-style toolkit with all core implementations located in `src/`, accompanied by polished Jupyter notebooks that demonstrate the mathematics, numerical methods, and empirical behaviour of each pricing model.  

---

## Project Overview

Option pricing seeks to model the fair value of derivatives under uncertain future asset prices.  
This repository explores a progression from analytical solutions to stochastic simulation and model comparison.

| Method | Description | Pros | Cons |
|:--|:--|:--|:--|
| **Black–Scholes (Analytical)** | Closed-form pricing under Geometric Brownian Motion | Fast, interpretable | Assumes constant volatility |
| **Heston Model (Stochastic Volatility)** | Volatility follows its own stochastic process | Captures volatility clustering | No closed form; complex calibration |
| **Monte Carlo Simulation** | Simulates many price paths under stochastic dynamics | Flexible, model-agnostic | Computationally expensive |
| **Variance Reduction** | Techniques to improve simulation efficiency | Increases accuracy | Requires additional implementation |
| **Model Comparison** | Evaluates pricing accuracy vs. analytical benchmarks | End-to-end validation | Computational overhead |

Each model is derived mathematically and implemented in Python, with side-by-side comparisons and visual diagnostics.

---

## Notebook Series

All notebooks include inline visualisations, derivations, and validation plots.

| # | Notebook | Focus |
|:--|:--|:--|
| 01 | [`01_black_scholes_pricing.ipynb`](notebooks/01_black_scholes_pricing.ipynb) | Derivation and implementation of the analytical Black–Scholes model |
| 02 | [`02_heston_model.ipynb`](notebooks/02_heston_model.ipynb) | Stochastic volatility and the Heston model simulation |
| 03 | [`03_monte_carlo_pricing.ipynb`](notebooks/03_monte_carlo_pricing.ipynb) | Monte Carlo pricing for European options |
| 04 | [`04_variance_reduction.ipynb`](notebooks/04_variance_reduction.ipynb) | Variance reduction methods: antithetic variates & control variates |
| 05 | [`05_model_comparison.ipynb`](notebooks/05_model_comparison.ipynb) | Comparative study of pricing methods and convergence results |
