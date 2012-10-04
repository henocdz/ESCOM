import vinculos,atributos,re

#from Benchmark.benchrun import *

def archivoExiste(f):
	def checarArchivo(*args,**kwargs):
		try:
			arch = open(args[0])
			flag = True
		except:
			flag = False
			print "Error al abrir archivo"

		if flag:
			f(*args,**kwargs)

	return checarArchivo


@archivoExiste
def transformar(archivo):

	try:
		f = open(archivo)
	except:
		print "Error Critico, no se puede continuar"
		exit()

	lineas = f.readlines()

	mRelacional = {}
	entidades = []
	lineasVinculos = []
	leyendoVinculos = False

	vinculosEnearios = []
	vinculos11 = []
	vinculos1N = []
	vinculosMN = []

	def getPKs(nombreEntidad):
		for atributo in mRelacional[nombreEntidad]:
			if atributo.count('pk') > 0 or atributo.count('ppk') > 0:
				yield atributo

	(ll,ee) = (0,0)

	for l in lineas:
		ll += 1
		ee = 0
		l = l.replace("\n",'')
		partesLinea = l.split(',')
		nombreEntidad = '';

		if l == '/vinculos':
			leyendoVinculos = True
			continue
		elif l == '':
			continue

		if leyendoVinculos:
			lineasVinculos.append(l)
			continue

		#Leyendo elementos por linea
		for elementoLinea in partesLinea:
			ee += 1

			lenElementoLinea = len(elementoLinea)
			fChar = elementoLinea[0]
			lChar = elementoLinea[lenElementoLinea-1]

			if fChar == 'D' and elementoLinea[1] == "(" and lChar == ')':
				nombres = (elementoLinea.replace('D(','').replace(')','')).split("|")
				nombreEntidad = nombres[0].replace('"','')
				nombrePropietaria = nombres[1].replace('"','')
				entidades.append(nombreEntidad)
				mRelacional[nombreEntidad] = []

				try:
					for p in mRelacional[nombrePropietaria]:
						if p[1].find('pk') >= 0 :
							mRelacional[nombreEntidad].append([p[0],"pk:"+nombrePropietaria])
				except:
					print "Tipo de entidad no encontrado Linea: ",ll," Elemento: ",ee
					exit()
			elif fChar == '"' and lChar == '"':
				nombreEntidad = elementoLinea.replace('"','')
				entidades.append(nombreEntidad)
				mRelacional[nombreEntidad] = []
			elif fChar=='{' and lChar == '}':
				nombreAtributo = elementoLinea.replace('{','').replace('}','')
				if nombreAtributo[0] == "C" and nombreAtributo[1] == "(" and nombreAtributo[len(nombreAtributo)-1]	== ")":
					compuesto = atributos.Compuesto(nombreAtributo)
					for atributo in compuesto.getAtributos("pk"):
						mRelacional[nombreEntidad].append(atributo)
				else:
					mRelacional[nombreEntidad].append([nombreAtributo,'pk'])
			elif fChar == '[' and lChar == ']':
				nombreAtributo = elementoLinea.replace('[','').replace(']','')

				if nombreAtributo[0] == "C" and nombreAtributo[1] == "(" and nombreAtributo[len(nombreAtributo)-1]	== ")":
					compuesto = atributos.Compuesto(nombreAtributo)
					for atributo in compuesto.getAtributos('ppk'):
						mRelacional[nombreEntidad].append(atributo)
				else:
					mRelacional[nombreEntidad].append([nombreAtributo,'ppk'])
			elif fChar == "C" and elementoLinea[1] == "(" and lChar	== ")":
				compuesto = atributos.Compuesto(elementoLinea)
				for atributo in compuesto.getAtributos('a'):
					mRelacional[nombreEntidad].append(atributo)
			elif fChar == '*' and lChar == '*':
				nombreAtributo = elementoLinea.replace('*','').replace('*','')

				if nombreAtributo[0] == 'C' and nombreAtributo[1] == '(' and nombreAtributo[len(nombreAtributo)-1] == ')':
					compuesto = atributos.Compuesto(nombreAtributo)
					mRelacional[compuesto.nombre] = []
					for atributo in compuesto.getAtributos('pk'):
						mRelacional[compuesto.nombre].append(atributo)
					for pk in getPKs(nombreEntidad):
						mRelacional[compuesto.nombre].append(pk)
				else:
					mRelacional[nombreAtributo] = [[nombreAtributo,'pk']]
					for pk in getPKs(nombreEntidad):
						mRelacional[nombreAtributo].append(pk)
			else:
				nombreAtributo = elementoLinea
				mRelacional[nombreEntidad].append([nombreAtributo,'a'])

	for v in lineasVinculos:
		(cu,cd,pu,pd) = ('','','','')

		elementoVinculo = v.split(',')

		relaciones = elementoVinculo[1].lower()
		relaciones = relaciones.split('u')

		if len(relaciones)>1:
			vinculosEnearios.append(vinculos.VinculoEneario(v,entidades))
			continue

		i = 0;
		for c in elementoVinculo[2]:
			i += 1
			c = c.lower()
			if c == 'p' or c == 't':
				if i==1:
					pu = c
				elif i==3:
					pd = c
			elif c == '1':
				if(i==2):
					cu = '1'
				else:
					cd = '1'
			elif c=='n' or c=='m':
				if(i==2):
					cu = 'n'
				else:
					cd = 'n'

		if (cu == '1' and cd == 'n') or (cu=='n' and cd=='1'):
			vinculos1N.append(vinculos.Vinculo(v,entidades,[cu,cd],[pu,pd]))
		elif cu=='n' and cd=='n':
			vinculosMN.append(vinculos.Vinculo(v,entidades,[cu,cd],[pu,pd]))
		elif cu=='1' and cd=='1':
			vinculos11.append(vinculos.Vinculo(v,entidades,[cu,cd],[pu,pd]))
	

	#Paso 3
	for uu in vinculos11:
		mRelacional = uu.format(mRelacional)

	#Paso 4
	for nu in vinculos1N:
		mRelacional = nu.format(mRelacional)

	#Paso 5
	for nm in vinculosMN:
		mRelacional = nm.format(mRelacional)

	#Paso 6
	for eneario in vinculosEnearios:
		mRelacional[eneario.nombre] = eneario.getKeys(mRelacional)

	for r in mRelacional:
		print mRelacional[r]
	imprimir(mRelacional)


