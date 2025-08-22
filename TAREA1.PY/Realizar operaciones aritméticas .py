def operaciones_basicas_binario(num1, num2):
    suma = bin(num1 + num2)[2:]
    resta = bin(num1 - num2)[2:]
    multiplicacion = bin(num1 * num2)[2:]
    division = bin(num1 // num2)[2:]  # División entera
    
    return suma, resta, multiplicacion, division

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas_binario(numero1, numero2)

print(f"Suma (binario): {suma}")
print(f"Resta (binario): {resta}")
print(f"Multiplicación (binario): {multiplicacion}")
print(f"División (binario): {division}")
