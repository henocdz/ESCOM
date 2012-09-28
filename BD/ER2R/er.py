# -*- coding: UTF-8 -*-

import os
def archivoExiste(f):
	def checarArchivo(*args,**kwargs):
		try:
			arch = open(args[0])
			flag = True
		except:
			flag = False
			print "Error al abrir archivo"
			#limpiar()

		if flag:
			f(*args,**kwargs)

	return checarArchivo


@archivoExiste
def transformar(archivo):
	#EsquemaDeRelacion
	modR = {}

	#Abrir archivo
	f = open(archivo)

	#Todas las lineas del archivo
	lineas = f.readlines()

	#Esquemas de Relacion
	entities = []
	#Cuando se llegue a vinculos
	vinc = False
	#Guardar vinculos
	vinculos = []


	def compuestoAddAttr(relacion,elem,k="na"):
		ncomp = elem.replace('C(','')
		ncomp = ncomp.replace(')','')
		#Separar nombre de entidad compuesta y componentes
		ecomp = ncomp.split(":")
		#Se obtiene nombre del principal
		nomEcomp = ecomp[0].replace('|','')
		#Genera los elemento de los cuales se compone el principal
		cC = ecomp[1].split(";")
		for component in cC:
			modR[nentidad].append([component,k])

	def compuestoReturnAttr(elem):
		ncomp = elem.replace('C(','')
		ncomp = ncomp.replace(')','')
		#Separar nombre de entidad compuesta y componentes
		ecomp = ncomp.split(":")
		#Se obtiene nombre del principal
		nomEcomp = ecomp[0].replace('|','')
		#Genera los elemento de los cuales se compone el principal
		cC = ecomp[1].split(";")
		for component in cC:
			yield (component,nomEcomp)

	#Analizar entidades
	for l in lineas:
		#Se recorre cada elemento del formado, separado por (,)
		elemento = l.split(",")

		#limpiar caracteres de escape
		l = l.replace('\n','')
		#Si se llega a la linea de vinculos se guarda el resto del doc en una nueva lista
		if l == "/vinculos":
			vinc = True
			continue
		#Si se encuentra una linea vacia, se ignora
		elif l == "":
			continue

		#Si ya se estan leyendo vinculos, se guardan y se ignora el resto de la funcion
		if vinc:
			vinculos.append(l)
			continue

		#Se guardara nombre de la entidad que se esta iterando
		nentidad = ""

		#Se recorren los elementos individuales de la linea
		for elem in elemento:

			#Se elimina el caracter final de la linea
			elem = elem.replace("\n",'')

			#Si el primer caracter es una comilla, es el nombre de entidad
			if elem[0] == '"':

				nentidad = elem.replace('"','')
				modR[nentidad] = []
				entities.append(nentidad)
			#Si el primer caracter es una llame, es una PK
			elif elem[0] == "{":
				# nattr almecenara el nombre del atributo, temporal
				nattr = elem.replace('{','')
				nattr = nattr.replace('}','')
				#Se agrega el atributo como PK al diccionario corresopndiente
				modR[nentidad].append([nattr,'pk'])
			#Si el primer caracter es un corchete, es una llave parcial
			elif elem[0] == "[":
				nattr = elem.replace('[','')
				nattr = nattr.replace(']','')

				#Se evalua si el primer elemento es compuesto
				if nattr[0] == "C" and nattr[1] == "(":
					compuestoAddAttr(nentidad,nattr,'ppk')
				else:
					modR[nentidad].append([nattr,'ppk'])
			#Elemento compuesto
			elif elem[0] == "C" and elem[1] == "(":
				compuestoAddAttr(nentidad,elem)
			#Si el primer caracter es un asterisco, es multivaluado
			elif elem[0] == "*":
				elem = elem.replace('*','')
				#Se crea nuevo esqema relacional
				if elem[0] == "C" and elem[1] == "(":
					nombreEsquema = compuestoReturnAttr(elem).next()[1]
					modR[nombreEsquema] = []

					for item in compuestoReturnAttr(elem):
						modR[nombreEsquema].append([item[0],'pk'])

				else:
					modR[elem] = []
					for pk in modR[nentidad]:
						if pk.count('pk') > 0 or pk.count('ppk') > 0:
							modR[elem].append(pk)
			#Si no es cualquiera de estos, es un atributo cualquiera
			else:
				nattr = elem
				modR[nentidad].append([nattr,'na'])

	#Se recorren los vinculos
	for v in vinculos:
		card1 = ""
		card2 = ""
		participantes = 0

		v = v.split(',')
		primera = int(v[1][0])
		segunda = int(v[1][2])

		nombreVinculo = v[0].replace('"','')

		v[1] = v[1].lower()
		if v[1].split('u','') > 0:
			#vinculo eneario
			pass

		i = 0;
		for e in v[2]:
			i += 1
			e = e.lower()
			if e == 'p' or e == 't':
				continue
			elif e == '1':
				if(i==2):
					card1 = '1'
				else:
					card2 = '1'
			elif e=='n' or e=='m':
				if(i==2):
					card1 = 'n'
				else:
					card2 = 'n'

		prim = entities[primera]
		seg = entities[segunda]


		#Convierte N:1
		if (card1 == '1' and card2 == 'n'):
			#Si la entidad tiene PK, se pediran como FK; 
			#sino, se pediran como PK
			pks = entityHasPK(modR,seg)
			for pk in obtenerClaves(modR,prim,pks):
				modR[seg].append(pk)
		#Convierte 1:N
		elif (card1 == 'n' and card2 == '1'):
			#Si la entidad tiene PK, se pediran como FK; 
			#sino, se pediran como PK
			pks = entityHasPK(modR,prim)
			for pk in obtenerClaves(modR,seg,pks):
				modR[prim].append(pk)
		#Convertir M:N
		elif card1 == 'n' and card2 == 'n':
			modR[nombreVinculo] = []
			for pk in obtenerClavesMN(modR,prim):
				modR[nombreVinculo].append(pk)
			for pk in obtenerClavesMN(modR,seg):
				modR[nombreVinculo].append(pk)

	for relacion in modR:
		print relacion," => "
		for attr in modR[relacion]:
			print "\t",attr

#Obtiene llaves de la entidad, cuando se utilizara para 1:N,N:1
#Se le indica si las requiere como PK o solo FK
def obtenerClaves(l,k,pks):
	for e in l[k]:
		if e.count('pk') > 0 and (not pks):
			yield e
		elif e.count('pk') > 0 and pks:
			yield [e[0],'na_'+k]
#Obtiene llaves de la entidad, cuando se utilizara para M:N
def obtenerClavesMN(l,k):
	for e in l[k]:
		if e.count('pk') > 0 or e.count('ppk'):
			yield [e[0],'pk_'+k]

#Busca si una entidad tiene PK
def entityHasPK(l,k):
	for e in l[k]:
		if e.count('pk') > 0:
			return True
	return False

print """
Bienvenido!

"""


#transformar("format.bd")
def goahead():
	transformar(raw_input("Introduzca el archivo a transformar (*.bd): "))
while 1:
	goahead()