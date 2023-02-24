#programa que da una piramide de
n = int(input("de que tamaño vas a querer la piramide \n"))

for i in range(1, n + 1):
    print(' ' * (n - i) + '#' * i)
