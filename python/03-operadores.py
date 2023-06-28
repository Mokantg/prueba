a= 25
b=2
c=14
d=36
e=7

#peradores aritmeticos o comunes

print("########## OPERADORES ARITMETICOS ##########")
print("suma entre a + b es: ", a+b)
print("resta entre a - b es: ", a-b)
print("multiplicacion entre a * b es: ", a*b)
print('la division entre a / b es: ', a/b)
print(a%b)
print(a**b)
print(a//b)


t= 5.29
g= 9.81

#operaciones aritmeticas entre flotantes
v= g * t
print(f"la velocidad del objeto en caida libre es de: {v} n/s")
print("la velocidad  del objeto en caida libre es de: {:.2f}".format(v))

#creando un numero complejo con complex
c2 = complex(3, -5)

print('el numero complejo es: ',c2)

print(c2.real)

#string con numero

print('Hola' * 5)

#no se puede
#print('Hola' * 3.5*2)

#print('Hola ' * (10*2) /5)

print("########## OPERADORES DE COMPARACION ##########")
print(a == b) # iguales
print(a >= b) # mayor o igual 
print(a <= b) # menor o igual 
print(a != b) # distintos

animal_domestico= 'gato'
animal_salvaje = 'leopardo'

print('\ncomparando cadenas de caracteres')
print(animal_domestico == animal_salvaje) #igual
print(animal_domestico != animal_salvaje) #diferentes
print(animal_domestico < animal_salvaje) #menor que
print(animal_domestico > animal_salvaje) #mayor que
print(animal_domestico >= animal_salvaje) #mayor o igual que
print(animal_domestico <= animal_salvaje) #menor o igual que


bencina= True
encendido = True
edad= 19

#utilizando el operador and
if bencina and encendido:
    print('El vehiculo puede avanzar') 
else:
    print('el vehiculo no puede arrancar')
#operador or
if bencina or encendido:
    print('el vehiculo puede arrancar')
else:  
    print('el vehiculo no puede arrancar')
#operador not
if not bencina and encendido:
    print('el vehiculo puede avanzar')
else: 
    print('el vehiculo no puede arrancar')

#utilizando tres operadores AND, OR Y NOT
if not bencina or (encendido and edad>=18):
    print('el vehiculo puede avanzar')
else: 
    print('el vehiculo no puede arrancar')