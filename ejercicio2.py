import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

contador = 0

for i in doc["directorios"]["directorio"]:
	nombre = i["nombre"]["content"]
	contador = contador + 1
print ("En total hay",contador,"confiterias")	