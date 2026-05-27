import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")

def saludar():
    label.config(text = "Hola mundo!")

boton = tk.Button(ventana, text="Hola", command=saludar)
boton.pack()

label = tk.Label(ventana, text = "")
label.pack()

ventana.mainloop()