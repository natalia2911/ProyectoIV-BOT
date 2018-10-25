
# Integración Continua

La integración continua es un modelo que consiste en hacer integraciones automáticas de un proyecto lo más a menudo posible para así poder detectar fallos cuanto antes

Para poder detectar dichos fallos usaremos una seria de test basandonos en `Travis CI`

Para realizar los test es necesario ejecutar el fichero `test.py`, tras instalarlo

- Para instalarlo lo que tenemos que hacer es ir:
	1. Tenemos que ir a la página de [Travis-CI](https://travis-ci.com/)
	2. Tenemos que seleccionar nuestro proyecto para que pueda pasar los test.
	3. Tenemos que añadir un fichero de configuración que nos indique que el lenguaje es python, e instalar el fichero de `requirements.txt`; Este fichero de configuración será `.travis.yml`

	![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/ejemplo2.png)


# Test 

Los test que hemos usado para poder incluir la integración continua es:
	
 - `testFecha`: comprueba que la fecha tenga el formato aaaa-mm-dd por lo que no puede ser ni una cadena, ni un número suelto.
 - `testUsuario`: nosotros hemos prefijado que el usuario sea un número, por lo que no pude ser una cadena.
-  `testAniadirNoticia`: para poder añadir una noticia, la fecha que ponemos se pone dentro del set como la fecha actual de día, ya que nosotros no hemos puesto la fecha como la fecha del suceso si no como la fecha de públicación de la misma. Esta tiene que cumplir que el usuario sea un número y la noticia una cadena.

Hemos añadido en la descripción principal un indicador que nos dice que el test ha sido pasado.
	
Aquí podemos ver un ejemplo de como funciona el test con Travis.
	![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/ejemplo1.png)
