#for= hasta que yo quiera
#while= hasta que se cumpla la condición

print('>>>>> COMIENZO CICLO WHILE <<<<<')

#WHILE (MIENTRAS)
print('\n>>>Creando bucle')

edad = 15
num = 0

#while edad < 18:
    #print('Eres menor de edad, no puedes manejar')
#print('fin bucle')
print('>>> Impresion de numeros de 2 en 2 hasta 100')

num = 0
while num<=100:
    print(num)
    num += 2
print('>>> Primer bucle terminado\n')

#bucle infinito
#while True:
    #print(num)
    #num +=2

print('>>> Impresion de numeros de 2 en 2 hasta 200')
while num <=200:
    print(num)
    num +=2
else: 
    print('Mi condicion es igual o mayor a 200')

print('>>> Segundo bucle terminado\n')



print('>>> Impresion de numeros de 2 en 2 hasta 300')
while num <=300:
    print(num)
    num += 2
    if num == 250:
        print('Mi condicion es igual a 250')
print('>>> Tercer bucle terminado\n')



print('>>> Impresion de numeros de 2 en 2 hasta 400')
while num <=400:
    print(num)
    num += 2
    if num == 350:
        print('Se detiene la ejecución')
        break
print(num)
print('>>> Cuarto bucle terminado\n')


#loop infinito + break
while True:
    parametro = input('>')
    if parametro == 'exit':
        break
    else:
        print(parametro)
print('\n')

print('>>>>> COMIENZO CICLO FOR <<<<<')
print('>>> Imprimiendo una lista de 10 valores\n')
#esto no esta bien optimizado
print('>> Primer For')
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
print('\n')

print('>> Segundo For')
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)
print('\n')

print('>> Tercer For')
for i in range(1, 11):
    print(i)
print('\n')