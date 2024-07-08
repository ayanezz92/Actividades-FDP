import tkinter as tk #Importando la interfaz grafica
import requests #Para hacer solicitudes http a la api
from io import BytesIO #Trabajar con datos binarios
from PIL import Image, ImageTk #Para trabajar con imágenes desntro de python

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url) #solicitud a la api meidante la url 

    if response.status_code == 200: #Respuesta fue exitosa.
        data = response.json()
        #definir los datos que vamos a obtener del pokemon
        nombre = data["name"]
        numero = data["id"]
        tipos = [tipos["type"]["name"] for tipos in data["types"]] #Obtenemos la categoria del pokemon
        resultado = f"Nombre: {nombre}\n Número del pokemon: {numero}\n Tipo(s): {",".join(tipos)}"
        
        imagen_url = data["sprites"]["front_default"]

        response_imagen = requests.get(imagen_url) #Solicitar get url
        imagen = Image.open(BytesIO(response_imagen.content)) #Abrímos la imagen con BytesIO
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS) #Redimensionar la imagen
        foto = ImageTk.PhotoImage(imagen) #Convertimos la imagen a un objeto
        label_imagen.config(image=foto)
        label_imagen.image = foto #guardando la referencia de la foto
    else:
        resultado = "No se encontró el pokemon"
        label_imagen.config(image=None) #Eliminar la imagen en resultado negativo
    label_resultado.config(text=resultado) #Configura la etiqueta label para mostrar la informacion del pokemon

window = tk.Tk() #Creando la ventana principal
window.title("Búscador de pokemon")

#Campo de busqueda
entry_pokemon = tk.Entry(window)
entry_pokemon.pack() #Empaqueta el campo para vizualizarlo en la pantalla
#boton para buscar
button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon)
button_buscar.pack()

#Espacio o etiqueta vacia para mostrar los datos
label_resultado = tk.Label(window, text="")
label_resultado.pack()
#Mostrar imagen
label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop() #Inicia un bucle principal para poder mostrar la aplicacion