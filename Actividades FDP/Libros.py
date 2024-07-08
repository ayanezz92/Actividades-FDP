import json

def cargar_libros():
    try:
        with open("libros.json", "r", encoding="utf-8")  as file:
            libros = json.load(file)
    except FileNotFoundError:
        libros = []
    return libros


def guardar_libros(libros):
    with open("libros.json", "w", encoding="utf-8") as file:
        json.dump(libros, file , indent=4)


def gestion_libros():
    libros = cargar_libros()

    while True:
        print("\nBienvenido a la gestión de la colección de libros")
        print("1. Agregar libro")
        print("2. Marcar libro como prestado")
        print("3. Listar todos los libros")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")
        

        if opcion == "1":
            titulo = input("Ingresa el titulo del libro: ")
            autor = input("Ingresa el autor: ")
            estado = "disponible"
            libro = {"titulo": titulo, "autor": autor, "estado": estado}
            libros.append(libro)

        elif opcion == "2":
            titulo = input("Ingresa el titula del libro que deseas marcar como prestado: ")
            encontrado = False
            for libro in libros:
                if libro["titulo"] == titulo:
                    libro["estado"] = "prestado"
                    encontrado = True
                    print(f"Libro {titulo} marcado como prestado.")
                    break
            if not encontrado:
                print(f"No se encontró el libro {titulo} en la colección.")

        elif opcion == "3":
            if libros:
                print("\nListado de libros: ")
                for libro in libros:
                    print(f"Titulo: {libro["titulo"]}, Autor: {libro["autor"]}, Estado: {libro["estado"]}")

            else:
                print("No hay libros en la colección.")
             
        elif opcion == "4":
            guardar_libros(libros)
            print("Saldrás del programa")
            break

        else:
            print("Opcion invalida, porfavor ingresa otra opción.")


gestion_libros()     