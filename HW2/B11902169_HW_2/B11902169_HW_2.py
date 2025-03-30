import sys
import numpy as np

if __name__ == '__main__':
    # note
        
    # input
        # S: stock price;
        # X: strike price;
        # r: continuously compounded annual interest rate;
        # s: annual volatility;
        # T: time to maturity in days, which is an integer and also an exercise date;
        # m: number of periods per day for the tree, an integer;
        # E: early exercise dates from now, a list of integers.
    # output
        # prices of the Bermudan put option
        # Bermudan call option
    # Sample 
        # python3 B11902169_HW_2.py 100 110 0.03 0.3 60 5 10 20 30 40 50
        # 11.248139, 1.687963
    
    S, X, r, s, T, m, *E = list(map(float, sys.argv[1:]))
    E = [int(e) for e in E]

    dt = 1 / (m * 365) # time step in years
    u = np.exp(s * np.sqrt(dt)) # up factor
    d = 1 / u # down factor
    p = (np.exp(r * dt) - d) / (u - d) # risk-neutral probability: pSu+(1−p)Sd= RS
    n = int(T * m) # number of time steps

    # Initialize the stock price tree and option price tree
    # Stock price tree
    stock_price_tree = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(i + 1):
            stock_price_tree[j, i] = S * (u ** (i - j)) * (d ** j)
    
    # Option put price tree
    put_tree = np.zeros((n + 1, n + 1))
    # Option call price tree
    call_tree = np.zeros((n + 1, n + 1))

    for i in range(n + 1):
        put_tree[i, n] = max(X - stock_price_tree[i, n], 0)
        call_tree[i, n] = max(stock_price_tree[i, n] - X, 0)
    
    for j in range(n - 1, -1, -1):
        day = int(j / m) + 1
        for i in range(j + 1):
            put_cont = np.exp(-r * dt) * (p * put_tree[i, j + 1] + (1 - p) * put_tree[i + 1, j + 1])
            call_cont = np.exp(-r * dt) * (p * call_tree[i, j + 1] + (1 - p) * call_tree[i + 1, j + 1])
            # Early exercise
            if day in E:
                put_ex = max(X - stock_price_tree[i, j], 0)
                call_ex = max(stock_price_tree[i, j] - X, 0)
            else:
                put_ex = put_cont
                call_ex = call_cont
            put_tree[i, j] = max(put_cont, put_ex)
            call_tree[i, j] = max(call_cont, call_ex)
    
    print(f"{put_tree[0, 0]:.6f}, {call_tree[0, 0]:.6f}")