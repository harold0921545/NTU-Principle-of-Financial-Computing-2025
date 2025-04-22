# README

## Overview
This code calculates the prices of up-and-out and up-and-in European barrier options (call and put) using a binomial tree model. Up-and-in options are computed using parity: vanilla - up-and-out.

## Input Parameters
The program expects the following command-line arguments:

- `S`: stock price
- `X`: strike price
- `r`: continuously compounded annual interest rate
- `s`: annual volatility
- `T`: time to maturity in days, which is an integer
- `H`: up-and-out barrier (H > S and H > X)
- `n`: number of time steps in T, an integer

## Output
After running the script, the prices of the up-and-out call, up-and-out put, up-and-in call, and up-and-in put options will be printed with six decimal places.

## Dependencies
- Python 3.x
- NumPy library

## Example
```bash
python3 B11902169_HW_3.py 100 110 0.03 0.3 60 120 100
```

**Output:**
```
0.311069, 11.083348, 1.370665, 0.057256
```
