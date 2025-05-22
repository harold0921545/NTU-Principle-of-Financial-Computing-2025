import sys
import math
import numpy as np

def _terminal_payoff_with_barrier(S_val, X_strike, is_call_opt, L_barrier, H_barrier): # Strict inequality for barriers
    if not (L_barrier < S_val < H_barrier):
        return 0
    if is_call_opt:
        return max(0, S_val - X_strike)
    else:
        return max(0, X_strike - S_val)

def calculate_double_barrier_option(S, X, r, sigma, T_days, H, L, k_param, is_call):
    T = T_days / 365

    dx = math.log(H / L) / (2 * k_param)
    dt_binomial = (dx / sigma) ** 2

    u = math.exp(dx)
    d = 1 / u

    p_binom = (math.exp(r * dt_binomial) - d) / (u - d)
    disc_binom = math.exp(-r * dt_binomial)
    levels = 2 * k_param + 1

    N_binom = int(T/ dt_binomial) - 1
    dt_trinomial = T - N_binom * dt_binomial

    V_binom = np.zeros((N_binom + 1, levels))

    for j in range(levels):
        S_T = L * (u ** j)
        V_binom[N_binom, j] = _terminal_payoff_with_barrier(S_T, X, is_call, L, H)

    for i in range(N_binom - 1, -1, -1):
        V_binom[i, 0] = V_binom[i, levels - 1] = 0
        for j in range(1, levels - 1):
            V_binom[i, j] = disc_binom * (p_binom * V_binom[i + 1, j + 1] + (1 - p_binom) * V_binom[i + 1, j - 1])
    
    grid_at_dt_trinomial = V_binom[0, :]
    mu_drift_annualized = r - 0.5 * (sigma ** 2)
    mu_expected_log = mu_drift_annualized * dt_trinomial
    var_log = (sigma ** 2) * dt_trinomial
    
    k_const = 2 * dx

    j_B_float = (mu_expected_log - math.log(L / S)) / dx
    j_B = int(round(j_B_float))
    j_B = max(0, min(levels - 1, j_B))

    S_b = L * (u ** j_B)
    mu_hat_actual_log = math.log(S_b / S) if S > 0 else 0

    beta = mu_hat_actual_log - mu_expected_log
    alpha = beta + k_const
    gamma = beta - k_const

    den_pu_pd = 2 * k_const ** 2
    den_pm = -k_const ** 2

    pu = (var_log + beta * gamma) / den_pu_pd
    pm = (var_log + alpha * gamma) / den_pm
    pd = 1.0 - pu - pm

    val_B = grid_at_dt_trinomial[j_B]

    idx_A = j_B + 2
    val_A = grid_at_dt_trinomial[idx_A] if 0 <= idx_A < levels else 0.0

    idx_C = j_B - 2
    val_C = grid_at_dt_trinomial[idx_C] if 0 <= idx_C < levels else 0.0

    price = math.exp(-r * dt_trinomial) * (pu * val_A + pm * val_B + pd * val_C)
    return price

if __name__ == '__main__':
        # input
        # S: stock price;
        # X: strike price;
        # r: continuously compounded annual interest rate;
        # s: annual volatility;
        # T: time to maturity in days, which is an integer, and there are 365 days in a year;
        # H: up-and-out barrier, where H > S and H > X;
        # L: down-and-out barrier, where L < S and L < X;
        # k: 2k represents the number of up steps from L to H, and is an integer as shown on page 776 of the course slides.
    # output
        # The price of the double-barrier barrier call option.
        # The delta of the double-barrier barrier call option (caluclated by S × 1.01 and S × 0.99).
        # The price of the double-barrier barrier put option.
        # The delta of the double-barrier barrier put option (caluclated by S × 1.01 and S × 0.99).
    # example
        # S = 95, X = 100, r = 0.10, s = 0.25, T = 365, H = 140, L = 90, and k = 50
        # 1.457183, 0.253302, 0.040884, 0.007052
        
    S_in, X_in, r_in, sigma_in, T_days_in, H_in, L_in, k_in = sys.argv[1:]
    S, X, r, sigma, T_days, H, L, k_param = float(S_in), float(X_in), float(r_in), float(sigma_in), int(T_days_in), float(H_in), float(L_in), int(k_in)

    c0 = calculate_double_barrier_option(S, X, r, sigma, T_days, H, L, k_param, True)
    c_up = calculate_double_barrier_option(S * 1.01, X, r, sigma, T_days, H, L, k_param, True)
    c_down = calculate_double_barrier_option(S * 0.99, X, r, sigma, T_days, H, L, k_param, True)
    delta_c = (c_up - c_down) / (S * 0.02)

    p0 = calculate_double_barrier_option(S, X, r, sigma, T_days, H, L, k_param, False)
    p_up = calculate_double_barrier_option(S * 1.01, X, r, sigma, T_days, H, L, k_param, False)
    p_down = calculate_double_barrier_option(S * 0.99, X, r, sigma, T_days, H, L, k_param, False)
    delta_p = (p_up - p_down) / (S * 0.02)
    
    print(f"{c0:.6f}, {delta_c:.6f}, {p0:.6f}, {delta_p:.6f}")