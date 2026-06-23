"""
Configuración de conexión a la base de datos MySQL - PetConnect.
Modificar los valores según el entorno de despliegue.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 3310,
    "database": "petconnect",
    "user": "root",
    "password": "",
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci",
    "autocommit": False
}
