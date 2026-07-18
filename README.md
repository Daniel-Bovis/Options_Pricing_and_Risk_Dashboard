# Options Pricing & Risk Dashboard

A Python tool that prices European call and put options using the Black-Scholes model, calculates the four primary Greeks, and plots expiry payoff diagrams.

## What it does

- Calculates fair value for European call and put options based on user inputs (spot price, strike, volatility, time to maturity, risk-free rate)
- Implements the four primary Greeks (Delta, Gamma, Vega, Theta) to quantify sensitivity to underlying price, volatility, and time decay
- Plots payoff diagrams at expiry across a range of stock prices, distinguishing time-value-adjusted fair pricing from terminal payoff outcomes
- Demonstrates how interest rates affect delta skew and the differing decay profiles of calls versus puts

## Libraries

- 'numpy'
- 'scipy'
- 'matplotlib'

# yield curve analyser

"Pulls live US Treasury yield data across five maturities via the FRED API. Plots the yield curve for any historical date and automatically flags 2y10y inversions.

## What it does

- Pulls live US Treasury yield data across five maturities (3-month to 30-year) via the FRED API
- Processes and cleans time-series data using Pandas
- Plots the yield curve for any user-specified historical date, visualising shifts in the term structure over time
- Calculates the 2y10y spread and automatically flags yield curve inversions, a key recession indicator watched closely by macro and rates desks

## Libraries

- 'pandas'
- 'requests'
- 'matplotlib'

# Portfolio Risk Analyser

Calculates 1-day 95% Value at Risk (VaR) for any stock using historical simulation. Pulls live price data via Yahoo Finance and visualises the return distribution.

## What it does

-	Built a Value at Risk (VaR) tool that pulls live historical price data via the Yahoo Finance API and calculates 1-day 95% VaR using historical simulation
-Computed daily returns using percentage change analysis across user-defined date ranges, applying NumPy's percentile function to identify the 5th percentile loss threshold
-	Visualised the full return distribution as a histogram with the VaR threshold marked, demonstrating awareness of fat tail risk and the limitations of normal distribution assumptions

## Libraries

- 'numpy'
- 'pandas'
- 'matplotlib'
- 'yfinance'
