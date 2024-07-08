nombres = []
for i in range(3):
    nombre = input("Ingresa tu nombre: ")
    nombres.append(nombre)

nombre_mas_largo = max(nombres, key=len)

print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")



print("============ Actividad parte número dos ==============")
#Creando listas
nombres = []
apellidos = []
#Pedir que se ingresen los nombres
print("\n Ingresa 3 nombres: ")
for i in range(3):
    nombre = input("Nombre {}: ".format(i + 1))
    nombres.append(nombre)
#Ingresar los apellidos
print("\nIngresa 3 apellidos: ")
for i in range(3):
    apellido = input("Apellido: {}: ".format(i + 1))
    apellidos.append(apellido)
#Imprimir de forma ordenanda en pantalla
print("\nNombres y apellidos: ")
for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)