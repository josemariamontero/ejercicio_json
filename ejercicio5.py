import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

direccion = input("Dime la calle de una confiteria: ")

for i in doc["directorios"]["directorio"]:
	ubicacion_past = i["direccion"]
	if direccion in ubicacion_past:
		descripcion = i["descripcion"]["content"]
		telefono = i["telefono"]["content"]
		foto = i["foto"]["content"]
		print (foto)

	#print(ubicacion_past[0])

#Libertad, 2 - 33206 Gijón
