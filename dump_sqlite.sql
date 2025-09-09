-- dump_sqlite.sql compatible con SQLite
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE AppTomamuestras_dispositivo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ubicacion TEXT,
    modelo TEXT,
    numero_serie TEXT,
    fecha_instalacion DATE,
    estado TEXT
);

CREATE TABLE AppTomamuestras_mantenimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo_id INTEGER NOT NULL,
    fecha_hora DATETIME NOT NULL,
    tipo_evento TEXT,
    observaciones TEXT,
    FOREIGN KEY(dispositivo_id) REFERENCES dispositivo(id) ON DELETE CASCADE
);

CREATE TABLE AppTomamuestras_muestra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo_id INTEGER NOT NULL,
    fecha_hora DATETIME NOT NULL,
    contenedor_id TEXT,
    volumen_ml REAL,
    tipo_muestra TEXT,
    estado TEXT,
    FOREIGN KEY(dispositivo_id) REFERENCES dispositivo(id) ON DELETE CASCADE
);

CREATE TABLE AppTomamuestras_registroestado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo_id INTEGER NOT NULL,
    fecha_hora DATETIME NOT NULL,
    nivel_bateria REAL,
    en_linea INTEGER,
    ultima_conexion DATETIME,
    codigo_error TEXT,
    observaciones TEXT,
    FOREIGN KEY(dispositivo_id) REFERENCES dispositivo(id) ON DELETE CASCADE
);

COMMIT;
PRAGMA foreign_keys=ON;