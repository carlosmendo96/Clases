#Programa que te dice si un número es primo o no
def numero_primo(n):
    primo = "Lo es"
    for i in range(2, n):
        if n % i == 0:
            primo = "No lo es"

    print(f'{n} un número primo, {primo} ')

numero_primo(55725242578753554)
