use echotech_db;

-- Inserta Empleados
insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario)
values("Daniel","Baeza","Daniel casa","+569 123456789", "Correo1@gmail.com", SYSDATE, 1000000)
insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario)
values("Yami","Ulloa","Yami casa","+569 987654321", "Correo2@gmail.com", SYSDATE, 2000000)
insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario)
values("Jose","Torres","Jose casa","+569 123498765", "Correo3@gmail.com", SYSDATE, 3000000)