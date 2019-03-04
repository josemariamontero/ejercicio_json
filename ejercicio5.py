import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)

indicador = False
direccion = input("Dime la calle de una confiteria: ")

for i in doc["directorios"]["directorio"]:
	if direccion in i["direccion"]:
		nombre = i["nombre"]["content"]
		indicador = True
		descripcion = i["descripcion"]
		telefono = i["telefono"]["content"]
		foto = i["foto"]["content"]
	if not indicador:
		print("No existe esa dirección")

print(nombre)
print("---------------------")
print("Descripción:",descripcion)
print("Telefono:",telefono)
print("Foto:",foto)
	#print(ubicacion_past[0])

#Libertad, 2 - 33206 Gijón
