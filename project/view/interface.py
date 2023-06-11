import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def gui():
    def get_clicked():
        return [path.get(), name.get(), frontendType.get().lower(), backend.get().lower(), frontend.get().lower()]
    # root window
    root = tk.Tk()
    root.geometry("450x400")
    root.resizable(False, False)
    root.title('@JuanMahecha9 -> Custom Fullstack Project')
    # store name address and path
    name = tk.StringVar()
    path = tk.StringVar()
    frontendType = tk.StringVar()
    backend = tk.StringVar()
    frontend = tk.StringVar()

    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    _label = ttk.Label(
        signin, text="If you only need an one service, type yes or no into the first and second field. \n \n")
    _label.pack(fill='x', expand=True)


    # Se necesita crear el frontend
    frontend_label = ttk.Label(
        signin, text="Yes or no, you need a frontend service?")
    frontend_label.pack(fill='x', expand=True)

    frontend_entry = ttk.Entry(signin, textvariable=frontend)
    frontend_entry.pack(fill='x', expand=True)

    # Se necesita crear el backend
    backend_label = ttk.Label(
        signin, text="Yes or no, you need an API rest service?")
    backend_label.pack(fill='x', expand=True)

    backend_entry = ttk.Entry(signin, textvariable=backend)
    backend_entry.pack(fill='x', expand=True)

    # Nombre proyecto
    name_label = ttk.Label(signin, text="Project Name:")
    name_label.pack(fill='x', expand=True)

    name_entry = ttk.Entry(signin, textvariable=name)
    name_entry.pack(fill='x', expand=True)
    name_entry.focus()

    # path
    path_label = ttk.Label(
        signin, text="Path, Ex. /Users/user/Desktop/env ...")
    path_label.pack(fill='x', expand=True)

    path_entry = ttk.Entry(signin, textvariable=path)
    path_entry.pack(fill='x', expand=True)

    # Typo de framework
    frontendType_label = ttk.Label(
        signin, text="Set Ionic or Angular")
    frontendType_label.pack(fill='x', expand=True)

    frontendType_entry = ttk.Entry(signin, textvariable=frontendType)
    frontendType_entry.pack(fill='x', expand=True)

    # boton ingresar
    get_button = ttk.Button(
        signin, text="Begin process...", command=get_clicked)
    get_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()
    return get_clicked()
