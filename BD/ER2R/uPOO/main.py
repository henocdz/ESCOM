class AttrCompuesto(object):
	"""Define la clase para un objeto de atributo compuesto"""
	def __init__(self,obj):
		self.elem = obj
		elem = self.elem.replace('C(','')
		elem = elem.replace(')','')
		#Separar nombre de entidad compuesta y componentes
		nombre_atributos = elem.split(":")
		#Se obtiene nombre del principal
		self.nombre = nombre_atributos[0].replace('|','')
		#Genera los elemento de los cuales se compone el principal
		self.atributos = nombre_atributos[1].split(";")
		#atributos = atributos.replace(" ",'')
	def getAtributos(self,keyType):
		for atributo in self.atributos:
			yield [atributo,keyType]


class Vinculo(object):
	def __init__(self,v):
		pass


class EsquemaRelacional(object):
	def __init__(self,nombre):
		self.nombre
	def getPKs(self):
		pass

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

	def getPKs(nombreEntidad):
		for atributo in mRelacional[nombreEntidad]:
			if atributo.count('pk') > 0 or atributo.count('ppk') > 0:
				yield atributo

	for l in lineas:
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
			lenElementoLinea = len(elementoLinea)
			fChar = elementoLinea[0]
			lChar = elementoLinea[lenElementoLinea-1]

			if fChar == '"' and lChar == '"':
				nombreEntidad = elementoLinea.replace('"','')
				entidades.append(nombreEntidad)
				mRelacional[nombreEntidad] = []
			elif fChar=='{' and lChar == '}':
				nombreAtributo = elementoLinea.replace('{','').replace('}','')
				if nombreAtributo[0] == "C" and nombreAtributo[1] == "(" and nombreAtributo[len(nombreAtributo)-1]	== ")":
					compuesto = AttrCompuesto(nombreAtributo)
					for atributo in compuesto.getAtributos("pk"):
						mRelacional[nombreEntidad].append(atributo)
				else:
					mRelacional[nombreEntidad].append([nombreAtributo,'pk'])
			elif fChar == '[' and lChar == ']':
				nombreAtributo = elementoLinea.replace('[','').replace(']','')

				if nombreAtributo[0] == "C" and nombreAtributo[1] == "(" and nombreAtributo[len(nombreAtributo)-1]	== ")":
					compuesto = AttrCompuesto(nombreAtributo)
					for atributo in compuesto.getAtributos('ppk'):
						mRelacional[nombreEntidad].append(atributo)
				else:
					mRelacional[nombreEntidad].append([nombreAtributo,'ppk'])
			elif fChar == "C" and elementoLinea[1] == "(" and lChar	== ")":
				compuesto = AttrCompuesto(elementoLinea)
				for atributo in compuesto.getAtributos('a'):
					mRelacional[nombreEntidad].append(atributo)
			elif fChar == '*' and lChar == '*':
				nombreAtributo = elementoLinea.replace('*','').replace('*','')

				if nombreAtributo[0] == 'C' and nombreAtributo[1] == '(' and nombreAtributo[len(nombreAtributo)-1] == ')':
					compuesto = AttrCompuesto(nombreAtributo)
					mRelacional[compuesto.nombre] = []
					for atributo in compuesto.getAtributos('pk'):
						mRelacional[compuesto.nombre].append(atributo)
				else:
					mRelacional[nombreAtributo] = []
					for pk in getPKs(nombreEntidad):
						mRelacional[nombreAtributo].append(pk)
			else:
				nombreAtributo = elementoLinea
				mRelacional[nombreEntidad].append([nombreAtributo,'a'])

	for v in lineasVinculos:
		(cu,cd,pu,pd) = ('','','','')

		elementoVinculo = v.split(',')
		nombreVinculo = elementoVinculo[0].replace('"','')


	print mRelacional

transformar('../format.bd')