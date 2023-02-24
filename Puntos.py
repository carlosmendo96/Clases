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

    def matriz():
        a = 0
        for i in range(n):
            a += arr[i][i] - arr[(n - 1) - i][i]
            return abs(a)
