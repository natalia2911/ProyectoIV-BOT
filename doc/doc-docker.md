# DockerFile
Hemos usado Docker ya que nos permite aislar la aplicación, para que podamos hacer el despliege de manera muy sencilla y confiable, garantizando que dicho despliege sea escalable de forma eficiente sin importar el sistema operativo anfitrión.

Nuestro DockerFile se queda con el siguiente aspecto:

	FROM python:3

	MAINTAINER Natalia <nataliamartir@correo.ugr.es>
	WORKDIR src/
	COPY . .
	RUN pip install --no-cache-dir -r requirements.txt

	EXPOSE 80
	CMD cd src && gunicorn noticiero-app:app --log-file=- --bind 0.0.0.0:80

  Vamos a explicar a continuación cada uno los elementos usados:
   - *FROM* : imagen usada por nuestro contenedor en este caso Python 3
  - *MAINTAINER*: Establece los datos de autor/propietario del archivo Dockerfile
  - *WORKDIR*: Establece el directorio para las directivas de CMD que se ejecutarán.
  - *COPY*: Se copian todos los archivos de la aplicación.
  - *RUN*: Permite ejecutar una instrucción en el contenedor
  - *EXPOSE*: Asigna el puerto que usa el contenedor
  - *CMD*: Establece el comando de inicio del proceso que se usará si no se indica uno al iniciar un contenedor con la imagen

Nosotros primero hemos probado ha ejecutar el contenedor en local, para comprobar que no hubiera ningún fallo.

 ## Despliege en Heroku.
Hemos creado el archivo `heroku.yml`, nos permitirá que Heroku cree la imagen apartir del DockerFile.

Para crearlo:
Hemos seguido los pasos del [tutorial](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

Un vez subido el fichero a nuestro repositorio, hemos tenido que indicarle a Heroku que nuestra app era un contenedor, de esta manera:

`heroku stack:set container -a contenedornoticias`

y hemos actualizado con `git push heroku master`


 ## Creación de la imagen en DockerHub

[Imagen](https://hub.docker.com/r/natalia2911/proyectoiv-bot/)

Para usar la imagen directamente :
` docker run -it natalia2911/proyectoiv-bot`


Para crear la imagen, hemos entrado en la pagina: https://hub.docker.com/ y en la parte de create hemos elegido `Create Automatic Build` y hemos sincronizado con nuestro repositorio de Github.


 ## Ejemplos
 -	https://contenedornoticias.herokuapp.com/ : nos devuelve OK
 -	https://contenedornoticias.herokuapp.com/noticia/usuario/000102034847 : : Nos devuelve las noticias de un determinado usuario (En nuestro caso el usuario es un numero)
 -	https://contenedornoticias.herokuapp.com/noticia/fecha/2032018 : Nos devuelve una noticia de una determinada fecha
- https://contenedornoticias.herokuapp.com/noticia/fecha/1 : Vemos aquí una fecha que no esta, y por lo tanto sale como que la noticia es False
