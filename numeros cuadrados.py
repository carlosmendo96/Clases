#Programa que da numeros cuadrados del 1 al 20
n = int(input("Escoge un número del 1 al 20 \n"))
if (n <= 20 and n >= 1):
    for i in range(0, n):
        print(i ** 2)
else:
    print("No es un número entre el 1 y 20")