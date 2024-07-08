#pregunta

print("""¿Cual de estos animales vive en el agua?""")
a = "0 puntos"
b = "0,5 puntos"
c = "0 puntos"
d = "1 punto"

print ("a) Perro")
print("b) Cocodrilo")
print("c) Conejo")
print("d) Tiburón")
respuesta = input("Ingresa tu respuesta: ")
if respuesta == "d":
    print(f"Es correcta obtienes {d}")
elif respuesta == "b":
    print(f"Es medianamente correcta, obtienes {b}")

else: print("Es incorrecta")