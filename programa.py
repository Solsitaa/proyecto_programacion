import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from db import Conexion
from modelo import Empleado

def gestion_empleado(parent: tk.Tk) -> None:
    ventana = tk.Toplevel(parent)
    ventana.title("Gestión de empleados")
    ventana.geometry("620x400")

    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.grid(row=0, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, pady=10, padx=5, columnspan=3, sticky="we")
    label_descrip = tk.Label(ventana, text="Descripción:")
    label_descrip.grid(row=1, column=0, pady=10, padx=5)
    entry_descrip = tk.Entry(ventana)
    entry_descrip.grid(row=1, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    columnas = ("id", "nombre", "descripcion")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", selectmode="browse")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("descripcion", text="Descripción")
    tabla.grid(row=2, column=0, columnspan=4, pady=5, padx=5)

    # def cargar() -> None:
    #     try:
    #         especialidades = Especialidad.buscar_todos()
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error al cargar especialidades\n{e}", parent=ventana)
    #         return
    #     tabla.delete(*tabla.get_children()) # borra todas las filas de la tabla
    #     for e in especialidades:
    #         tabla.insert("", "end", values=(e.obtener_id(), e.obtener_nombre(), e.obtener_descripcion()))

    def seleccionar(event=None) -> None:
        seleccion = tabla.selection()
        if seleccion:
            valores = tabla.item(seleccion[0], "values")
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, valores[1])
            entry_descrip.delete(0, tk.END)
            entry_descrip.insert(0, valores[2])

    def limpiar() -> None:
        entry_nombre.delete(0, tk.END)
        entry_descrip.delete(0, tk.END)
        seleccion = tabla.selection()
        if seleccion:
            tabla.selection_remove(seleccion)
    
    # def ingresar() -> None:
    #     nombre = entry_nombre.get()
    #     descripcion = entry_descrip.get()
    #     try:
    #         Especialidad(None, nombre, descripcion).guardar()
    #         cargar()
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error al ingresar la especialidad\n{e}", parent=ventana)

    def modificar() -> None:
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccionar primero una especialidad", parent=ventana)
        else:
            id_especialidad = int(tabla.item(seleccion[0], "values")[0])
            try:
                nombre = entry_nombre.get()
                descripcion = entry_descrip.get()
                Especialidad(id_especialidad, nombre, descripcion).actualizar()
            except Exception as e:
                messagebox.showerror("Error", f"Error al modificar\n{e}", parent=ventana)
        #cargar()
        limpiar()

def test() -> None:
    cursor = None
    try:
        cursor = Conexion().obtener_conexion().cursor()
        cursor.execute("SELECT version()")
        version = cursor.fetchone()[0]
        messagebox.showinfo("Información", f"Conexión exitosa:\nVersión del servidor: {version}")
    except Exception as e:
        messagebox.showerror("Error", f"Error de conexión:\n{e}")
    finally:
        if cursor is not None:
            cursor.close()

def main():
    ventana = tk.Tk()
    ventana.title("EchoTech")
    ventana.geometry("300x300")
    ventana.resizable(False, False)

    titulo = tk.Label(ventana, text="Menú EchoTech", font=("Arial", 16, "bold"))
    titulo.pack(pady=20, padx=15)

    boton_test = tk.Button(ventana, text="Probar conexión", width=30, command=test)
    boton_test.pack(pady=10)

    boton_especialidad = tk.Button(ventana, text="Gestionar especialidades", width=30,
                                       command=lambda:gestion_empleado(ventana))
    boton_especialidad.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy)
    boton_salir.pack(pady=10)

    ventana.mainloop()

main()