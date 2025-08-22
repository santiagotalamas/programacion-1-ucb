def hex_a_bin(hexadecimal):
    decimal = int(hexadecimal, 16)
    return bin(decimal)[2:]

def bin_a_hex(binario):
    decimal = int(binario, 2)
    return hex(decimal)[2:]

# Ejemplo de uso
hexadecimal = input("Ingresa un número hexadecimal: ")
binario = input("Ingresa un número binario: ")

print(f"Hexadecimal a Binario: {hex_a_bin(hexadecimal)}")
print(f"Binario a Hexadecimal: {bin_a_hex(binario)}")
