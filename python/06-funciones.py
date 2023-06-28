#01-DECLARANDO LA PRIMERA FUNCIÓN
print('>>>>>> DECLARANDO UNA FUNCION SIMPLE <<<<<<')

def mi_primera_funcion():
    print('Esta es mi primera función')
    
mi_primera_funcion()

#02-DECLARANDO UNA FUNCION Y UTILIZANDO LISTAS
print('\n>>>>>> DECLARANDO UNA FUNCION SIMPLE Y UTILIZANDO LISTAS <<<<<<')

def concatenar(lista1, lista2):
    return lista1 + lista2

lista1=[1, 2, 3]
lista2=[4, 5, 6]

#concatenar()
print(concatenar(lista1,lista2))

#03-DECLARANDO UNA FUNCION MULTIPLICACION PASANDO PARAMETROS
print('\n>>>>>> DECLARANDO UNA FUNCION MULTIPLICACION PASANDO PARAMETROS <<<<<<')

def multiplicacion(num1, num2):
    return num1 * num2

#multiplicacion()
print(multiplicacion(10,5))

#04-FUNCIONES SUMA Y RESTA (POR TECLADO)
print('\n>>>>>> FUNCIONES SUMA Y RESTA (POR TECLADO) <<<<<<')

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))

resultado = suma(a,b)

resultado2 = resta(a,b)
print(f'el resultado de la suma: {resultado}')
print(f'el resultado de la resta: {resultado2}')