import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

indicador = False
confiteria = input("Introduce el nombre de la confiteria: ")

for i in doc["directorios"]["directorio"]:
	horarios = i["horario"]
	if confiteria in i["nombre"]["content"]:
		indicador = True
		print ("El horario de",i["nombre"]["content"],"es:",horarios)

if not indicador:
	print ("Esa confitería no existe")
	