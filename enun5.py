#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 5.Muestra solamente los nombres de los directorios en los que 
#	el tipo de atributo sea igual a "Zona Wifi,Comunicaciones"


from lxml import etree

doc = etree.parse("/home/charlie/Escritorio/GitHub/ejercicio_xml/zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")

for d in directorio:
	if d.attrib.get("tipo") == "Zona Wifi,Comunicaciones":
		print d.findtext("nombre")