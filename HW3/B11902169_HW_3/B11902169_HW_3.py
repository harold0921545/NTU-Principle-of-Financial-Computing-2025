import sys
import math
import numpy as np

if __name__ == '__main__':
    # input
        # S: stock price
        # X: strike price
        # r: continuously compounded annual interest rate
        # s: annual volatility
        # T: time to maturity in days, which is an integer, and there are 365 days in a year
        # H: up-and-out barrier, where H > S and H > X
        # n: number of time steps in T, which is an integer
    # output
        # The price of the up-and-out barrier call option.
        # The price of the up-and-out barrier put option.
        # The price of the up-and-in barrier call option.
        # The price of the up-and-in barrier put option.
    # example
        # python3 B11902169_HW_3.py 100 110 0.03 0.3 60 120 100
        # 0.311069, 11.083348, 1.370665, 0.057256
    
    S, X, r, s, T, H, n = map(float, sys.argv[1:])

    T = T / 365
    n = int(n)
    u = math.exp(s * math.sqrt(T / n))
    d = 1 / u
    q = (math.exp(r * (T / n)) - d) / (u - d)
    
    # print(T, n, u, d, q)

    vanilla_call = np.zeros((n + 1, n + 1))
    vanilla_put = np.zeros((n + 1, n + 1))

    for i in range(n + 1):
        for j in range(i + 1):
            vanilla_call[i][j] = max(0, S * (u ** j) * (d ** (i - j)) - X)
            vanilla_put[i][j] = max(0, X - S * (u ** j) * (d ** (i - j)))
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            vanilla_call[i][j] = math.exp(-r * (T / n)) * (q * vanilla_call[i + 1][j + 1] + (1 - q) * vanilla_call[i + 1][j])
            vanilla_put[i][j] = math.exp(-r * (T / n)) * (q * vanilla_put[i + 1][j + 1] + (1 - q) * vanilla_put[i + 1][j])
    vanilla_call_price = vanilla_call[0][0]
    vanilla_put_price = vanilla_put[0][0]

    up_and_out_call = np.zeros((n + 1, n + 1))
    up_and_out_put = np.zeros((n + 1, n + 1))

    for i in range(n + 1):
        for j in range(i + 1):
            up_and_out_call[i][j] = max(0, S * (u ** j) * (d ** (i - j)) - X)
            up_and_out_put[i][j] = max(0, X - S * (u ** j) * (d ** (i - j)))
            if S * (u ** j) * (d ** (i - j)) >= H:
                up_and_out_call[i][j] = 0
                up_and_out_put[i][j] = 0
            
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            up_and_out_call[i][j] = math.exp(-r * (T / n)) * (q * up_and_out_call[i + 1][j + 1] + (1 - q) * up_and_out_call[i + 1][j])
            up_and_out_put[i][j] = math.exp(-r * (T / n)) * (q * up_and_out_put[i + 1][j + 1] + (1 - q) * up_and_out_put[i + 1][j])
    
            if S * (u ** j) * (d ** (i - j)) >= H:
                up_and_out_call[i][j] = 0
                up_and_out_put[i][j] = 0
    
    up_and_out_call_price = up_and_out_call[0][0]
    up_and_out_put_price = up_and_out_put[0][0]
    up_and_in_call_price = vanilla_call_price - up_and_out_call_price
    up_and_in_put_price = vanilla_put_price - up_and_out_put_price
    print(f"{up_and_out_call_price:.6f}, {up_and_out_put_price:.6f}, {up_and_in_call_price:.6f}, {up_and_in_put_price:.6f}")