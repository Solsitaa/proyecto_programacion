from datetime import date  
class Empleado: 
    def __init__(self, id_empleado,nombre, direccion, telefono,correo,fecha_contrato, salario):  
        self.__id= id_empleado  
        self.__nombre= nombre  
        self.__direccion= direccion  
        self.__telefono= telefono  
        self.__correo= correo  
        self.__contrato=fecha_contrato  
        self.__salario= salario  
    def obtener_id(self): 
        return self.__id  
    def obtener_nombre(self):  
        return self.__nombre  
    def obtener_direccion(self):  
        return self.__direccion  
    def obtener_telefono(self):  
        return self.__telefono  
    def obtener_correo(self):  
        return self.__correo  
    def obtener_contrato(self):  
        return self.__contrato  
    def obtener_salario(self): 
        return self.__salario  
    def modificar_direccion(self, direccion: str):  
        self.__direccion = direccion  
    def modificar_telefono(self, telefono: str):  
        self.__telefono = telefono  
    def modificar_correo(self, correo: str): 
        self.__correo = correo 
    def modificar_fecha_contrato(self, fecha_contrato: date):  
        self._contrato= fecha_contrato  
    def modificar_salario(self, salario: int):  
        self.__salario=salario     
    def __str__(self): 
        return f"{self.__id} {self.__nombre}" 
class Departamento:  
    def __init__(self, id_d,nd,g,e):  
        self.__id_departamento=id_d  
        self.__nombre_dep=nd  
        self.__gerente= g  
        self.__empleados: list[Empleado] = list() 
    def obtener_id_departamento(self):  
        return self.__id_departamento  
    def obtener_nombre_dep(self):  
        return self.__nombre_dep 
    def obtener_gerente(self): 
        return self.__gerente  
    def obtener_empleado(self):  
        return self.__empleado  
    def modificar_nom_dep(self, nd: str ):  
        self.__nombre_dep=nd  
    def modificar_gerente(self, g:str):  
        self.__gerente=g 
    def agregar_empleado(self,empleado : Empleado): 
        self.__empleados.append(empleado) 
    def quitar_empleado(self,empleado : Empleado): 
        self.__empleados.remove(empleado) 
##Daniel 
class Usuario(Empleado): 
    def __init__(self,id_empleado,nombre, direccion, telefono,correo,fecha_contrato, salario, IdUsuario, NombreUsuario, Contraseña): 
        super().__init__(id_empleado,nombre, direccion, telefono,correo,fecha_contrato, salario) 
        self.__IdUsuario = IdUsuario 
        self.__NombreUsuario = NombreUsuario 
        self.__Contraseña = Contraseña 
    def obtener_ID_Usuario(self): 
        return self.__IdUsuario 
    def obtener_NombreUsuario(self): 
        return self.__NombreUsuario 
    def obtener_Contraseña(self):
        return self.__Contraseña 
class Rol: 
    def __init__(self,IdRol, Nombre, Descripcion): 
        self.__IdRol = IdRol 
        self.__Nombre = Nombre 
        self.__Descripcion = Descripcion 
    def obtener_ID_Rol(self): 
        return self.__IdRol
    def obtener_Nombre(self): 
        return self.__Nombre 
    def obtener_Descripcion(self): 
        return self.__Descripcion
class Permiso: 
    def __init__(self,IdPermiso,nombre,descripcion,modulo): 
        self.__idPermiso = IdPermiso 
        self.__nombre = nombre 
        self.__descripcion = descripcion 
        self.__modulo = modulo
    def obtener_id_permiso(self):
        return self.__idPermiso 
    def obtener_nombre(self): 
        return self.__nombre 
    def obtener_descripcion(self): 
        return self.__descripcion
    def obtener_modulo(self): 
        return self.__modulo
##Jose 
class informe: 
    def __init__(self, empleado, proyecto, departamento, registro_de_tiempo): 
        self.__empleado = empleado 
        self.__proyecto = proyecto 
        self.__departamento = departamento 
        self.__registro_de_tiempo = registro_de_tiempo 
    def obtener_empleado(self): 
        return self.__empleado 
    def obtener_proyecto(self): 
        return self.__proyecto 
    def obtener_departamento(self): 
        return self.__departamento
    def obtener_registro_de_tiempo(self): 
        return self.__registro_de_tiempo 
    def exportar_pdf(self): 
        pass 
    def exportar_excel(self): 
        pass 
class administrador(Empleado): 
    def __init__(self, id_empleado,nombre, direccion, telefono,correo,fecha_contrato, salario):  
        super().__init__(id_empleado,nombre, direccion, telefono,correo,fecha_contrato, salario) 
    def generar_informe(): 
        pass 
class crear_departamento: 
    def __init__(self, id): 
        self.__id_departamento = id 
    def busqueda_departamento(self): 
        pass 
    def eliminar_departamento(self): 
        pass 
    def editar_departamento(self): 
        pass  
    def crear_departamento(self): 
        pass 
#Yami
class Registro: 
    def __init__(self, id_r, f, hr, d):  
        self.__id_registro= id_r  
        self.__fecha= f  
        self.__horas_trabajadas= hr  
        self.__descripcion= d
    def obtener_id_registro(self):  
        return self.__id_registro  
    def obtener_fecha(self):  
        return self.__fecha 
    def obtener_horas_trabajadas(self):  
        return self.__horas_trabajadas  
    def obtener_descripcion(self): 
        return self.__descripcion  
    def modificar_descripcion(self, d:str): 
        self.__descripcion= d
#class proyecto:
