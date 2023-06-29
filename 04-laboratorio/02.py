a = ['Rojo', 'Verde', 'Celeste', 'Violeta']
b = ['Osorno', 'Puerto Montt', 'Puerto Varas', 'Valdivia']

#A
def palabras_max(a):
    palabras_a= max(len(a))
    print(f'la palabra con más letras es: {palabras_a}')

palabras_max(a)

#B
def palabra_min(b):
    palabras_b = min(len(b))
    print(f'la palabra con menos letras es: {palabras_b}')

palabra_min(b)

#C
def concatenar_l(a,b):
    lista_a_b= a+b
    print(lista_a_b)

concatenar_l(a,b)

#D
def mayusculas (lista_a_b):
    print(lista_a_b.upper())

mayusculas()

#E
def ordenar(lista_a_b):
    print(lista_a_b.sort())

ordenar()