def imprimir(mr):
	ce = ""
	for r in mr:
		
		ce += "\n"+r+" => \n    "

		for attr in mr[r]:
			if  attr[1].find('ppk:') >= 0 or attr[1].find('pk:') >= 0 or attr[1].find("fk:")>=0:
				s = attr[1].split(":")
				if s[0] == "ppk":
					s[0] = s[0][1:]
				ce += "["+s[0].replace(':','').upper()+"] /=> "+s[1]+"."+attr[0]+ "    "
			elif  attr[1].find('ppk') >= 0 or attr[1].find('pk') >= 0 or attr[1].find("fk")>=0:
				s = attr[1]
				if s == "ppk":
					s = s[1:]
				ce += "["+s.replace(':','').upper()+"] /=> "+attr[0]+ "    "
			else:
				ce += attr[0]+"    "

		ce = ce[:-2]
		ce += "\n"

	try:
		f = open('output.txt','w')
		f.write(ce)
		f.close()
	except:
		print "\n\t|!| ERROR: Imposible crear archivo. Se muestra a continuacion: \n"
		print ce
	else:
		print "\n\t>>>Se ha guardado el archivo output.txt exitosamente \n"


#Ignoren esto x)
"""
with Timer():
	transformar('format.bd')
"""


def goahead():
	transformar(raw_input("Introduzca el archivo a transformar (*.bd): "))
while 1:
	goahead()