# Hola mundo modificado
print("Hola Mundo")
with open("credenciales","r") as file:
    for linea in file:
        print(linea.strip())