import random
num= []
for i in range(20):
    num.append(random.randint(40, 350))

print(num)

buscar = int(input("Ingrese un número a buscar en la lista: "))
repetido = num.count(buscar)

print(f"El número {buscar} se repite {repetido} veces en la lista.")