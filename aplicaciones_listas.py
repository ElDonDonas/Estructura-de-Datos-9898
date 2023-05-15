# Pedimos al usuario que ingrese una lista de números separados por comas
numeros_str = input("Ingresa una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números
numeros = [float(x) for x in numeros_str.split(",")]

# Calculamos el promedio de los números en la lista
promedio = sum(numeros) / len(numeros)

# Mostramos el promedio en pantalla
print("El promedio es:", promedio)
