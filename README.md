# Longstaff Schwartz
A project based on the article "Valuing American Options by Simulation - A Simple Least-Squares Approach". We reproduce the results from the paper.

## Advancement
For now, the project implements a simple version of the Longstaff\& Schwartz Pricer and its finite differences counter part: only non-path dependent markovian options over 1D underlying following a Local Volatility diffusion (i.e $\mathrm{d}X_t = rX_t\mathrm{d}t + \sigma(t, X_t) X_t\mathrm{d}W_t$) can be priced (for instance the American Put).

## To come
For the next version, I plan to enrich the `LocalVolatilityModel` by adding the possibility for the user to calibrate it to Market data. For now, the User has to instantiate the `LocalVolatilityModel` and right away pass it the volatility function $\sigma(t, X_t)$ through its parameter `sigma` (Examples: `sigma = 0.2` for constant volatility or `sigma = lambda t, x: 1/(1 + np.exp(x/40))` for local volatility).
It would be great to also add the calibration possibily into `BlackScholesModel` and `HestonModel`.

Another 'simple' improvement would be to allow deterministic but non-constant interest rate $r(t)$.
