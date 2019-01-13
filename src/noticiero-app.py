from flask import Flask, jsonify
import funciones

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def inicio():
	return jsonify(status="Ok")

@app.route('/status',  methods = ['GET'])
def status():
	return jsonify(status="OK")

@app.route('/noticia/usuario/<usuario>', methods = ['GET'])
def Noticias_1(usuario):
	n=funciones.Noticias()
	datos=n.getNoticiasUsuario(usuario)
	return jsonify(noticia=datos)

@app.route('/noticia/fecha/<fecha>', methods = ['GET'])
def Noticias_2(fecha):
	n=funciones.Noticias()
	datos=n.getNoticiasFecha(fecha)
	return jsonify(noticia=datos)
