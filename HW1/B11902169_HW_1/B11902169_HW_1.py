import sys
import math


if __name__ == '__main__':
    # note
        # level coupon bond
    # input
        # C: cash in TA's hand;
        # n: time to maturity of the loan and bond in years, an integer
        # m: the number of payments per annum, an integer
        # r1: annual interest rate of the loan, compounded m times per year
        # r2: annual interest rate of the bond, compounded m times per year

    # output
        # The maximum loan amount (V1, an integer) that TA can apply for balanced payments (the following outputs are with V1 of the maximum loan amount);
        # Total interest paid on the loan (rounded to six decimal places);
        # Total interest received from the bond (rounded to six decimal places);
        # Annualized internal rate of return of the investment (rounded to six decimal places).
    
    # V1: loan value (integer)
    # V2: bond value (integer)
    # V1 + C = V2
    # example: C = 10000, n = 2, m = 12, r1 = 0.018, r2 = 0.045
    # output: 968, 18.254282, 987.120000, 0.046329

    C, n, m, r1, r2 = map(float, sys.argv[1:])
    n, m =  int(n), int(m)
    
    V1 = 0
    while True:
        V1 += 1
        V2 = C + V1
        
        loan_regular_payment = V1 * (r1 / m) / (1 - (1 + r1 / m) ** (-n * m))
        bond_interest = V2 * (r2 / m)

        if loan_regular_payment > bond_interest:
            break
    V1 -= 1
    V2 = C + V1
    loan_regular_payment = V1 * (r1 / m) / (1 - (1 + r1 / m) ** (-n * m))
    bond_interest = V2 * (r2 / m)
    
    loan_total_interest = loan_regular_payment * n * m - V1

    cash_flow = [-V2] + [bond_interest - loan_regular_payment] * (n * m - 1) + [bond_interest - loan_regular_payment + V2]
    print(cash_flow)
    

    print(f"{V1}, {loan_total_interest:.6f}, {bond_interest * n * m:.6f}, {irr * m:.6f}")
