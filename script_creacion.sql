drop database if exists echotech_db;
create database echotech_db
character set utf8mb4
collate utf8mb4_general_ci;

use echotech_db;

CREATE TABLE Empleado(
    id_empleado integer auto_increment,
    nombre_empleado varchar(100) not null,
    apellido_empleado varchar(100) not null,
    direccion VARCHAR(100),
    numero_de_telefono varchar(15),
    correo varchar(200),
    fecha_contrato DATE,
    salario DECIMAL(10,2),
    primary key (id_empleado)
);

CREATE TABLE Usuario(
    id_usuario integer auto_increment,
    nombre_usuario varchar(100) not null,
    contrasena varchar(100) not null,
    id_empleado integer not null,
    primary key (id_usuario),
    constraint id_empleado_fk foreign key (id_empleado)
        references Empleado(id_empleado)
);

CREATE TABLE Rol(
    id_rol integer auto_increment,
    nombre_rol varchar(100) not null,
    descripcion varchar(200),
    primary key (id_rol)
);

CREATE TABLE Permiso(
    id_permiso integer auto_increment,
    nombre_permiso varchar(100) not null,
    descripcion VARCHAR(200),
    modulo varchar(100),
    primary key (id_permiso)
);

CREATE TABLE usuario_rol (
    id_usuario integer NOT NULL,
    id_rol integer NOT NULL,
    PRIMARY KEY (id_usuario, id_rol),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol) ON DELETE CASCADE
);

CREATE TABLE rol_permiso (
    id_rol integer NOT NULL,
    id_permiso integer NOT NULL,
    PRIMARY KEY (id_rol, id_permiso),
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol) ON DELETE CASCADE,
    FOREIGN KEY (id_permiso) REFERENCES Permiso(id_permiso) ON DELETE CASCADE
);