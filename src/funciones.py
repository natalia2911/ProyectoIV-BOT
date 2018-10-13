#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from datetime import datetime, date, time, timedelta
import calendar

class Noticias:

		def __init__(self):
			with open('noticias.json', 'r') as f:
				self.ap = json.load(f)

		def getNoticiasFecha(self, fecha):
			noticia = []
			for i in self.ap:
				if i["fecha"] == fecha:
					for j in i["noticia"]:
						noticia.append(j)
				if not noticia: noticia = False 
			return noticia
			

		def getNoticiasUsuario(self, usuario):
			noticia = []
			try:
				for i in self.ap[usuario-1]["noticia"]:
					noticia.append(i["noticia"])
			except:
					noticia = False
			return noticia

		def setNoticia(self, usuario, noticia):
			fecha = date.today()
			try:
				self.ap[usuario-1]["noticia"].append({"usuario":usuario, "fecha":fecha, "noticia":noticia})
				with open('noticias.json', 'w') as f:
					json.dump(self.ap, f)
				return True
			except:
				return False



