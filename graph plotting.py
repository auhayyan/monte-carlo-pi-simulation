import matplotlib.pyplot as plt
import numpy as np

# Your data
N = [1000, 10000, 100000, 1000000, 10000000]

pi_vals = [
    np.mean([3.076,3.232,3.092,3.216,3.092]),
    np.mean([3.1456,3.1532,3.1252,3.1288,3.1068]),
    np.mean([3.13912,3.14208,3.13796,3.14608,3.1452]),
    np.mean([3.144476,3.1434,3.138392,3.140132,3.143648]),
    np.mean([3.141058,3.140648,3.1413376,3.1416844,3.1412812])
]

# True value
true_pi = np.pi

# Error
errors = [abs(p - true_pi) for p in pi_vals]

# Time (your averages)
times = [0.0015, 0.015, 0.15, 1.1, 7.5]

# ---- GRAPH 1 ----
plt.figure()
plt.plot(N, pi_vals, marker='o')
plt.xscale('log')
plt.title("Pi Estimate vs Sample Size")
plt.xlabel("N")
plt.ylabel("Estimated Pi")
plt.savefig("pi estimate vs sample size.png")

# ---- GRAPH 2 ----
plt.figure()
plt.plot(N, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.title("Error vs Sample Size")
plt.xlabel("N")
plt.ylabel("Error")
plt.savefig("error vs sample size.png")

# ---- GRAPH 3 ----
plt.figure()
plt.plot(N, times, marker='o')
plt.xscale('log')
plt.title("Time vs Sample Size")
plt.xlabel("N")
plt.ylabel("Time (s)")
plt.savefig("time vs sample size.png")

plt.show()