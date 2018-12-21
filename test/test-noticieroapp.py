# -*- coding: utf-8 -*-
import pytest, json, requests
import os
from requests import *
import sys
sys.path.append('../src/')

import tempfile
import pytest

url = 'https://noticiero-app.herokuapp.com/'

def test_raiz():
	response = requests.get(url)
	assert response.json()['status']=="OK", "Estado correcto"

def test_status():
	response = requests.get(url+'/status')
	assert response.json()['status']=="OK", "Estado correcto"

def test_noticiasUsuario():
	response = requests.get(url+'/noticia/usuario/')
	assert response.json()['status']=="OK", "Estado correcto"

def test_noticiasFecha():
	response = requests.get(url+'/noticia/fecha/')
	assert response.json()['status']=="OK", "Estado correcto"
