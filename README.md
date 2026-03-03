# Numerical Differentiation Module (Week 6)

## Differentiate module (differentiate.py)

This repo contains a small Python module called differentiate.py that approximates derivatives using numerical differentiation.

The module includes four internal helper methods:
- _forward_diff
- _backward_diff
- _central_diff
- _five_point_diff

You should not call those helper functions directly. Instead, use the public function diff(), which selects a method using the mode argument:
- mode = 0: forward difference
- mode = 1: backward difference
- mode = 2: central difference
- mode = 3: five-point central difference

In `experiment.py`, the test function is:

- `g(x) = x^2 ln(x)`
- center point `a = 2`
- exact derivative at `a = 2` is stored as `gprime = 2 + 4 ln(2)`

Then the script creates a list of step sizes `hlist` and computes absolute errors for each mode:

```python
import numpy as np
import matplotlib.pyplot as plt
from differentiate import diff

def g(x):
    return (x**2 * np.log(x))

a = 2
gprime = 2 + 4 * np.log(2)

hlist = np.linspace(0.005, 0.5, 100)

forward_error = np.abs([diff(g, a, h=h, mode=0) for h in hlist] - gprime)
backward_error = np.abs([diff(g, a, h=h, mode=2) for h in hlist] - gprime)
central_error = np.abs([diff(g, a, h=h, mode=1) for h in hlist] - gprime)
five_point_error = np.abs([diff(g, a, h=h, mode=3) for h in hlist] - gprime)
```

What the plots show

The experiment produces two plots:

# All methods vs step size

Forward, Backward, Central, and Five-Point error curves are plotted on the same figure.

The x-axis is reversed, so smaller step sizes appear to the right.

# Central vs Five-Point

Only Central and Five-Point errors are plotted to compare the two most accurate methods.

These plots show how the numerical derivative accuracy changes depending on both the method (mode) and the chosen step size h.

# Acknowledgements
I'd like to acknowledge Dr.Rumpf for his guidance that led me to complete this assignment, and ChatGPT for correcting syntax issues, code, and deepening my understanding of the code.
