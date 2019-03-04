import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

#direccion = input("Dime la calle de una confiteria: ")

for i in doc["directorios"]["directorio"]:
	ubicacion_past = i["direccion"]
	print(ubicacion_past[0])