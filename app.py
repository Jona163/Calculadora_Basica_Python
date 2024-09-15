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
        label_resultado.config(text=f"Resultado: {resultado}", fg="lime")
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida, ingresa números.")

def restar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}", fg="lime")
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida, ingresa números.")

def multiplicar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}", fg="lime")
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida, ingresa números.")

def dividir():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "División por cero no permitida.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}", fg="lime")
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida, ingresa números.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Hacker")
root.geometry("400x400")
root.config(bg="black")  # Fondo oscuro

# Estilo general
fuente_hacker = ("Courier New", 16, "bold")
color_hacker = "lime"
color_entry = "#1B1B1B"
color_boton = "#008000"
color_boton_hover = "#004d00"
color_texto = color_hacker

# Función para cambiar el color del botón al pasar el ratón
def on_enter(e):
    e.widget['background'] = color_boton_hover

def on_leave(e):
    e.widget['background'] = color_boton

# Widgets
label1 = tk.Label(root, text="Número 1:", font=fuente_hacker, bg="black", fg=color_texto)
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root, font=fuente_hacker, bg=color_entry, fg=color_hacker, insertbackground="lime")
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Número 2:", font=fuente_hacker, bg="black", fg=color_texto)
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, font=fuente_hacker, bg=color_entry, fg=color_hacker, insertbackground="lime")
entry2.grid(row=1, column=1, padx=10, pady=10)

# Botones de las operaciones
boton_sumar = tk.Button(root, text="Sumar", font=fuente_hacker, bg=color_boton, fg=color_texto, command=sumar)
boton_sumar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
boton_sumar.bind("<Enter>", on_enter)
boton_sumar.bind("<Leave>", on_leave)

boton_restar = tk.Button(root, text="Restar", font=fuente_hacker, bg=color_boton, fg=color_texto, command=restar)
boton_restar.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
boton_restar.bind("<Enter>", on_enter)
boton_restar.bind("<Leave>", on_leave)

boton_multiplicar = tk.Button(root, text="Multiplicar", font=fuente_hacker, bg=color_boton, fg=color_texto, command=multiplicar)
boton_multiplicar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
boton_multiplicar.bind("<Enter>", on_enter)
boton_multiplicar.bind("<Leave>", on_leave)

boton_dividir = tk.Button(root, text="Dividir", font=fuente_hacker, bg=color_boton, fg=color_texto, command=dividir)
boton_dividir.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
boton_dividir.bind("<Enter>", on_enter)
boton_dividir.bind("<Leave>", on_leave)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Courier New", 18, "bold"), bg="black", fg="lime")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

# Ejecutar el bucle principal de la ventana
root.mainloop()
