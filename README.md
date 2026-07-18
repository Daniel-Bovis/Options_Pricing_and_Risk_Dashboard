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
