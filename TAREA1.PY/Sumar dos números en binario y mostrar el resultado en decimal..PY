def suma_binarios(bin1, bin2):
    decimal1 = int(bin1, 2)
    decimal2 = int(bin2, 2)
    suma_decimal = decimal1 + decimal2
    return suma_decimal

binario1 = input("Ingresa el primer número binario: ")
binario2 = input("Ingresa el segundo número binario: ")

resultado = suma_binarios(binario1, binario2)
print(f"La suma en decimal es: {resultado}")
