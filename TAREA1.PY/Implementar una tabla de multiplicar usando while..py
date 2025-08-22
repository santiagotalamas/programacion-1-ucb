def tabla_multiplicar(numero):
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

numero_tabla = int(input("Ingresa el número para la tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)
