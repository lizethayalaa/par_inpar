# Programa para determinar si un numero es par impar

# input
x = int(input("ingresa un numero: "))

# processing
r = x%2

# output
if r % 2 == 0:
    msj = "par "
else:
    msj = "impar "

print("El numero " + str(x) + " es " + msj)