import statistics
from collections import Counter
def calcular_estadisticas_de_archivo():
    nombre_archivo = "datos.txt"
    try:
        with open (nombre_archivo, "r") as file:
            numeros = [float(line.strip()) for line in file.readlines()]

            if not numeros:
                print("El archivo se encuentra vacío")
                return

        promedio = sum(numeros) / len(numeros)

        numeros_ordenandos = sorted(numeros)
        n = len(numeros_ordenandos)
        if n % 2 == 0:
            mediana = (numeros_ordenandos[n//2 -1] + numeros_ordenandos [n//2]) /2
        else: 
            mediana = numeros_ordenandos[n//2]

        frecuencia = Counter(numeros)
        moda_frecuencia_max = max(frecuencia.values())
        moda = [numeros for numeros, frecuencia in frecuencia.items() if frecuencia == moda_frecuencia_max]
        
        print("makefile")
        print("Copiar código")
        print(f"Promedio: {promedio}")
        print(f"Media: {mediana}")
        print(f"Moda:{", ".join(map(str, moda))}")
    
    except FileNotFoundError:
        print(f"El {nombre_archivo} no fue encontrado")

calcular_estadisticas_de_archivo()