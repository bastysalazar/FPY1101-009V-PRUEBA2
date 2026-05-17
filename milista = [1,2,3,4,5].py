diccionario = {"nombre":"cesar huispe",
            "fonos":[
                988778882, 
                988877776,
                877666333],
            "activos":True}
print("nombre:",diccionario["nombre"])
print("segundo telefono:",diccionario["fonos"][1])
diccionario["email"]="cesar.huispe@gmail.com"
diccionario["fonos"].append(123456789)
diccionario["activo"]=False
diccionario["fonos"][0]=99999999
del diccionario["activo"]
diccionario["fonos"].pop(2)
print(diccionario)