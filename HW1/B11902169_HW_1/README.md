# README

## Overview
This code calculates the maximum loan amount (V1) that can be applied for with balanced payments, based on the given parameters. It also computes the total interest paid on the loan, total interest received from the bond, and the annualized internal rate of return (IRR) of the investment.

## Input Parameters
The code requires five command-line arguments:
1. `C` - Initial cash available
2. `n` - Loan and bond maturity time (in years, integer)
3. `m` - Number of payments per year (integer)
4. `r1` - Annual interest rate of the loan (compounded `m` times per year)
5. `r2` - Annual interest rate of the bond (compounded `m` times per year)

## Output
The code prints the following values:
1. Maximum loan amount (`V1`)
2. Total interest paid on the loan (rounded to six decimal places)
3. Total interest received from the bond (rounded to six decimal places)
4. Annualized IRR of the investment (rounded to six decimal places)

## How to Run
Execute the code using Python with command-line arguments. Example:
```sh
python3 B11902169_HW_1.py 10000 2 12 0.018 0.045
```
This example sets `C = 10000`, `n = 2`, `m = 12`, `r1 = 0.018`, and `r2 = 0.045`.

## Dependencies
- Python 3
- SciPy (`pip install scipy`)

## Notes
- The code uses a binary search to determine the maximum loan amount (`V1`).
- Newton's method is used to find the IRR.
- If IRR computation fails, `nan` is returned.

