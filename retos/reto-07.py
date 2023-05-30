def contar_palabras(frase):
    palabras = frase.split()
    frase = {}
    for palabra in palabras:
        frase[palabra] = len(palabra)
    return frase

frase = input("Introduce una frase: ")
print(contar_palabras(frase))