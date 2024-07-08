#MatrículaColegio
alumno = input("Ingrese el nombre del alumno: ")
rut = input("Ingrese rut del apoderado: ")
curso = input("Ingrese curso en el que desea matrícularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad*10)+matricula

print("-----Detalle Anualidad Colegio----")
print(f"NOMBRE ALUMNO: {alumno}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
