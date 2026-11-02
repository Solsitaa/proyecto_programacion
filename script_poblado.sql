use echotech_db;

-- Agregar a script_poblado.sql
INSERT INTO departamento (nombre, id_gerente)
VALUES
('Informática', NULL),
('Recursos Humanos', NULL),
('Contabilidad', NULL);

-- Inserta Empleados
insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario,id_departamento)
values('Daniel','Baeza','Daniel casa','+569 123456789','Correo1@gmail.com', CURDATE(), 1000000,1);

insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario,id_departamento)
values('Yami','Ulloa','Yami casa','+569 987654321','Correo2@gmail.com', CURDATE(), 2000000,1);

insert into Empleado(nombre_empleado, apellido_empleado, direccion, numero_de_telefono, correo, fecha_contrato, salario,id_departamento)
values('Jose','Torres','Jose casa','+569 123498765','Correo3@gmail.com', CURDATE(), 3000000,1);


