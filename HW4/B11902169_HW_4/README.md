# README

## Overview
This program prices a European double-barrier option (both call and put) using a binomial-trinomial tree model. 

## Input Parameters
The program expects the following command-line arguments in order:

1.  `S`: Current stock price (float).
2.  `X`: Strike price of the option (float).
3.  `r`: Continuously compounded annual risk-free interest rate (float, e.g., 0.05 for 5%).
4.  `sigma`: Annual volatility of the stock price (float, e.g., 0.2 for 20%).
5.  `T_days`: Time to maturity in days (integer).
6.  `H`: Upper barrier level (float, must be greater than `S` and `X`).
7.  `L`: Lower barrier level (float, must be less than `S` and `X`).
8.  `k`: An integer parameter. The term `2k` represents the number of discrete upward price steps in the logarithm of the stock price from the lower barrier `L` to the upper barrier `H`. This defines the granularity of the price grid.

## Output
The script will print a single line to standard output containing four comma-separated values, each formatted to six decimal places:

1.  Price of the double-barrier call option.
2.  Delta of the double-barrier call option.
3.  Price of the double-barrier put option.
4.  Delta of the double-barrier put option.

## Dependencies
*   Python 3.x
*   NumPy library

To install NumPy, you can use pip:
```bash
pip install numpy
```

## Example
To run the script with the example parameters:
`S = 95`, `X = 100`, `r = 0.10`, `sigma = 0.25`, `T_days = 365`, `H = 140`, `L = 90`, `k = 50`

Execute the following command in your terminal:
```bash
python3 B11902169_HW_4.py 95 100 0.10 0.25 365 140 90 50
```

Expected Output:
```
1.457183, 0.253302, 0.040884, 0.007052
```