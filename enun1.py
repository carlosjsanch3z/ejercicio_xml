#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Lista todos los nombres de los directorios

from lxml import etree

doc = etree.parse("zona-wifi.xml")

raiz = doc.getroot()

directorio = raiz.findall("directorio")

for d in directorio:
	nombres = d.findall("nombre")
	for n in nombres:
		print n.text
