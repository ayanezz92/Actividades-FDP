#Solicitar notas
not1 = float(input("Ingresa la nota uno: "))
not2 = float(input("Ingresa la nota dos: "))
not3 = float(input("Ingresa la nota tres: "))

notaF = (not1+not2+not3)/3

if notaF >= 4.0:
    print(f"Aprobado con {notaF}")
else: 
    print(f"No has aprobado, tu nota es {notaF}")