from math import sqrt, log
from random import randint
import time

def slow_select(a, k):
    def count_less(x, a):
        return sum(1 for elem in a if elem < x)

    sequence = [y for y in a if count_less(y, a) <= k]
    return max(sequence) if sequence else None

def select_recursive(a, k, sample_size, delta):
    if len(a) <= sample_size:
        return slow_select(a, k)
    else:
        kth = k * sample_size / len(a)
        sample_indices = [randint(0, len(a) - 1) for _ in range(sample_size)]
        sample = [a[i] for i in sample_indices]
        kmin_select = slow_select(sample, kth - delta)
        kmin = max(0, kmin_select) if kmin_select is not None else 0  # Aseguramos que kmin_select no sea None
        kmax_select = slow_select(sample, kth + delta)
        kmax = min(max(a), kmax_select) if kmax_select is not None else max(a)  # Aseguramos que kmax_select no sea None
        offset = sum(1 for e in a if e < kmin)
        new_a = [e for e in a if kmin <= e <= kmax]

        if k < offset or k >= offset + len(new_a):
            return select_recursive(a, k, sample_size, delta)
        else:
            return select_recursive(new_a, k - offset, sample_size, delta)

def sample_select(a, k):
    sample_size = int(0.5 * sqrt(len(a)))
    delta = 0.5 * sqrt(sample_size * log(sample_size))
    return select_recursive(a, k, round(sample_size), round(delta))

# Generamos un array de 100000000 elementos con números aleatorios entre 1 y 100000000
a = [randint(1, 100000000) for _ in range(100000000)]

# Medimos el tiempo de inicio
start_time = time.time()

# Ejecutamos la función
result = sample_select(a, 10)

# Medimos el tiempo de finalización
end_time = time.time()

# Imprimimos el resultado y el tiempo de ejecución
print(a)
print("El resultado es:", result)
print("El tiempo de ejecución fue:", end_time - start_time, "segundos")
