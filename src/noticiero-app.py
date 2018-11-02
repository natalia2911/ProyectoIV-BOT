#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import funciones

app = Flask(__name__)

@app.route('/')
def inicio():
	return jsonify(status="Ok")

@app.route('/noticia/<usuario>')
def Noticias(usuario):
	n=funciones.Noticias()
	datos=n.getNoticiasUsuario(usuario)
	return jsonify(noticia=datos)
    
@app.route('/noticias/<fecha>')
def Noticias(fecha):
	n=funciones.Noticias()
	datos=n.getNoticiasFecha(fecha)
	return jsonify(noticia=datos)

@app.errorhandler(404)
def page_not_found(error):
    return 'error HTTP 404, not found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)