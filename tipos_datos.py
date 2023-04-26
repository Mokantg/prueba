#Clase 26-04-23 apuntes TIPOS DE DATOS

#{}=llaves
#[]=corchetes
#()=parentesis
#/=division
#*=multiplicacion
#**=exponente


edad= 17 #enteros
estatura= 1.63 #real
peso= 60.1
complejo = 1 + 41 #complejos

print("")
#transformacion de un real a entero
print(peso)
print("transformando un valor real a entero: ", int (peso))

#transformando un entero a real
print("Transformando un valor entero a real: ", float(edad))

#OPERACIONES ARITMETICAS
imc= peso / (estatura**2)
print("Mi imc es de: ",imc,"\n")
print(type(imc))
#print("Mi imc es de:{imc}\n")

print("Mi imc es de: {:.2f}".format(imc),"\n")#formateando el valor de sale 2 decimales

asignatura= "programacion"
carrera= "Ingenieria Civil en Informatica"
print("####### 02- STRING #######")
print("La asignatura de", asignatura, "corresponde a la carrera de", carrera)

#uso la funcion de len (contabilizar cantidad de caracteres)
print("la cantidad de caracteres de la palabra", asignatura," es de",len(asignatura))
print("la cantidad de caracteres de la palabra", carrera," es de",len(carrera))

#valores booleanos
ampolleta= False
interruptor = True

print("####### 03- BOOLEANOS #######")
print(ampolleta,interruptor)
print("la variable ampolleta es de tipo:",type(interruptor),"\n")#type reconoce el tipo de dato que se esta trabajando

#podemos transformar cualquier valor a un booleano (como cualquier valor entero, string, int, etc)
print(bool(0))
print(bool(" "))
print(bool(None))
print(bool("True"))
print(bool(1))
print(bool("\n"))

#inicializando listas de 2 maneras
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacia:",nueva_lista)
print("Esta es otra lista vacia:",otra_lista)
print(type(otra_lista))

#declarando 3 listas diferentes
estudiantes=["Matias", "Marco", "Juan", "Pedro", "Cristobal", "Marco"]
num=[1,2,3,4,5,6,7,8,9,10]
lenguaje=["Python"]
data=['Osorno', {'UV': 'Nivel bajo', 'Temp °C': 15}, {-40.5725, -72.1353}]
listamixta=["Felipe", 100, True]
#mixta=["Juan", 18, "Pepe", 13, "Nacho", 16]

#se puede realizar una lista de datos compuestos
print("lista de cadena de caracteres:", estudiantes)
print("lista de numeros:", num)
print("lista de un solo elemento:", lenguaje)
print("esta es una lista mixta:", listamixta)
print('esto es igual a una lista', data)
print(len(listamixta))#cuenta los elementos en la lista
print(estudiantes.count("Marco"))#cuenta la cantidad de elementos llamados Marco
print(num.count(5000))#cantidad de ocurrencias de un elemento en especifico

lenguaje = ['JavaScript']
print('nuevo valor del arreglo de un elemento:',lenguaje)

#como accedo a un elemento especifico de la lista
print(estudiantes[0])#correcto (1° elemento de la lista)
print(estudiantes[1])#2° elemento de la lista
#print(estudiantes[7])#incorrecto
print('Posición -2', estudiantes[-2])

