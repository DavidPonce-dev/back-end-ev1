# Programacion Backend Evaluacion 1 2023

Esta es la propuesta de solucion a la primera evaluacion 

## Instalacion

Necesitas tener [python](https://www.python.org/downloads/) instalado

Use el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar  virtualenv.

```bash
pip install virtualenv
```

Hay que crear el entorno virtual y ejecutarlo para luego instalar las dependencias dentro de este

```bash
py -m venv env   
env/scripts/activate
pip install -r requirements.txt
```

## Uso
Ejecute los comandos para realizar las migraciones

```bash
python manage.py makemigrations menuApp
python manage.py makemigrations optionApp
python manage.py migrate
```

Ahora puede ejecutar el servidor en el entorno virtual


```bash
python manage.py runserver
```
## Consideraciones
Revisar las configuraciones de conexion a mysql para una ejecucion exitosa
Se edita desde
```
./eduardo_chami/.env
```

```bash
...
DB_HOST=localhost
DB_NAME=django
DB_PORT=33060
DB_USER=root
DB_PASSWORD=root
...
```