def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_primos():
    suma = 0
    for i in range(1, 101):
        if es_primo(i):
            suma += i
    return suma

print(f"La suma de los números primos entre 1 y 100 es: {suma_primos()}")
