# goit-algo-hw-10


# Monte Carlo Integration vs SciPy quad — Conclusion

### Observed Results:

| Number of Samples | Monte Carlo Result | SciPy quad Result |
|-------------------|--------------------|-------------------|
| 100               | 2.32               | 2.66667           |
| 1000              | 2.608              | 2.66667           |
| 10000             | 2.6528              | 2.66667           |
| 100000            | 2.67336             | 2.66667           |

### Analysis:

- The **Monte Carlo method** provides an approximate result that improves as the number of samples increases.
- At 100 samples the error is quite large, but at 100,000 samples the result is very close to the reference value (error < 0.3%).
- The **SciPy quad** function gives the exact (analytical) result for this integral.

### Conclusion:

- The implemented Monte Carlo algorithm works correctly and demonstrates **convergence toward the true value** as the number of points increases.
- Monte Carlo is suitable when analytical solutions are hard or impossible to obtain, but for simple integrals (like this one) `quad` is clearly more precise and efficient.
- The accuracy of Monte Carlo depends strongly on the number of samples (O(1/√n)).

---
