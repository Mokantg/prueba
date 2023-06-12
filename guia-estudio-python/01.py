def numeros(n):
    numeros= []
    for i in range(n):
        num = int(input(f'ingrese el {i+1}° número: '))
        numeros.append(num)
    print(f'Números ingresados: {numeros}')
    total = sum(numeros)
    print(f"La suma total es: {total}")
    pares = sum([num for num in numeros if num % 2 == 0])
    print(f"La suma de los números pares es: {pares}")
    impares = sum([num for num in numeros if num % 2 != 0])
    print(f"La suma de los números impares es: {impares}")

n= int(input('Cuantos números desea ingresar:\n'))
numeros(n)
