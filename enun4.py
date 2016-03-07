#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4. Pide una subcadena y si coincide con el nombre de una de las categorias de 
#	un directorio, muestre el nombre de dichos directorios

from lxml import etree

doc = etree.parse("zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")

var = raw_input("Subcadena: ")

for d in directorio:
	categorias = d.findall("categorias")
	for c in categorias:
		categoria = c.findall("categoria")
		for ca in categoria:
			if ca.text.startswith(var):
				padre = ca.getparent().getparent()
				nombre = padre.findtext("nombre")
				print nombre