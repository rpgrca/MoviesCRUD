# MoviesCRUD

Un programa hecho en Python con Tkinter para manejo de películas y categorías.

Menú Sistema:
- Salir: Sale del programa

Menú Ajustes:
- Memoria Volátil: Realiza manejo en memoria de los datos. Trae 5 películas por defecto.
- Archivo JSON: Serializa a un único archivo JSON
- Archivo CSV: Serializa a dos archivos CSV, uno de películas y uno de categorías
- Vacío (sin valores): Trabaja en memoria, pero sin datos de prueba
- Base Shelve: Serializa a una base de datos Shelve
- Base MySQL: Serializa a una base de datos MySQL
- Base ZODB: Serializa a una base de datos ZODB
- Base MongoDB: Serializa a una base de datos Mongo
- Base SQLite3: Serializa a una base de datos SQLite3.
- Configuración: Permite modificar los archivos/conexiones a utilizar por cada tipo de conexión.
  NO SE PUEDE MODIFICAR LA CONFIGURACION DE LA CONEXION ACTUAL. Tampoco de Memoria Volatil y Vacio.

Las categorías se graban al grabar la película. NO SE PUEDEN BORRAR UNA VEZ CREADAS.

Si cambiar a una nueva conexión no es posible, se revierte a la anterior.
