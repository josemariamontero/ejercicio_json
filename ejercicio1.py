import json
with open('confiterias.json','r') as fichero:
	doc = json.load(fichero)
	#print(doc)

for i in doc["directorios"]["directorio"]:
	nombre = i["nombre"]["content"]
	pag_web = i["web"]
	#print(i)
	if not pag_web:
		print (nombre,"->","Ésta confitería no tiene página web")
	else:
		print(nombre,"->",pag_web)