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