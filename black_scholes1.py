import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


S = float(input("Enter the current stock price (S₀): "))

K = float(input("Enter the strike price (K): "))

r = float(input("Enter the risk-free interest rate (r) [as a decimal, e.g. 0.05 for 5%]: "))

T = float(input("Enter the time to maturity (T in years): "))


sigma = float((input("Enter the volatility (σ) [as a decimal, e.g. 0.2 for 20%]: ")))


e = math.e

d1_bottom = sigma * math.sqrt(T)
x = S / K
d1_top = (T * (r + (0.5 * (sigma ** 2)))) + (math.log(x))
d1 = (d1_top) / (d1_bottom)

d2 = (d1) - d1_bottom

N_call1 = norm.cdf(d1)
N_call2 = norm.cdf(d2)

N_put1 = norm.cdf((-1) * d2)
N_put2 = norm.cdf((-1)* d1)

call_calc = (S * N_call1) - K * (math.exp((-1 * r) * T)) * N_call2

put_calc = (K * (math.exp((-1 * r) * T)) * N_put1) - (S * N_put2)

delta_call = norm.cdf(d1)
delta_put = norm.cdf(d1)-1

gamma_call = norm.pdf(d1) / (S * sigma * math.sqrt(T))
gamma_put = norm.pdf(d1) / (S * sigma * math.sqrt(T))

vega = (S * norm.pdf(d1) * math.sqrt(T)) / 100

theta_call = -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) - r * K * math.exp(-r*T) * norm.cdf(d2)
theta_put = -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) + r * K * math.exp(-r*T) * norm.cdf(-d2)

option_type = input("do you have a call or put option? ").lower()

if option_type == "call" :
    print("the fair price for your option is " + str(call_calc))
    print("the delta is " + str(delta_call))
    print("the gamma is "+ str(gamma_call))
    print("the vega is " + str(vega))
    print("the theta is " + str(theta_call))
   
if option_type == "put" :
    print("the fair price for your option is " + str(put_calc))
    print("the delta is " + str(delta_put))
    print("the gamma is "+ str(gamma_call))
    print("the vega is " + str(vega))
    print("the theta is " + str(theta_put))

stock_prices = np.linspace(S * 0.5, S * 1.5, 200)

call_payoffs = np.maximum(stock_prices - K, 0)
put_payoffs = np.maximum(K - stock_prices, 0)

plt.plot(stock_prices, call_payoffs, label="Call Payoff")
plt.plot(stock_prices, put_payoffs, label="Put Payoff")
plt.axvline(x=K, color='gray', linestyle='--', label="Strike Price")
plt.xlabel("Stock Price at Expiry")
plt.ylabel("Payoff")
plt.title("Option Payoff Diagram")
plt.legend()
plt.show()