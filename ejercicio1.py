"""
	Ejercicio de practica 1
	@pablom7
"""

import codecs
import json
archivo = codecs.open("datos.txt")
lineas = archivo.readlines()
lineas_diccionario = [json.loads(l) for l in lineas]
goles = list(filter(lambda x: list(x.items())[1][1]>3, lineas_diccionario))
print("Jugadores que han anotado mas de 3 goles: ")
print(list(goles))
nacionalidad = list(filter(lambda x: list(x.items())[0][1]=="Nigeria", lineas_diccionario))
print("Jugadores de Nigeria: ")
print(list(nacionalidad))
alturas = lambda x: list(x.items())[2][1]
print("El jugador de mayor altura mide: ")
print(max(list(map(alturas, lineas_diccionario))))
print("El jugador de menor altura mide: ")
print(min(list(map(alturas, lineas_diccionario))))
