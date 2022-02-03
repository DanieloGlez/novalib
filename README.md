# NOVALIB
### Sistema de Gestión para el departamento de Liberación de Lotes de la UEB Novatec
#
### Configuración:
1. Restaurar la salva de la base de datos ```/bd/liberacion_dump``` (Se requiere PostgreSQL 13.4)
3. Cambiar la informacion en ```config.json``` acorde con la configuración que se vaya a establecer
2. Instalar python 3.8 y ejecutar el siguiente comando en la terminal para instalar las dependencias: 
```
 pip install -r requirements.txt
```
### Ejecución:
- Windows 
```
python .\liberacion\liberacion.py
```
- Linux or MacOS
```
python ./liberacion/liberacion.py
```