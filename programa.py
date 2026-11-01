import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from db import Conexion
from modelo import Empleado

def gestion_empleado(parent: tk.Tk) -> None:
    ventana = tk.Toplevel(parent)
    ventana.title("Gestión de empleados")
    ventana.geometry("1600x1000")

    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.grid(row=0, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_apellido = tk.Label(ventana, text="Apellido:")
    label_apellido.grid(row=1, column=0, pady=10, padx=5)
    entry_apellido = tk.Entry(ventana)
    entry_apellido.grid(row=1, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_direccion = tk.Label(ventana, text="Direccion:")
    label_direccion.grid(row=2, column=0, pady=10, padx=5)
    entry_direccion = tk.Entry(ventana)
    entry_direccion.grid(row=2, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_telefono = tk.Label(ventana, text="Telefono:")
    label_telefono.grid(row=3, column=0, pady=10, padx=5)
    entry_telefono = tk.Entry(ventana)
    entry_telefono.grid(row=3, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_correo = tk.Label(ventana, text="Correo:")
    label_correo.grid(row=4, column=0, pady=10, padx=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.grid(row=4, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_fecha_contrato = tk.Label(ventana, text="Fecha Contrato:")
    label_fecha_contrato.grid(row=5, column=0, pady=10, padx=5)
    entry_fecha_contrato = tk.Entry(ventana)
    entry_fecha_contrato.grid(row=5, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    label_salario = tk.Label(ventana, text="Salario:")
    label_salario.grid(row=6, column=0, pady=10, padx=5)
    entry_salario = tk.Entry(ventana)
    entry_salario.grid(row=6, column=1, pady=10, padx=5, columnspan=3, sticky="we")


    #tablas de abajo
    columnas = ("id", "nombre", "apellido","direccion","telefono","correo","fecha","salario")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", selectmode="browse")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("direccion", text="Direccion")
    tabla.heading("telefono", text="Telefono")
    tabla.heading("correo", text="Correo")
    tabla.heading("fecha", text="Fecha de contrato")
    tabla.heading("salario", text="Salario")
    tabla.grid(row=7, column=0, columnspan=4, pady=5, padx=5)

    def cargar() -> None:
        try:
            empleados = Empleado.buscar_todos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar empleados\n{e}", parent=ventana)
            return
        tabla.delete(*tabla.get_children()) # borra todas las filas de la tabla
        for e in empleados:
            tabla.insert("", "end", values=(e.obtener_id(), e.obtener_nombre(), e.obtener_apellido(), e.obtener_direccion(), e.obtener_telefono(), e.obtener_correo(), e.obtener_contrato(), e.obtener_salario()))

    def seleccionar(event=None) -> None:
        seleccion = tabla.selection()
        if seleccion:
            valores = tabla.item(seleccion[0], "values")
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, valores[1])
            entry_apellido.delete(0, tk.END)
            entry_apellido.insert(0, valores[2])
            entry_direccion.delete(0, tk.END)
            entry_direccion.insert(0, valores[3])
            entry_telefono.delete(0, tk.END)
            entry_telefono.insert(0, valores[4])
            entry_correo.delete(0, tk.END)
            entry_correo.insert(0, valores[5])
            entry_fecha_contrato.delete(0, tk.END)
            entry_fecha_contrato.insert(0, valores[6])
            entry_salario.delete(0, tk.END)
            entry_salario.insert(0, valores[7])

    def limpiar() -> None:
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_fecha_contrato.delete(0, tk.END)
        entry_salario.delete(0, tk.END)
        seleccion = tabla.selection()
        if seleccion:
            tabla.selection_remove(seleccion)
    
    def ingresar() -> None:
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        fecha = entry_fecha_contrato.get()
        salario = entry_salario.get()
        try:
            Empleado(None, nombre, apellido, direccion,telefono,correo,fecha,salario).guardar()
            cargar()
        except Exception as e:
            messagebox.showerror("Error", f"Error al ingresar al empleado\n{e}", parent=ventana)

    def modificar() -> None:
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccionar primero un empleado", parent=ventana)
        else:
            id_empleado = int(tabla.item(seleccion[0], "values")[0])
            try:
                nombre = entry_nombre.get()
                apellido = entry_apellido.get()
                direccion = entry_direccion.get()
                telefono = entry_telefono.get()
                correo = entry_correo.get()
                fecha = entry_fecha_contrato.get()
                salario = entry_salario.get()
                Empleado(id_empleado, nombre, apellido,direccion,telefono,correo,fecha,salario).actualizar()
            except Exception as e:
                messagebox.showerror("Error", f"Error al modificar\n{e}", parent=ventana)
        cargar()
        limpiar()

    def eliminar() -> None:
            seleccion = tabla.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccionar primero un empleado", parent=ventana)
            else:
                if messagebox.askyesno("Confirmación", "¿Está seguro?", parent=ventana):
                    id_empleado = int(tabla.item(seleccion[0], "values")[0])  
                    try:
                        Empleado.buscar_por_id(id_empleado).eliminar() 
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al eliminar\n{e}", parent=ventana)
            cargar()
            limpiar()

    # TreeViewSelect es un evento que se produce cuando se selecciona una fila
    tabla.bind("<<TreeviewSelect>>", seleccionar)
    
    boton_ingresar = tk.Button(ventana, text="Ingresar", command=ingresar)
    boton_ingresar.grid(row=10, column=0, pady=10, padx=5)
    boton_modificar = tk.Button(ventana, text="Modificar", command=modificar)
    boton_modificar.grid(row=10, column=1, pady=10, padx=5)
    boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar)
    boton_eliminar.grid(row=10, column=2, pady=10, padx=5)
    boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.grid(row=10, column=3, pady=10, padx=5)


    cargar()

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

    boton_especialidad = tk.Button(ventana, text="Gestionar empleados", width=30,
                                       command=lambda:gestion_empleado(ventana))
    boton_especialidad.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy)
    boton_salir.pack(pady=10)

    ventana.mainloop()

main()