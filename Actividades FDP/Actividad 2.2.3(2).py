#ValorNetoDeUnProducto
producto = input("Ingresa el nombre del producto: ")
valorProducto = int(input("Ingresa el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto*valorNeto)

print("------Detalle Producto------")
print(f"NOMBRE PRODUCTO:  {producto}")
print(f"VALOR PRODUCTO:  {valorProducto}")
print (f"VALOR PRODUCTO SIN IVA:  {valorSinIva}")

