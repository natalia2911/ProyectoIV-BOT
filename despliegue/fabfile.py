from fabric.api import run, sudo, env, shell_env
import os

def Desinstalar():
	sudo("sudo rm -rf ./ProyectoIV-BOT")

def Instalar():
	run("git clone https://github.com/natalia2911/ProyectoIV-BOT")
	run('cd ProyectoIV-BOT/  && sudo pip3 install -r requirements.txt')

def Iniciar():
	run('cd ~/ProyectoIV-BOT/src/ && sudo gunicorn noticiero-app:app -b 0.0.0.0:80 --log-file=-')
