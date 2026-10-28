import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from db import Conexion
from modelo import Empleado


def main():
    ventana = tk.Tk()
    ventana.title("EchoTech")
    ventana.geometry("300x300")
    ventana.resizable(False, False)

    titulo = tk.Label(ventana, text="Menú EchoTech", font=("Arial", 16, "bold"))
    titulo.pack(pady=20, padx=15)

    ##boton_especialidad = tk.Button(ventana, text="Gestionar especialidades", width=30,
    ##                               command=lambda:gestion_especialidad(ventana))
    ##boton_especialidad.pack(pady=10)

    ##boton_test = tk.Button(ventana, text="Probar conexión", width=30, command=test)
    ##boton_test.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy)
    boton_salir.pack(pady=10)

    ventana.mainloop()

main()