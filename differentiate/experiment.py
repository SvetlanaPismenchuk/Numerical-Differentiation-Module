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

plt.figure()

plt.plot(hlist, forward_error, label="Forward Difference")
plt.plot(hlist, backward_error, label="Backward Difference")
plt.plot(hlist, central_error, label="Central Difference")
plt.plot(hlist, five_point_error, label="Five-Point Difference")

plt.title("Numerical Differentiation Errors vs Step Size")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")

plt.legend()

# Reverse x-axis, step size decreases left to right
plt.xlim(0.5, 0.005)

plt.show()


plt.figure()

plt.plot(hlist, central_error, label="Central Difference")
plt.plot(hlist, five_point_error, label="Five-Point Difference")

plt.title("Central vs Five-Point Error")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")

plt.legend()
plt.xlim(0.5, 0.005)

plt.show()

input()
