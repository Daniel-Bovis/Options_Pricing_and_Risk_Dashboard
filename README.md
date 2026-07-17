# Options Pricing & Risk Dashboard

A Python tool that prices European call and put options using the Black-Scholes model, calculates the four primary Greeks, and plots expiry payoff diagrams.

## What it does

- Calculates fair value for European call and put options based on user inputs (spot price, strike, volatility, time to maturity, risk-free rate)
- Implements the four primary Greeks (Delta, Gamma, Vega, Theta) to quantify sensitivity to underlying price, volatility, and time decay
- Plots payoff diagrams at expiry across a range of stock prices, distinguishing time-value-adjusted fair pricing from terminal payoff outcomes
- Demonstrates how interest rates affect delta skew and the differing decay profiles of calls versus puts

## Libraries

- `numpy`
- `scipy`
- `matplotlib`
