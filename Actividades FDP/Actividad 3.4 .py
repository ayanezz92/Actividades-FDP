#Menú Principal 
print("Elige la operación que deseas resolver: ")
print("1-. Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
#Solicitar al usuario ingresar una opción
opcion = input("Ingresa una opción (1/2/3/4):")

#Solicitar al usuario ingresar los números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número:"))

def suma (num1, num2):
    return num1 + num2

def resta (num1, num2):
    return num1 - num2

def multiplicación (num1, num2):
    return num1 * num2

def división (num1, num2):
    if num1 == 0:
        print("No es posible esta operación")
    elif num2 == 0:
        print("No es posible esta operación")
    else: 
        return num1 / num2 

#Realizar operación seleccionada

if opcion == "1":
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == "2":
    print(num1, "-", num2, "=", resta(num1, num2) )

elif opcion == "3":
    print(num1, "*", num2, "=", multiplicación(num1, num2))

elif opcion == "4": 
    print(num1, "/", num2, "=", división(num1, num2))

else:
    print("Esta opción es invalida")