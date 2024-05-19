# Longstaff Schwartz
A project based on the article "Valuing American Options by Simulation - A Simple Least-Squares Approach". We reproduce the results from the paper.

## Advancement
For now, the project implements the simplest version of the Longstaff Pricer and its finite differences counter part: only non-path dependent markovian options over 1D underlying following a Black Scholes diffusion (i.e $\mathrm{d}X_t = rX_t\mathrm{d}t + \sigma X_t\mathrm{d}W_t$) can be priced (for instance the American Put).

## To come
For the next version, I plan to allow other diffusion (especially local volatility model $\mathrm{d}X_t = rX_t \mathrm{d}t + \sigma(t, X_t)\mathrm{d}W_t$) both for the Finite Differences Pricer and the L\&S pricer. For that purpose, it will be necessary to add a class `LocalVolatilityModel` in `diffusion.py` and change the `FiniteDifferencesPricer` in `FiniteDifferences.ipynb`. Also, I will have to update the report accordingly.
