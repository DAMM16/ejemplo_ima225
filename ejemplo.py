# Hola mundo modificado
print("Lectura de credenciales:")
with open("credenciales","r") as file:
    for linea in file:
        print(linea.strip())