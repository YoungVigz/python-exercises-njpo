def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(start):
    next_number = start + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

start_value = int(input("Wartość startowa: "))
number_of_primes = int(input("Ilość liczb pierwszych do policzenia: "))

primes = []
for _ in range(number_of_primes):
    start_value = next_prime(start_value)
    primes.append(start_value)

print("Kolejne liczby pierwsze:", primes)
