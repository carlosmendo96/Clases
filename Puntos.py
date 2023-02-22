#Programa que da matrices n x m
n = int(input("número de filas de tu matrizz \n"))
m = int(input("número de columnas de tu matriz \n"))

matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        valor = int(input(f'Digite el valor {i}, {j} de la matriz \n'))
        matriz[i].append(valor)

for i in matriz:
    print(i, end=' ')
    print()
