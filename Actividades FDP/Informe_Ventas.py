print("Ingresa los numeros de ventas de correspondientes a cada producto: ")
 
pc= int(input("Ingresa la cantidad de Pan ciabatta vendido: "))
pdl = int(input("Ingresa la cantidad de Pie de limón vendido: "))
cf = int(input("Ingresa la cantidad de Cafés vendidos: "))
te = int(input("Ingresa la cantidad de Té vendida: "))
alf = int(input("Ingresa la catidad de alfajores vendidos: ")) 
ventas_totales = 0
def venta_de_pan (pc):
   return pc * 2000

def venta_de_pie (pdl):
   return pdl * 3500

def venta_de_cafe (cf):
   return cf * 2200

def venta_de_te (te):
   return te * 1600

def venta_de_alfajores (alf):
   return alf * 1000

def obtener_float (mensaje):
   while True:
        try:
            valor = float(input(mensaje))
            if valor < 0 :
                print("El valor no puede ser negativo, intente de nuevo")
            else:
                return valor
        except Exception:
            print("Ingresa un valor valido")


def ventas_totales_del_dia ():
    total = venta_de_pan + venta_de_pie + venta_de_cafe + venta_de_te + venta_de_alfajores
    return total


def inicio():

         while True: 
               pan_ciabatta = venta_de_pan(pc)
               pie_de_limon = venta_de_pie(pdl)
               cafe = venta_de_cafe(cf)
               venta_te = venta_de_te(te)
               alfajores = venta_de_alfajores(alf)
               total = pan_ciabatta + pie_de_limon + cafe + venta_te + alfajores

               with open ("Informe de ventas.txt", "w") as archivo:
                  archivo.write("Informe de ventas\n")
                  archivo.write("================================\n")
                  archivo.write(f"Pan ciabatta vendido: {pc}  =    ${pan_ciabatta}\n")
                  archivo.write(f"Pie de limón vendido: {pdl}  =   ${pie_de_limon}\n")
                  archivo.write(f"Café vendido: {cf}  =   ${cafe}\n")
                  archivo.write(f"Té vendido: {te}  =  ${venta_te}\n")
                  archivo.write(f"Alfajores vendidos: {alf}  =  ${alfajores}\n")
                  archivo.write("------------------------------\n")
                  archivo.write(f"El total de las ventas son: ${total}\n")
   
               print("Los datos fueron guardados correctamentes en el archivo Informe de ventas.txt.")

               break
        

inicio()