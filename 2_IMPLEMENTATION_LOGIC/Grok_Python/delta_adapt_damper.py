# delta_adapt_damper.py (Delta_Adapt Logic - Rate Control)

def apply_damping(solution_candidate, k_star_variance, max_rate_r):
    """
    Applies non-destructive rate control and filters noise using dynamic epsilon.
    """
    # 1. Calculate Dynamic Hysteresis (Epsilon)
    # Epsilon (ε) increases when K* variance is high (high panic/noise).
    epsilon_base = 0.05
    epsilon_boost = 0.1 * k_star_variance
    dynamic_epsilon = epsilon_base + epsilon_boost

    # 2. Apply Rate Limit (r_max)
    # Prevents solution from changing P distribution too quickly.
    damped_solution = limit_rate(solution_candidate, max_rate_r)
    
    # 3. Apply Hysteresis Filter
    if solution_candidate.change_magnitude() < dynamic_epsilon:
        return 'Noise_Filtered_Hold_Current_State'
    else:
        return damped_solution