#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2. Lista todos los nombre de los directorios y muestra el número de categorias que tiene en su menú de la página web.

from lxml import etree

doc = etree.parse("/home/charlie/Escritorio/GitHub/ejercicio_xml/zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")

for d in directorio:
	nombres = d.findall("nombre")
	categorias = d.findall("categorias")
	for n in nombres:
		for c in categorias:
			print "Lugar: " + n.text + "  Numero de categorias: " + str(len(c))  
			



