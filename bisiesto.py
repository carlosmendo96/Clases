#Programa que te dice si el año es bisiesto del año 1900 al 100,000
n = int(input("Coloca el año que quieres saber \n"))
if n >= 1900 and n <= 100000:
    if n % 4 == 0 or (n % 100 != 0 and n % 400 == 0):
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")
else:
    print("No es un año válido")