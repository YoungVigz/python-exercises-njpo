import random

def estimate_pi(sample_size):
    circle_points_sum = 0

    for _ in range(sample_size):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            circle_points_sum += 1

    return 4 * circle_points_sum / sample_size

sample_size = int(input("Podaj liczbę powtórzeń dla estymacji liczby pi: "))
pi_estimate = estimate_pi(sample_size)
print("Szacowana wartość liczby pi:", pi_estimate)
