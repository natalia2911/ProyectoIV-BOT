#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import funciones
import pytest
import sys, os.path

src = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src)

from funciones import Noticias

class Tests(unittest.TestCase):

	test = funciones.Noticias()
	if __name__ == '__main__':
		unittest.main()

	def testFecha(self):
		self.assertEqual(self.test.getNoticiasFecha(1),False,"No puede ser un número, debe ser una fecha")
		self.assertEqual(self.test.getNoticiasFecha("cadena"),False,"No puede ser una cadena, debe ser una fecha")
		self.assertEqual(self.test.getNoticiasFecha(2018-10-11),[str('El próximo 20 de enero de celebrará una fiesta en nombre de un profesor'),
			str('Antes del dia 10 de octubre deben estar asignados los TFG de la promoción 18-19')],
			"La fecha es correcta")


	def testUsuario(self):
		self.assertEqual(self.test.getNoticiasUsuario("cadena"),False,"No puede ser una cadena, debe ser un número")
		self.assertEqual(self.test.getNoticiasUsuario("1"),str('Marcos, es el mejor alumno de la clase'),"El usuario es correcto")

	def testAniadirNoticia(self):
		self.assertEqual(self.test.setNoticia("cadena","cadena",3),False,"El usuario no puede ser una cadena, tiene que ser un número")
		self.assertEqual(self.test.setNoticia("0","0",3),False,"La noticia no puede ser un entero")
		self.assertEqual(self.test.setNoticia("10","Habrá una fiesta de la escuela el día 9",3),True,"La noticia se ha añadido de forma correcta")
