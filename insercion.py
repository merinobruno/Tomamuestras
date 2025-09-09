import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Copiá y pegá los INSERTS aquí como execute() o executescript()
cursor.executescript("""
INSERT INTO AppTomamuestras_dispositivo (nombre, ubicacion, modelo, numero_serie, fecha_instalacion, estado) VALUES
('Tomador Pozo A', 'Pozo 1 - Plataforma Norte', 'TX-Oil100', 'SN-P001', '2025-01-01', 'Activo'),
('Tomador Pozo B', 'Pozo 2 - Plataforma Sur', 'TX-Oil200', 'SN-P002', '2025-02-15', 'Activo'),
('Tomador Pozo C', 'Pozo 3 - Plataforma Este', 'TX-Oil300', 'SN-P003', '2025-03-20', 'Mantenimiento');
INSERT INTO AppTomamuestras_mantenimiento (dispositivo_id, fecha_hora, tipo_evento, observaciones) VALUES
(3, '2025-09-01 10:00:00', 'Revisión rutinaria', 'Se reemplazó filtro de petróleo'),
(3, '2025-09-05 14:30:00', 'Calibración', 'Ajuste del flujo de muestreo'),
(2, '2025-08-20 09:00:00', 'Revisión rutinaria', 'Todo correcto, presiones normales');
INSERT INTO AppTomamuestras_muestra (dispositivo_id, fecha_hora, contenedor_id, volumen_ml, tipo_muestra, estado) VALUES
(1, '2025-09-09 08:00:00', 'C001', 500.00, 'Petróleo', 'Procesada'),
(1, '2025-09-09 12:00:00', 'C002', 450.50, 'Agua de pozo', 'Procesada'),
(2, '2025-09-08 09:30:00', 'C003', 600.00, 'Gas', 'En espera'),
(3, '2025-09-07 11:00:00', 'C004', 550.00, 'Petróleo', 'Procesada');
INSERT INTO AppTomamuestras_registroestado (dispositivo_id, fecha_hora, nivel_bateria, en_linea, ultima_conexion, codigo_error, observaciones) VALUES
(1, '2025-09-09 08:00:00', 95.0, 1, '2025-09-09 08:00:00', NULL, 'Todo correcto'),
(2, '2025-09-09 08:05:00', 80.5, 1, '2025-09-09 08:05:00', NULL, 'Todo correcto'),
(3, '2025-09-09 07:50:00', 40.0, 0, '2025-09-08 18:00:00', 'E101', 'Batería baja, fuera de línea');                    
                     """)

conn.commit()
conn.close()