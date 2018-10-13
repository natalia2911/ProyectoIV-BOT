[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.org/natalia2911/ProyectoIV-BOT.svg?branch=master)](https://travis-ci.org/natalia2911/ProyectoIV-BOT)

# Proyecto IV : Bot Noticiero 

Repositorio creado para la asignatura de Infraestructura Virtual, de 4º curso, en el grado de Ingeniería Informática (GII) de la Universidad de Granada (UGR) en el curso 2018-2019

## Descripción

Mi proyecto para este curso se basará en crear un microservicio en la nube el cual será usado por un bot de Telegram que nos indique las noticias del día o de días anteriores.
Nuestro usuario podrá consultar las noticias de diferentes días, según la petición propia del usuario.

## Herramientas

- El lenguaje en que programaremos nuestro proyecto será en Python. He decidido usar este lenguaje ya que es un lenguaje que actualmente está en auge y creo que podría aportarme muchas cosas aprenderlo en profundidad.

- Para realizar este proyecto usaremos un entorno virtual de desarrollo adecuado a python el cual será `virtualenv` para más información sobre este entorno de desarrollo [pinche aquí](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-entornovirtual.md).


- Hemos pensado en usar un determinado editor de texto, en este caso será Atom ([Más información](https://atom.io/) 

- Será gestionado por una base de datos donde almacenemos todo tipo de noticias, podremos usar tanto [MySQL](https://www.mysql.com/), como [MariaDB](https://mariadb.org/), aun no lo tenemos completamente definido.

- Para realizar el testeo vamos a utilizar la librería `unittest` por su gran variedad de funcionalidades. [Más información](https://docs.python.org/3/library/unittest.html)

- El micro-framework que vamos a usar será `Flask` ya que me parece que será una buena herramienta para usar con Python, para desarrollar nuestro microservicio.

- Ahora mismo utilizaremos `ficheros JSON` para el almacenamiento estatico, más tarde procederemos a implementar la BBDD.

- Para realizar los test usaremos [Travis-CI](https://travis-ci.org/)


## Integración Continua

La integración continua es un modelo que consiste en hacer integraciones automáticas de un proyecto lo más a menudo posible para así poder detectar fallos cuanto antes

Para poder detectar dichos fallos usaremos una seria de test basandonos en `Travis CI`

Para hacer realizar los test vamos a usar `funciones.py` donde podremos obtener todas las noticias de un determinado día, las noticias que un usuario público, añadir una noticia a la lista de noticias.

Para realizar los test es necesario ejecutar el fichero `test.py`, tras instalarlo

- Para instalarlo lo que tenemos que hacer es ir:
	1. Tenemos que ir a la página de [Travis-CI](https://travis-ci.com/)
	2. Tenemos que seleccionar nuestro proyecto para que pueda pasar los test.
	3. Tenemos que añadir un fichero de configuración que nos indique que el lenguaje es python, e instalar el fichero de `requirements.txt`

	Para más información ir a: [más info](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-integracionCont.md)








