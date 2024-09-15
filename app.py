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
        label_resultado.config(text=f"Resultado: {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def restar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def multiplicar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

ef dividir():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir por cero")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Pro")
root.geometry("400x400")
root.config(bg="#2C3E50")  # Fondo oscuro

# Estilo general
fuente_general = ("Arial", 16, "bold")
color_boton = "#E74C3C"
color_boton_hover = "#C0392B"
color_texto = "#ECF0F1"
color_entry = "#34495E"


# Función para cambiar el color del botón al pasar el ratón
def on_enter(e):
    e.widget['background'] = color_boton_hover

def on_leave(e):
    e.widget['background'] = color_boton

# Widgets
label1 = tk.Label(root, text="Número 1:", font=fuente_general, bg="#2C3E50", fg=color_texto)
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root, font=fuente_general, bg=color_entry, fg=color_texto)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Número 2:", font=fuente_general, bg="#2C3E50", fg=color_texto)
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, font=fuente_general, bg=color_entry, fg=color_texto)
entry2.grid(row=1, column=1, padx=10, pady=10)
