num = int(input("Ingrese un número:\n"))

if num % 2 == 0:
    print(f'El número es par: {num}')
else:
    print(f'El número es impar: {num}')

if 2 >= num:
    print("Es primo")
elif num % 2 != 0:
    print('Es primo')
else:
    print('No es primo')

if num>50:
    print('El número es mayor a 50')
elif num==50:
    print('El número es 50')
else:
    print('El número es menor a 50')