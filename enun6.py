#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 6. Un programa que pida una categoria y genere un fichero html que muestre : el nombre, el horario y una img de la zona wifi.

from lxml import etree

doc = etree.parse("zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")

var = raw_input("Subcadena: ")
lista=[]
dicc= {}
for d in directorio:
	categorias = d.findall("categorias")
	for c in categorias:
		categoria = c.findall("categoria")
		for ca in categoria:
			if ca.text.startswith(var):
				padre = ca.getparent().getparent()
				nombre = padre.findtext("nombre")
				horario = padre.findtext("horario")
				imagen = padre.findtext("foto")
			
				
				nombre = nombre.encode('utf-8')
				horario = horario.encode('utf-8')

				dicc["nombre"]=nombre
				dicc["horario"]=horario
				dicc["imagen"]=imagen
				lista.append(dicc)
				dicc = {}


with open ("wifis.html", "w") as archivo:

	for elemento in lista:
		archivo.write("<h1>"+elemento["nombre"]+"</h1>"+"\n")
		archivo.write("<p>"+elemento["horario"]+"</p>"+"\n")
		archivo.write("<img src="+str(elemento["imagen"])+"/>"+"\n")



