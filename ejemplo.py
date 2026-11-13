# Hola mundo modificado
print("Otro título\n")

with open("credenciales","r") as file:
    for linea in file:
        print(linea.strip())