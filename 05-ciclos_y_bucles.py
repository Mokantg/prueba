#for= hasta que yo quiera
#while= hasta que se cumpla la condición

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