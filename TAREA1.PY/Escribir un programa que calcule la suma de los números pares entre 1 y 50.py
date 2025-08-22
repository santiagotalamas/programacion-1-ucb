def suma_pares():
    suma = 0
    for i in range(1, 51):
        if i % 2 == 0:
            suma += i
    return suma

print(f"La suma de los números pares entre 1 y 50 es: {suma_pares()}")
