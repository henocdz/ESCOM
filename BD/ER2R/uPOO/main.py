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
	def __init__(self,lineasVinculo,entidades,cardinalidad,participacion):
		self.bk = lineasVinculo
		self.elementos = (self.bk).split(',')

		self.nombre = self.elementos[0]
		self.v = (self.elementos[1]).replace('d','r')
		self.v = (self.v).split('r')
		self.c = cardinalidad
		self.p = participacion
		#entidades

		try:
			self.eu = entidades[int(self.v[0])]
			self.ed = entidades[int(self.v[1])]
		except:
			raise TypeError

		nombreL = len(self.nombre)
		if self.nombre[0] == '"' and self.nombre[nombreL-1] == '"':
			self.nombre = (self.nombre).replace('"','').replace('"','')
		else:
			raise SyntaxError

		if len(self.elementos) > 3:
			self.atributos = self.elementos[3]
		else:
			self.atributos = []
	def format(self,mRelacional):
		self.newRelacional = mRelacional

		if self.c[0] == '1' and self.c[1] == 'n':
			for pk in self.getPKs(self.eu):
				if self.hasPKs(self.ed):
					pk[1] = 'fk_',self.eu
				(self.newRelacional[self.ed]).append(pk)
		elif self.c[0] == 'n' and self.c[1] == '1':
			for pk in self.getPKs(self.ed):
				if self.hasPKs(self.eu):
					pk[1] = 'fk_',self.ed
				(self.newRelacional[self.eu]).append(pk)
		elif self.c[0] == '1' and self.c[1] == '1':
			if self.p[0] == 'p' and self.p[1] == 't':
				for pk in self.getPKs(self.eu):
					if self.hasPKs(self.ed):
						pk[1] = 'fk_',self.eu
					(self.newRelacional[self.ed]).append(pk)
			elif self.p[0]=='t' and self.p[1]=='p':
				for pk in self.getPKs(self.ed):
					if self.hasPKs(self.eu):
						pk[1] = 'fk_'+self.ed
					(self.newRelacional[self.eu]).append(pk)
			else:
				for pk in self.getPKs(self.eu):
					if self.hasPKs(self.ed):
						pk[1] = 'fk_',self.eu
					(self.newRelacional[self.ed]).append(pk)
		elif self.c[0] == 'n' and self.c[1] == 'n':
			self.newRelacional[self.nombre] = []
			for pk in self.getPKs(self.eu):
				(self.newRelacional[self.nombre]).append(pk)
			for pk in self.getPKs(self.ed):
				(self.newRelacional[self.nombre]).append(pk)
				
		return self.newRelacional
	def getPKs(self,nombreEntidad):
		for atributo in self.newRelacional[nombreEntidad]:
			if atributo.count('pk') > 0 or atributo.count('ppk') > 0:
				yield atributo
	def hasPKs(self,nombreEntidad):
		for atributo in self.newRelacional[nombreEntidad]:
			if atributo.count('pk') > 0:
				return True
		return False

class VinculoEneario(object):
	def __init__(self,lineasVinculo,entiades):
		self.bk = lineasVinculo
		self.elementos = (self.bk).split(',')
		self.nombre = self.elementos[0]

		nombreL = len(self.nombre)
		if self.nombre[0] == '"' and self.nombre[nombreL-1] == '"':
			self.nombre = (self.nombre).replace('"','').replace('"','')
		else:
			raise SyntaxError

	def getKeys(self,dic):
		return [['prueba','pk']]

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
			vinculosEnearios.append(VinculoEneario(v,entidades))
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
			vinculos1N.append(Vinculo(v,entidades,[cu,cd],[pu,pd]))
		elif cu=='n' and cd=='n':
			vinculosMN.append(Vinculo(v,entidades,[cu,cd],[pu,pd]))
		elif cu=='1' and cd=='1':
			vinculos11.append(Vinculo(v,entidades,[cu,cd],[pu,pd]))
	

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


	for relacion in mRelacional:
		print relacion," => "
		for attr in mRelacional[relacion]:
			print "\t",attr

transformar('../format.bd')