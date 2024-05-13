import time

def measure_time(n):
    start_time = time.time()
    array = []
    for i in range(n):
        array.append(i)
    end_time = time.time()
    return end_time - start_time

n = 1000000
execution_time = measure_time(n)
print(f"Czas dodawania {n} elementów do tablicy: {execution_time} sekund.")