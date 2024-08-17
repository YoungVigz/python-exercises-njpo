# Przykład zrealizowany dla ciągu Tetranacciego gdzie w przeciwieństwie do ciągu Fibonacciego sumujemy poprzednie 4 wyrazy a nie 2 
# co zwiększa ilość obliczeń dla tej samej liczby iteracji (w porównaniu do ciągu Fib)

import time
from functools import lru_cache

def tetranacci_without_cache(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return (tetranacci_without_cache(n-1) + tetranacci_without_cache(n-2) +
                tetranacci_without_cache(n-3) + tetranacci_without_cache(n-4))

@lru_cache(maxsize=None)
def tetranacci_cache(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return (tetranacci_cache(n-1) + tetranacci_cache(n-2) +
                tetranacci_cache(n-3) + tetranacci_cache(n-4))

def benchmark(n):

    start = time.time()
    result_no_cache = tetranacci_without_cache(n)
    time_no_cache = time.time() - start
    
    start = time.time()
    result_cache = tetranacci_cache(n)
    time_cache = time.time() - start
    
    return result_no_cache, time_no_cache, result_cache, time_cache

n = 50  
result_no_cache, time_no_cache, result_cache, time_cache = benchmark(n)

print(f"Tetranacci({n}) bez pamięci podręcznej: {result_no_cache}, czas: {time_no_cache:.6f}s")
print(f"Tetranacci({n}) z pamięcią podręczną: {result_cache}, czas: {time_cache:.6f}s")
