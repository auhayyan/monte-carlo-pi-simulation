import random
import time

def est_pi(n_samples):
    inside = 0

    for _ in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside += 1

    pi_est = 4 * inside / n_samples
    return pi_est
    

start = time.time()
samples = 10000000
pi_val = est_pi(samples)
end = time.time()
inside = pi_val / 4 * samples
print(f"samples: {samples}")
print(f"estimated π: {pi_val}")
print(f"inside: {inside}")
print(f"time taken: {end - start:.4f} seconds")