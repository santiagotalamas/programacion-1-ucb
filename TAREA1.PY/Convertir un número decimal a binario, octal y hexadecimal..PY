def convertir_numero(numero):
    binario = bin(numero)[2:]
    octal = oct(numero)[2:]
    hexadecimal = hex(numero)[2:]
    
    return binario, octal, hexadecimal

numero = int(input("Ingresa un número decimal: "))
binario, octal, hexadecimal = convertir_numero(numero)
print(f"Binario: {binario}, Octal: {octal}, Hexadecimal: {hexadecimal}")
