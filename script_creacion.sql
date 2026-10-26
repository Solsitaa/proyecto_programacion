DROP TABLE rol_permiso PURGE;
DROP TABLE usuario_rol PURGE;
DROP TABLE Permiso PURGE;
DROP TABLE Rol PURGE;
DROP TABLE Usuario PURGE;
DROP TABLE Empleado PURGE;

CREATE TABLE Empleado(
    id_empleado VARCHAR2(12),
    nombre_empleado VARCHAR2(100) CONSTRAINT nombre_empleado_nn NOT NULL,
    apellido_empleado VARCHAR2(100) CONSTRAINT apellido_empleado_nn NOT NULL,
    direccion VARCHAR(100),
    numero_de_telefono VARCHAR2(15),
    correo VARCHAR2(200),
    fecha_contrato DATE,
    salario NUMBER,
    primary key (id_empleado)
);

CREATE TABLE Usuario(
    id_usuario VARCHAR2(12) CONSTRAINT id_usuario_pk PRIMARY KEY,
    nombre_usuario VARCHAR2(100) CONSTRAINT nombre_usuario_nn NOT NULL,
    contraseña VARCHAR2(100) CONSTRAINT contraseña_nn NOT NULL,
    id_empleado VARCHAR2(12) not null,
    constraint id_empleado_fk foreign key (id_empleado)
    references Empleado(id_empleado)
);

CREATE TABLE Rol(
    id_rol VARCHAR2(12) CONSTRAINT id_rol_ok PRIMARY KEY,
    nombre_rol VARCHAR2(100) CONSTRAINT nombre_rol_nn NOT NULL,
    descripcion VARCHAR2(200)
);

CREATE TABLE Permiso(
    id_permiso VARCHAR2(12) CONSTRAINT id_permiso_pk PRIMARY KEY,
    nombre_permiso VARCHAR2(100) CONSTRAINT nombre_permiso_nn NOT NULL,
    descripcion VARCHAR(200),
    modulo VARCHAR2(100)
);

CREATE TABLE usuario_rol (
    id_usuario VARCHAR2(12) NOT NULL,
    id_rol VARCHAR2(12) NOT NULL,

    PRIMARY KEY (id_usuario, id_rol),

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE,

    FOREIGN KEY (id_rol)
        REFERENCES rol(id_rol)
        ON DELETE CASCADE
);

CREATE TABLE rol_permiso (
    id_rol VARCHAR2(12) NOT NULL,
    id_permiso VARCHAR2(12) NOT NULL,

    PRIMARY KEY (id_rol, id_permiso),

    FOREIGN KEY (id_rol)
        REFERENCES Rol(id_rol)
        ON DELETE CASCADE,

    FOREIGN KEY (id_permiso)
        REFERENCES Permiso(id_permiso)
        ON DELETE CASCADE
);