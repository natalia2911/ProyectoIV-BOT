from fabric.api import *
from fabric.contrib.console import confirm
import os


# Definimos una variable de entorno con el host al que nos vamos a conectar
# y el nombre de usuario
env.user = "vagrant"
env.host = ['noticieroapp.westeurope.cloudapp.azure.com']


def Desinstalar():
	#Borramos el codigo antiguo
	run("sudo rm -rf ./ProyectoIV-BOT")

def Instalar():
	#Instalamos el servicio clonando eliminando el codigo anterior e instalando los requerimientos
	Desinstalar()
	run("git clone https://github.com/natalia2911/ProyectoIV-BOT")
	run('cd ProyectoIV-BOT/  && sudo pip3 install -r requirements.txt')


def Iniciar():
	#Iniciamos el servicio
	with cd("ProyectoIV-BOT/src/"):
		sudo("gunicorn noticiero-app:app --log-file - &")
