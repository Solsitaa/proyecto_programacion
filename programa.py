import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
from db import Conexion
from modelo import Departamento, Empleado, Administrador, Informe

def gestion_empleado(parent: tk.Tk) -> None:
    ventana = tk.Toplevel(parent)
    ventana.title("Gestión de empleados")
    ventana.geometry("1000x800")

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

    label_id_departamento = tk.Label(ventana, text="ID Departamento:")
    label_id_departamento.grid(row=7, column=0, pady=10, padx=5)
    entry_id_departamento = tk.Entry(ventana)
    entry_id_departamento.grid(row=7, column=1, pady=10, padx=5, columnspan=3, sticky="we")


    #tablas de abajo
    columnas = ("id", "nombre", "apellido","direccion","telefono","correo","fecha","salario","id departamento")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", selectmode="browse")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("direccion", text="Direccion")
    tabla.heading("telefono", text="Telefono")
    tabla.heading("correo", text="Correo")
    tabla.heading("fecha", text="Fecha de contrato")
    tabla.heading("salario", text="Salario")
    tabla.heading("id departamento", text="ID Departamento")
    tabla.grid(row=8, column=0, columnspan=4, pady=5, padx=5)

    def cargar() -> None:
        try:
            empleados = Empleado.buscar_todos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar empleados\n{e}", parent=ventana)
            return
        tabla.delete(*tabla.get_children()) # borra todas las filas de la tabla
        for e in empleados:
            tabla.insert("", "end", values=(e.obtener_id(), e.obtener_nombre(), e.obtener_apellido(), e.obtener_direccion(), e.obtener_telefono(), e.obtener_correo(), e.obtener_contrato(), e.obtener_salario(),e.obtener_id_departamento()))

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
            entry_id_departamento.delete(0, tk.END)
            entry_id_departamento.insert(0, valores[8])

    def limpiar() -> None:
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_fecha_contrato.delete(0, tk.END)
        entry_salario.delete(0, tk.END)
        entry_id_departamento.delete(0, tk.END)
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
        departamento = entry_id_departamento.get()
        try:
            Empleado(None, nombre, apellido, direccion,telefono,correo,fecha,salario,departamento).guardar()
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
                departamento = entry_id_departamento.get()
                Empleado(id_empleado, nombre, apellido,direccion,telefono,correo,fecha,salario,departamento).actualizar()
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

def gestion_departamento(parent: tk.Tk) -> None:
    ventana = tk.Toplevel(parent)
    ventana.title("Gestión de departamentos")
    ventana.geometry("1600x1000")

    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.grid(row=0, column=0, pady=10, padx=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, pady=10, padx=5, columnspan=3, sticky="we")
    
    label_gerente = tk.Label(ventana, text="ID Gerente:")
    label_gerente.grid(row=1, column=0, pady=10, padx=5)
    entry_gerente = tk.Entry(ventana)
    entry_gerente.grid(row=1, column=1, pady=10, padx=5, columnspan=3, sticky="we")

    columnas = ("id", "nombre", "gerente")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", selectmode="browse")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("gerente", text="Gerente")
    tabla.grid(row=8, column=0, columnspan=4, pady=5, padx=5)

    #funciones
    def cargar() -> None:
            try:
                departamentos = Departamento.buscar_todos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar departamentos\n{e}", parent=ventana)
                return
            tabla.delete(*tabla.get_children()) # borra todas las filas de la tabla
            for e in departamentos:
                tabla.insert("", "end", values=(e.obtener_id(), e.obtener_nombre(), e.obtener_gerente()))

    def seleccionar(event=None) -> None:
            seleccion = tabla.selection()
            if seleccion:
                valores = tabla.item(seleccion[0], "values")
                entry_nombre.delete(0, tk.END)
                entry_nombre.insert(0, valores[1])
                entry_gerente.delete(0, tk.END)
                entry_gerente.insert(0, valores[2])

    def limpiar() -> None:
            entry_nombre.delete(0, tk.END)
            entry_gerente.delete(0, tk.END)
            seleccion = tabla.selection()
            if seleccion:
                tabla.selection_remove(seleccion) 


    def ingresar() -> None:
        nombre = entry_nombre.get()
        gerente = entry_gerente.get()
        try:#gpteado
            gerente = int(gerente) if gerente else None
            Departamento(None, nombre, gerente).guardar()
            cargar()
            #gpteado
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Error al ingresar el departamento\n{e}",
                parent=ventana
            )


    def modificar() -> None:
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showerror(
                "Error",
                "Seleccionar primero un departamento",
                parent=ventana
            )
            return

        id_departamento = int(tabla.item(seleccion[0], "values")[0])

        try:
            nombre = entry_nombre.get()
            gerente = entry_gerente.get()

            gerente = int(gerente) if gerente else None

            departamento = Departamento(id_departamento, nombre, gerente)
            departamento.actualizar()

            cargar()
            limpiar()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Error al modificar\n{e}",
                parent=ventana
            )

    def eliminar() -> None:
                seleccion = tabla.selection()
                if not seleccion:
                    messagebox.showerror("Error", "Seleccionar primero un departamento", parent=ventana)
                else:
                    if messagebox.askyesno("Confirmación", "¿Está seguro?", parent=ventana):
                        id = int(tabla.item(seleccion[0], "values")[0])  
                        try:
                            Departamento.buscar_por_id(id).eliminar() 
                        except Exception as e:
                            messagebox.showerror("Error", f"Error al eliminar\n{e}", parent=ventana)
                cargar()
                limpiar()



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

