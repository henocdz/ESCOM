class Compuesto(object):
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

class Multivaluado(object):
	"""Define la clase para un objeto Multivaluado"""
	def __init__(self,obj,father):
		self.nombre = obj.replace('*','')
		self.f = father

	def getFatherKeys(self,mr,f):
		try:
			for a in mr[f]:
				bka = a[1]
				isPK = bka.split(':')
				
				if len(isPK) == 0:
					isPK = bka
				else:
					isPK = isPK[0]

				isPK = isPK.lower()

				if isPK == "pk" or isPK == "ppk":
					yield [a[0],"pk:"+f]
		except:
			exit()
			print "Esa entidad no existe"

	def format(self,mr):

		newRelacional = mr

		if self.nombre[0] == 'C' and self.nombre[1] == '(' and self.nombre[len(self.nombre)-1] == ')':
			compuesto = Compuesto(self.nombre)

			newRelacional[compuesto.nombre] = []
			for atributo in compuesto.getAtributos('pk'):
				newRelacional[compuesto.nombre].append(atributo)
			for pk in self.getFatherKeys(newRelacional,self.f):
				newRelacional[compuesto.nombre].append(pk)
		else:
			newRelacional[self.nombre] = [[self.nombre,'pk']]
			for pk in self.getFatherKeys(newRelacional,self.f):
				newRelacional[self.nombre].append(pk)

		return newRelacional