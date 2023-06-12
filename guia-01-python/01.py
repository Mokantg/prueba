texto = '''La Universidad de los Lagos es una institucion estatal fundada en 1993. 
Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. 
Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica.'''


palabra = "universidad"
n = texto.count(palabra)

print(f"La palabra '{palabra}' aparece {n} veces en el párrafo.")

repetidos = tuple(texto.split())
print(f"Las palabras encontradas son: {repetidos}")