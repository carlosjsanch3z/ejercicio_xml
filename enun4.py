#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4. Pide una subcadena y si coincide con el nombre de una de las categorias de 
#	un directorio, muestre el nombre de dichos directorios

from lxml import etree

doc = etree.parse("/home/charlie/Escritorio/GitHub/ejercicio_xml/zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")


for d in directorio:
	nombres = d.findall("nombre")
	categorias = d.findall("categorias")
	print "--------------------------"
	for c in categorias:
		categoria = c.findall("categoria")
		for ca in categoria:
			print ca.text 