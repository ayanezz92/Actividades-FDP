matriz_2d = [
        [3,1,9,10],#0
         [7,-1,4,8],#1
        [3,16,-7,9]#2
]
for i in matriz_2d:
    for l in i :
        print(l)

matriz_3d = [
        ["amarillo", "Rojo", "Naranja", "Verde", "Blanco"],#0
]
for i in matriz_3d:
    for f in i :
        print(f)

matriz_3d = [
    [
        ["amarillo","rojo","naranja"],
        ["rojo","verde","amarillo"],
        ["rojo","verde","amarillo"]
    ],
    [
        ["verde","amarillo","blanco"],
        ["amarillo","verde","naranja"],
        ["verde","amarillo","blanco"]
    ],
    [
        ["blanco","rojo","blanco"],
        ["naranja","verde","amarillo"],
        ["verde","amarillo","blanco"]
    ]
]
print(matriz_3d)
amarillo = 0
rojo = 0
naranja = 0
verde = 0
blanco = 0
len(matriz_3d)
for dimension in matriz_3d:
    for fila in dimension:
        for elemento in fila:
            if elemento == "amarillo":
                amarillo = amarillo + 1
            if elemento == "rojo":
                rojo = rojo + 1
            if elemento == "naranja":
                naranja = naranja + 1
            if elemento == "verde":
                verde = verde + 1
            if elemento == "blanco":
                blanco = blanco + 1

print (f"numero de elementos 'amarillo': {amarillo}")
print (f"numero de elementos 'rojo': {rojo}")
print (f"numero de elementos 'naranja': {naranja}")
print (f"numero de elementos 'verde': {verde}")
print (f"numero de elementos 'blanco': {blanco}")