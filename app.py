
# Autor: Jonathan Hernández
# Fecha: 14 Septiembre 2024
# Descripción: Código para calculadora sencilla , python.
# GitHub: https://github.com/Jona163

import tkinter as tk
from tkinter import messagebox

# Funciones de la calculadora
def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def restar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def multiplicar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def dividir():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir por cero")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Básica")

# Crear los widgets
label1 = tk.Label(root, text="Número 1:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Número 2:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Botones de las operaciones
boton_sumar = tk.Button(root, text="Sumar", command=sumar)
boton_sumar.grid(row=2, column=0)

boton_restar = tk.Button(root, text="Restar", command=restar)
boton_restar.grid(row=2, column=1)

boton_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
boton_multiplicar.grid(row=3, column=0)

boton_dividir = tk.Button(root, text="Dividir", command=dividir)
boton_dividir.grid(row=3, column=1)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2)

# Ejecutar el bucle principal de la ventana
root.mainloop()
