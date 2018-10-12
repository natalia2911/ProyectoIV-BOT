# Integración Continua

Los test que hemos usado para poder incluir la integración continua es:
	- `testFecha`: comprueba que la fecha tenga el formato aaaa-mm-dd por lo que no puede ser ni una cadena, ni un número suelto.
	- `testUsuario`: nosotros hemos prefijado que el usuario sea un número, por lo que no pude ser una cadena.
	- `testAniadirNoticia`: para poder añadir una noticia, la fecha que ponemos se pone dentro del set como la fecha actual de día, ya que nosotros no hemos puesto la fecha como la fecha del suceso si no como la fecha de públicación de la misma. Esta tiene que cumplir que el usuario sea un número y la noticia una cadena.
	
Aquí podemos ver un ejemplo de como funciona el test con Travis.
	![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/ejemplo1.png)