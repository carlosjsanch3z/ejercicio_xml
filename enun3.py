#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. Introduce un identificador, si existe muestre toda la información del directorio, si no, que muestre un mensaje de error.

from lxml import etree

doc = etree.parse("zona-wifi.xml")

raiz = doc.getroot()

comodin = False

identificador = raw_input("Introduce un identificador: ")

directorio = raiz.findall("directorio")



for i in directorio:
	ids = i.findall("identificador")
	for o in ids:
		if identificador == o.text:
			comodin = True
			print "	Nombre: " + i.findtext("nombre")
			print "	Telefono: " + i.findtext("telefono")
			print "	Fax: " + i.findtext("fax")
			print "	Correo electronico: " + i.findtext("correo-electronico")
			print "	Horario: " + i.findtext("horario")
			print "	Localización: " + i.findtext("localizacion")

if comodin == False:
	print "	Error: Identificador no encontrado."