def armar_informe() -> Informe:
    """Crea el informe usando la clase Administrador (como en el diagrama)."""
    # Administrador de ejemplo: hereda de Empleado, que pide 8 datos
    admin = Administrador(None, "Administrador", "", "", "", "", None, 0)
    empleados = Empleado.buscar_todos()
    proyectos = []   # pendiente
    registros = []   # pendiente
    return admin.generar_informe(empleados, proyectos, registros)


def generar_informe(parent) -> None:
    ruta = filedialog.asksaveasfilename(
        parent=parent,
        title="Guardar informe",
        defaultextension=".csv",
        initialfile="informe.csv",
        filetypes=[("Excel / CSV", "*.csv")],
    )
    if not ruta: 
        return
    try:
        armar_informe().exportar_excel(ruta)
        messagebox.showinfo("Informe", f"Informe guardado en:\n{ruta}", parent=parent)
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el informe\n{e}", parent=parent)


def menu_administrador(parent) -> None:
    """Ventana del administrador. Se puede abrir desde el menú principal del grupo."""
    ventana = tk.Toplevel(parent)
    ventana.title("Administrador")
    ventana.geometry("300x280")
    ventana.resizable(False, False)

    titulo = tk.Label(ventana, text="Panel administrador", font=("Arial", 16, "bold"))
    titulo.pack(pady=20, padx=15)

    boton_dep = tk.Button(ventana, text="Gestionar departamentos", width=30,
                          command=lambda: gestion_departamento(ventana))
    boton_dep.pack(pady=10)

    boton_informe = tk.Button(ventana, text="Generar informe", width=30,
                              command=lambda: generar_informe(ventana))
    boton_informe.pack(pady=10)

    boton_cerrar = tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy)
    boton_cerrar.pack(pady=10)

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

    boton_empleados = tk.Button(ventana, text="Gestionar empleados", width=30,
                                       command=lambda:gestion_empleado(ventana))
    boton_empleados.pack(pady=10)

    boton_departamentos = tk.Button(ventana, text="Gestionar Departamentos", width=30,
                                        command=lambda:gestion_departamento(ventana))
    boton_departamentos.pack(pady=10)

    boton_administrador = tk.Button(ventana, text="Prueba administrador", width=30,
                                            command=lambda:menu_administrador(ventana))
    boton_administrador.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy)
    boton_salir.pack(pady=10)

    ventana.mainloop()

main()