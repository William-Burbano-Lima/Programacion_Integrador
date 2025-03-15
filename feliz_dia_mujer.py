import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def mostrar_mensaje():
    mensajes = [
        "¡Feliz Día de la Mujer! Eres fuerte, valiente y llena de luz.",
        "Hoy celebramos tu esencia, tu poder y tu inspiración. ¡Felicidades!",
        "Que cada día sea una oportunidad para brillar. ¡Feliz Día de la Mujer!",
        "El mundo es mejor gracias a mujeres como tú. ¡Felicidades en tu día!",
        "Nunca olvides lo increíble que eres. ¡Feliz 8 de marzo!"
    ]
    mensaje = random.choice(mensajes)
    messagebox.showinfo("Día de la Mujer", mensaje)

# Crear ventana principal
root = tk.Tk()
root.title("Feliz Día de la Mujer")
root.geometry("1000x1000")
root.configure(bg="#FFC0CB")

# Cargar imagen
imagen = Image.open("dia_mujer.png")  # Asegúrate de tener una imagen con este nombre en la carpeta
imagen = imagen.resize((500, 500))
foto = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(root, image=foto, bg="#FFC0CB")
label_imagen.pack(pady=10)

# Etiqueta de bienvenida
label_texto = tk.Label(root, text="¡Feliz Día de la Mujer!", font=("Arial", 14, "bold"), bg="#FFC0CB", fg="#800080")
label_texto.pack(pady=10)

# Botón para mostrar mensaje
btn_mensaje = tk.Button(root, text="Ver Mensaje Especial", font=("Arial", 12), command=mostrar_mensaje, bg="#800080", fg="white")
btn_mensaje.pack(pady=20)

# Ejecutar la ventana
root.mainloop()
