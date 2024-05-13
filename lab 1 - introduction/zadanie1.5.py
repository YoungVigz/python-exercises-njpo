import time

def fibonacci(n):
    if n <= 1:
        return n
    fib_prev = 0
    fib_curr = 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_curr

start_time = time.time()
n = 93
result = fibonacci(n)
end_time = time.time()

elapsed_time = end_time - start_time

print("Dla elementu", n, "ciągu Fibonacciego wartość wynosi:", result)
print("Wartość obliczono w czasie: ", elapsed_time)
