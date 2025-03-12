import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola, mundo!")

ventana = tk.Tk()
ventana.title("Mi Primera App")

etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)
boton.pack()

ventana.mainloop()
