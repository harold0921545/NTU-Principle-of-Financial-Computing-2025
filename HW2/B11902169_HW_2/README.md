# README
## Overview

This code calculates the prices of Bermudan call and put options using a binomial tree model, accounting for the possibility of early exercise at specified dates.

## Input Parameters

The program expects the following command-line arguments:

- S: stock price
- X: strike price
- r: continuously compounded annual interest rate
- s: annual volatility
- T: time to maturity in days, which is an integer and also an exercise date
- m: number of periods per day for the tree, an integer
- E: early exercise dates from now, a list of integers

## Output

After running the script, the prices of the Bermudan put and call options will be printed with six decimal places.

## Dependencies

- Python 3.x
- NumPy library

### Example:
For the command:

```bash
python3 B11902169_HW_2.py 100 110 0.03 0.3 60 5 10 20 30 40 50
```

The output might look like:

```
11.248121, 1.687963
```
