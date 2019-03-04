import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

indicador = False
confiterias = input("Dime una subcadena para buscar la confitería: ")

for i in doc["directorios"]["directorio"]:
	nombre = i["nombre"]["content"]
	if confiterias in nombre:
		indicador = True
		print(nombre)

if not indicador:
	print("El nombre introducido no pertenece a ninguna confitería")