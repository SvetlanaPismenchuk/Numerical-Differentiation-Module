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

Example usage:

```python
import numpy as np
from differentiate import diff

def f(x):
    return x**2
diff(f, x0, h, mode)

```
