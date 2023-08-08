CREATE TABLE Usuario (
    dni VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
);


CREATE TABLE Direccion (
    Id_direccion SERIAL PRIMARY KEY,
    dni VARCHAR(15),
    ciudad VARCHAR(100),
    avenida VARCHAR(100),
    Departamento VARCHAR(50),
    FOREIGN KEY (dni) REFERENCES Usuario(dni)
);


CREATE TABLE Mascota (
    id_mascota SERIAL PRIMARY KEY,
    dni VARCHAR(15),
    nombre VARCHAR(100),
    peso DECIMAL,
    edad INTEGER,
    raza VARCHAR(50),
    categoria VARCHAR(50),
    FOREIGN KEY (dni) REFERENCES Usuario(dni)
);
