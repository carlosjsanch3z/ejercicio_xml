#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. Introduce un identificador, si existe muestre toda la información del directorio, si no, que muestre un mensaje de error.

from lxml import etree

doc = etree.parse("/home/charlie/Escritorio/GitHub/ejercicio_xml/zona-wifi.xml")

raiz = doc.getroot()

identificador = raw_input("Introduce un identificador: ")

directorio = raiz.findall("directorio")

comodin = False

for i in directorio:
	ids = i.findall("identificador")
	for o in ids:
		print o.text
'''
if comodin == False:
	print "Error"
'''