n=2
suma=0
maximo = 30

while n<maximo:
    print(n)
    suma= suma+n
    if n%5==0:
        print(f'{n} es divisible por 5')
        suma_div_5 =+ n
        
    if n%2!=0:
        #print(f'{n} es impar')
        suma_impar =+n
    n+=3
print(f'la suma de los números divisibles por 5 es: {suma_div_5}')
print(f'la suma de los números impares es: {suma_impar}')
print(f'la suma de todos los números es: {suma}')