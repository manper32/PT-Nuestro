# Prueba técnica NUESTRO
Este proyecto se creo con el fin de desarrollar la prueba técnica propuesta por por Nuestro la cual propone:
```
Desarrolle una aplicación web responsive que consulte los de comics del UMC y los liste alfabéticamente indicando por item titulo, imagen, creadores, series y año de creación.
```
Esto teniendo claro que se hizo uso de la documentación de las API [MARVEL](https://developer.marvel.com/docs)
## Debug
En primer lugar tener claro que debemos tener instalado un administrador de entornos de desarrollo de python3, ademas de  esto es importante crear el ambiente con la version precisada en el Pipfile.

En caso de tener pipenv instalado basta con crear una carpeta en la raíz del proyecto la cual se llame .venv, de este modo, las dependencias quedaran instaladas ahi, por ultimo ejecutar comando pipenv install, el cual tomara todos los requerimientos y los instalara de manera automática en el entorno.
## Variables de entorno
Para el correcto funcionamiento del proyecto, es necesario hacer el set de las siguientes variables de entorno, en un archivo nombrado .env, el cual tiene que estar ubicado en la raíz del proyecto, en caso de no tener intension de modificar la ruta de lectura de las variables de entorno:
- PUBLIC_KEY
- PRIVATE_KEY
- SECRET_KEY
- DEBUG

Las dos primeras variables son proveídas por MARVEL, la SECRET_KEY puede ser definida a gusto da la persona a ejecutar el proyecto.
## Autor
Manuel Alejandro Perez Padilla
## Recursos
- [POSTMAN](https://www.getpostman.com/collections/e8b3fd42063a94ed7ec1) (se comparte la coleccion en postman utilizada para hacer el desarrollo)