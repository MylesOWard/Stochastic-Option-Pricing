from setuptools import setup, find_packages

setup(
    name="montecarlo_var",
    version="0.1.0",
    description="A Python toolkit for Monte Carlo Value-at-Risk (VaR) and Expected Shortfall estimation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/<your-username>/monte-carlo-var",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scipy>=1.7.0",
        "yfinance>=0.2.0"
    ],
    python_requires=">=3.8",
)
