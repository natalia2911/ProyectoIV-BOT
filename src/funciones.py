#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from datetime import datetime, date, time, timedelta
import calendar
import os


class Noticias:

		def __init__(self):
			with open('noticias.json', 'r') as f:
				self.noticias = json.load(f)

		def getNoticiasFecha(self, fecha):
			noticia = []
			for i in self.noticias:
				if i["fecha"] == fecha:
					for j in i["noticia"]:
						noticia.append(j)
				if not noticia: noticia = False
			return noticia

		def getNoticiasUsuario(self, usuario):
			noticia = []
			for i in self.noticias:
				if i["usuario"] == usuario:
					for j in i["noticia"]:
						noticia.append(j)
				if not noticia: noticia = False
			return noticia

		def setNoticia(self, usuario, noticia, nNoticia):

			if len(self.noticias) > nNoticia and nNoticia >=0:
				fecha = date.today()

				self.noticias["nNoticia"]["usuario"] = usuario
				self.noticias["nNoticia"]["fecha"] = fecha
				self.noticias["nNoticia"]["noticia"] = noticia

				with open('noticias.json', 'w') as f:
					json.dump(self.noticias, f)
				return True
			else:
				return False
