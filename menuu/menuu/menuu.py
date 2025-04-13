
import tkinter as tk
from tkinter import messagebox

def archivo_nuevo_presionado(event=None):
    calc = tk.Toplevel()
    calc.title("Calculadora de Sumas")
    calc.geometry("250x180")

    tk.Label(calc, text="Numero 1:").pack()
    entrada1 = tk.Entry(calc)
    entrada1.pack()

    tk.Label(calc, text="Numero 2:").pack()
    entrada2 = tk.Entry(calc)
    entrada2.pack()

    resultado_var = tk.StringVar()
    tk.Label(calc, textvariable=resultado_var, fg="blue").pack()

    def sumar():
        try:
            n1 = float(entrada1.get())
            n2 = float(entrada2.get())
            resultado = n1 + n2
            resultado_var.set(f"Resultado: {resultado}")
        except ValueError:
            resultado_var.set("Ingresa solo numeros validos.")

    tk.Button(calc, text="Sumar", command=sumar).pack(pady=10)

def copiar_enlace(url):
    ventana.clipboard_clear()
    ventana.clipboard_append(url)
    ventana.update()
    messagebox.showinfo("Copiado", f"Enlace copiado:\n{url}")

def menu_iniciar_con_sistema_presionado():
    estado = "activado" if iniciar_con_sistema.get() else "desactivado"
    messagebox.showinfo("Inicio automatico", f"Iniciar con sistema esta {estado}.")

def menu_tema_presionado():
    valor_tema = tema_elegido.get()
    if valor_tema == 1:
        ventana.config(bg="white")
    elif valor_tema == 2:
        ventana.config(bg="#2c2c2c")

ventana = tk.Tk()
ventana.title("Menu")
ventana.geometry("400x300")

barra_menus = tk.Menu()

# Menu Archivo
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=archivo_nuevo_presionado)
ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

# Menu Opciones
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
menu_opciones.add_checkbutton(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    variable=iniciar_con_sistema
)

# Submenu Tema
menu_tema = tk.Menu(menu_opciones, tearoff=False)
tema_elegido = tk.IntVar()
tema_elegido.set(1)
menu_tema.add_radiobutton(label="Claro", variable=tema_elegido, value=1, command=menu_tema_presionado)
menu_tema.add_radiobutton(label="Oscuro", variable=tema_elegido, value=2, command=menu_tema_presionado)
menu_opciones.add_cascade(menu=menu_tema, label="Tema")

# Menu Enlaces
menu_enlaces = tk.Menu(barra_menus, tearoff=False)
menu_enlaces.add_command(label="Google", command=lambda: copiar_enlace("https://www.google.com"))
menu_enlaces.add_command(label="YouTube", command=lambda: copiar_enlace("https://www.youtube.com"))
menu_enlaces.add_command(label="Python", command=lambda: copiar_enlace("https://www.python.org"))

barra_menus.add_cascade(label="Archivo", menu=menu_archivo)
barra_menus.add_cascade(label="Opciones", menu=menu_opciones)
barra_menus.add_cascade(label="Enlaces", menu=menu_enlaces)

ventana.config(menu=barra_menus)
ventana.mainloop()