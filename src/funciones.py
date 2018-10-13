#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from datetime import datetime, date, time, timedelta
import calendar

class Noticias:

		def __init__(self):
			with open('noticias.json', 'r') as f:
				self.data = json.load(f)

		def getNoticiasFecha(self, fecha):
			noticia = []
			for i in self.data:
				if i["fecha"] == fecha:
					for j in i["noticia"]:
						noticia.append(j)
				if not noticia: noticia = False 

			return noticia
			

		def getNoticiasUsuario(self, usuario):
			noticia = []
			try:
				for i in self.data[usuario-1]["noticia"]:
					noticia.append(i["noticia"])
			except:
					noticia = False

				return noticia

		def setNoticia(self, usuario, noticia):
			fecha = date.today()
			try:
				self.data[usuario-1]["noticia"].append({'usuario': usuario,'fecha': fecha, 'noticia': noticia})
				#with open('noticias.json', 'w') as f:
					#json.dump(self.data, f)
				return True
			except:
				return False

