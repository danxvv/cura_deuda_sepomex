# Backend para prueba de conocimiento de CURA DEUDA

## DEMO API
La api se encuentra actualmente en un servidor, por lo que se puede acceder a ella mediante la siguiente liga: http://34.72.229.196/api

## preparación del entorno

Antes de ejecutar algún comando o script se necesitan instalar ciertos paquetes para que todo pueda funcionar.
Instalar mediante:

`pip install -r requirements.txt`

Así mismo es recomendable declarar de una vez las variables para que flask funcione:

* Linux : `export FLASK_APP=main.py`
* Windows-CMD : `set FLASK_APP=main.py`
* Windows-PowerShell : `$env:FLASK_APP = main.py`

## Uso del SeedScript

El script `extract_data.py` está listo para funcionar sin configurar nada, pues hace uso de **sqlite3**, si no existe la base de datos el script la creara, procederá a borrar tablas que se requieran si existen para evitar conflictos y creara las siguientes para nosotros:
* estados
* municipios
* colonias
El script se encarga de filtrar la información en bruto del archivo `CPdescarga.xls` y nos ordena la información en las tablas ya mencionadas.

## Correr la API

La API se desarrollo en Flask, si ya se ha declarado la variable `FLASK_APP` basta con ejecutar el siguiente comando `flask run` lo que ejecutara el API en nuestra PC.

En caso de que no corra la aplicación intentar con el siguiente comando `flask run --host=0.0.0.0` 

## autenticación

Para hacer uso de los endpoints se uso BasicAuth, cuyo usuario es `admin` y contraseña `password`. Si se usa la API desde el navegador automáticamente se lanzara un promt para ingresar los datos.  
Si se usa la api desde Postman o similares basta con poner el usuario y la contraseña en BasicAuth.

### Endpoints

* `http://127.0.0.1/api/cp` - Nos devuelve todos los códigos postales del país (tarda un poco en cargar todos)
* `http://127.0.0.1/api/cp/{numerocp}` - Al poner un código postal valido, nos devolverá **Código Postal - Nombre Colonia - Nombre Estado - Tipo Colonia - Tipo Zona**
* `http://127.0.0.1/api/estados` - Devuelve los estados con su numero de estado y su capital
* `http://127.0.0.1/api/estado/{estado}` - Busca en los estados si hay alguno que coincida con el endpoint
* `http://127.0.0.1/api/municipios` - Devuelve los municipios del país y el estado al que pertenecen
* `http://127.0.0.1/api/municipio/{municipio}` Busca en los municipios si hay alguno que coincida con el endpoint
* `http://127.0.0.1/api/colonias` Devuelve todas las colonias del país
* `http://127.0.0.1/api/colonia/{colonia}` Busca en las colonias si hay alguno que coincida con el endpoint
* `http://127.0.0.1/api/estado`**[POST]** - Permite mediante el método POST añadir un nuevo estado y ciudad mediante JSON, siguiendo la siguiente estructura:  

```json
[  
{"estado":"nombre_estado"},  
{"capital":"nombre_capital"}  
]
```


## Docker

también se creó una imagen del proyecto en Docker, el archivo `Dockerfile` muestra los comandos usados para crear dicha imagen.  
La imagen actualmente se encuentra en DockerHub en la siguiente liga: [DockerHub](https://hub.docker.com/r/danxvv/dockerhub/tags?page=1&ordering=last_updated)  
Para poder correr la imagen en un contenedor local se debe tener instalado Docker y ejecutar el siguiente comando:  
`docker run -dp 80:80 danxvv/dockerhub:deploy_image`

