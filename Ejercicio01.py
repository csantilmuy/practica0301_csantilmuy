# Escribir dos funciones, una función que reciba un número entero positivo n y
# calcule el número de fibonacci asociado a ese número de manera recursiva y
# otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de ejecución para
# n = (1, 10, 20, 30 y 40) por fuerza bruta.
import time
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
def fibonacci_bucle(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
valores_n = [1, 10, 20, 30, 40]
resultados = []
for n in valores_n:
    inicio_recursivo = time.time()
    fibonacci_recursivo(n)
    fin_recursivo = time.time()
    tiempo_recursivo = fin_recursivo - inicio_recursivo
    inicio_bucle = time.time()
    fibonacci_bucle(n)
    fin_bucle = time.time()
    tiempo_bucle = fin_bucle - inicio_bucle
    resultados.append((n, tiempo_recursivo, tiempo_bucle))
print(f"{'n':<10}{'tiempo ejecución (recursivo)':<30}{'tiempo ejecución (bucles)':<30}")
for n, t_rec, t_buc in resultados:
    print(f"{n:<10}{t_rec:<30}{t_buc:<30}")