DROP DATABASE IF EXISTS echotech_db;

CREATE DATABASE echotech_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE echotech_db;

CREATE TABLE Permiso (
    id_permiso INTEGER AUTO_INCREMENT,
    nombre_permiso VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    modulo VARCHAR(100),
    PRIMARY KEY (id_permiso)
);

CREATE TABLE Rol (
    id_rol INTEGER AUTO_INCREMENT,
    nombre_rol VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    PRIMARY KEY (id_rol)
);

CREATE TABLE rol_permiso (
    id_rol INTEGER NOT NULL,
    id_permiso INTEGER NOT NULL,
    PRIMARY KEY (id_rol, id_permiso),
    constraint fk_rol_permiso_rol FOREIGN KEY (id_rol)
        REFERENCES Rol(id_rol) ON DELETE CASCADE,
    constraint fk_rol_permiso_permiso FOREIGN KEY (id_permiso)
        REFERENCES Permiso(id_permiso) ON DELETE CASCADE
);

CREATE TABLE Usuario (
    id_usuario INTEGER AUTO_INCREMENT,
    nombre_usuario VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
    id_rol INTEGER NOT NULL,
    PRIMARY KEY (id_usuario),
    CONSTRAINT fk_usuario_rol FOREIGN KEY (id_rol)
        REFERENCES Rol(id_rol) ON DELETE CASCADE
);
--CREATE TABLE usuario_rol (
 --   id_usuario INTEGER NOT NULL,
   -- id_rol INTEGER NOT NULL,
  --  PRIMARY KEY (id_usuario, id_rol),
    --CONSTRAINT fk_usuario_rol_usuario FOREIGN KEY (id_usuario)
   --     REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
   -- FOREIGN KEY (id_rol)
   --     REFERENCES Rol(id_rol) ON DELETE CASCADE
--);

CREATE TABLE departamento (
    id_departamento INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    id_empleado_gerente INTEGER,
    PRIMARY KEY (id_departamento)
);

CREATE TABLE Empleado (
    id_empleado INTEGER AUTO_INCREMENT,
    nombre_empleado VARCHAR(100) NOT NULL,
    apellido_empleado VARCHAR(100) NOT NULL,
    direccion VARCHAR(100),
    numero_de_telefono VARCHAR(15),
    correo VARCHAR(200),
    fecha_contrato DATE,
    salario DECIMAL(10,2),
    id_departamento INT DEFAULT 1,
    PRIMARY KEY (id_empleado),
    FOREIGN KEY (id_departamento)
        REFERENCES departamento(id_departamento)
);


ALTER TABLE departamento
ADD CONSTRAINT fk_gerente
FOREIGN KEY (id_empleado_gerente)
REFERENCES Empleado(id_empleado);

CREATE TABLE registro (
    id_registro integer auto_increment,
    fecha_registro DATETIME NOT NULL,
    horas_trabajadas integer NOT NULL,
    descripcion varchar(200),
    id_empleado integer NOT NULL,
    PRIMARY KEY (id_registro),
    constraint fk_registro_empleado FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado) ON DELETE CASCADE
)

CREATE table proyecto (
    id_proyecto integer auto_increment,
    nombre_proyecto varchar(100) not null,
    descripcion varchar(200),
    fecha_inicio DATE,
    id_empleado integer NOT NULL,
    PRIMARY KEY (id_proyecto),
    constraint fk_proyecto_empleado FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado) ON DELETE CASCADE
);

