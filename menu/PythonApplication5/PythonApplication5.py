import tkinter as tk
from tkinter import messagebox

def archivo_nuevo_presionado(event=None):
    print("Has presionado para crear un nuevo archivo")

def menu_iniciar_con_sistema_presionado():
    if iniciar_con_sistema.get():
        print("Opcion establecida (iniciar con el sistema).")
    else:
        print("Opcion deshabilitada (no iniciar con el sistema).")

def menu_tema_presionado():
    valor_tema = tema_elegido.get()
    if valor_tema == 1:
        print("Tema claro establecido.")
    elif valor_tema == 2:
        print("Tema oscuro establecido.")

# Funcion para copiar enlace al portapapeles
def copiar_enlace(url):
    ventana.clipboard_clear()
    ventana.clipboard_append(url)
    ventana.update()
    messagebox.showinfo("Copiado", f"Enlace copiado:\n{url}")

ventana = tk.Tk()
ventana.title("Barra de menus en Tk")
ventana.config(width=400, height=300)

barra_menus = tk.Menu()

# === Menu Archivo ===
menu_archivo = tk.Menu(barra_menus, tearoff=False)

try:
    img_menu_nuevo = tk.PhotoImage(file="nuevo_archivo.png")
    menu_archivo.add_command(
        label="Nuevo",
        accelerator="Ctrl+N",
        command=archivo_nuevo_presionado,
        image=img_menu_nuevo,
        compound=tk.LEFT
    )
except Exception as e:
    menu_archivo.add_command(
        label="Nuevo",
        accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )

ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

# === Menu Opciones ===
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
menu_opciones.add_checkbutton(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    variable=iniciar_con_sistema
)

# Submenu Tema
menu_tema = tk.Menu(barra_menus, tearoff=False)
tema_elegido = tk.IntVar()
tema_elegido.set(1)
menu_tema.add_radiobutton(
    label="Claro",
    variable=tema_elegido,
    value=1,
    command=menu_tema_presionado
)
menu_tema.add_radiobutton(
    label="Oscuro",
    value=2,
    variable=tema_elegido,
    command=menu_tema_presionado
)
menu_opciones.add_cascade(menu=menu_tema, label="Tema")

# === Menu Enlaces ===
menu_enlaces = tk.Menu(barra_menus, tearoff=False)
menu_enlaces.add_command(label="Google", command=lambda: copiar_enlace("https://www.google.com"))
menu_enlaces.add_command(label="YouTube", command=lambda: copiar_enlace("https://www.youtube.com"))
menu_enlaces.add_command(label="Python", command=lambda: copiar_enlace("https://www.python.org"))

# Agregar menus a la barra
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
barra_menus.add_cascade(menu=menu_enlaces, label="Enlaces")

ventana.config(menu=barra_menus)
ventana.mainloop()