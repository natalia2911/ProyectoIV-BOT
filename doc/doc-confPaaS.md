# Despliege y configuración de un PaaS - Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

En este caso el despliege lo vamos a hacer en Heroku.

Heroku es una plataforma como servicio de computación en la Nube que soporta distintos lenguajes de programación.
Heroku es propiedad de Salesforce.com.1​ Heroku, es una de las primeras plataformas de computación en la nube. Para más info
 [Pincha aquí](https://es.wikipedia.org/wiki/Heroku)
 [Accede a Heroku](https://www.heroku.com/)

 Para hacer el despliegue, seguimos los siguientes pasos:

 ## Pasos:

1. Tenemos que hacernos una cuenta en Heroku, en la que tenemos que poner nuestro correo y datos personales.
2. Tenemos que crear una nueva aplicación
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-1.png)

	Tenemos que ponerle el nombre de la aplicación, en este caso vamos a poner `noticiero-app`

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-2.png)

3. Tenemos que crear un documento con los Dynos que se llama `Procfile`

Este documento sirve para indicar que comando se debe ejecutar.
Este debe estar en la raíz del proyecto.
En el nuestro tenemos esta linea:
`web: cd src && gunicorn noticiero-app:app --log-file -`
Nos indica que el fichero en python donde se realiza el despligue.

Usamos el comando `gunicorn` para el despliegue de la aplicación ya que `gunicorn` es un programa con la versión mas poderosa del comando de django, por lo que incrementará el rendimiento de la misma.

Para poder usar este comando tenemos que instalarlo con pip

4. Tenemos que asociar Github con Heroku, también tenemos que indicarle que realice el despliegue automático.
		4.1 Vamos a `Deploy`
		4.2 En `Deployment method`  seleccionamos Github (Aquí nos pedirán que busquemos el repositorio y lo conectemos, que accedamos a Github y que permitamos el acceso a Heroku)
		4.3 Activamos `Automatic deploys` y marcamos la casilla `Wait for CI to pass before deploy`

Así es como quedaría después de realizar estos pasos:
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-4.png)

5. Hacemos el primer despliegue:

Para hacer el primer despliegue le damos a `Deploy Branch`

Tenemos que tener la aplicación en la linea de comandos, con el cliente de Heroku.

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-5.png)


6. Aquí tenemos una serie de ejemplos de funcionamiento.

-   https://noticiero-app.herokuapp.com/ : nos devuelve {status="Ok"}
-   https://noticiero-app.herokuapp.com/noticia/usuario/000102034847 : Nos devuelve las noticias de un determinado usuario (En nuestro caso el usuario es un numero)
-   https://noticiero-app.herokuapp.com/noticia/fecha/2032018 : Nos devuelve una noticia de una determinada fecha
-   https://noticiero-app.herokuapp.com/noticia/fecha/1 : Vemos aquí una fecha que no esta, y por lo tanto sale como que la noticia es False


![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-6.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-7.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/hito3-8.png)
