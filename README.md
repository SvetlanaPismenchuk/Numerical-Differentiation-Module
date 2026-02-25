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
- mode = 2: central difference (default)
- mode = 3: five-point central difference

Example usage:

```python
import numpy as np
import differentiate

def f(x):
    return x**2

x0 = 3.0

# default: central difference
approx = differentiate.diff(f, x0)
print(approx)

# forward difference
approx_fwd = differentiate.diff(f, x0, h=0.01, mode=0)
print(approx_fwd)

# five-point difference
approx_five = differentiate.diff(f, x0, h=0.01, mode=3)
print(approx_five)
