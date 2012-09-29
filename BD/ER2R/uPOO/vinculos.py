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

		print self.v,"\n\n"
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
			self.hasAtributos = True
			self.atributos = self.elementos[3]
		else:
			self.hasAtributos = False
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
				if pk[1] == 'ppk':
					pk[1] = pk[1].replace('ppk','ppk_'+self.eu)
				elif pk[1] == 'pk':
					pk[1] = pk[1].replace('pk','pk_'+self.eu)
				(self.newRelacional[self.nombre]).append(pk)
			for pk in self.getPKs(self.ed):
				if pk[1] == 'ppk':
					pk[1] = pk[1].replace('ppk','ppk_'+self.ed)
				elif pk[1] == 'pk':
					pk[1] = pk[1].replace('pk','pk_'+self.ed)
				(self.newRelacional[self.nombre]).append(pk)
		return self.newRelacional
	def getAtributos():
		aL = len(self.hasAtributos)
		if not(self.atributos[0] == '/' and self.atributos[aL-1] == '/'):
			raise SyntaxError

		self.atributos = self.atributos.replace('/','')
		self.a = (self.atributos).split(';')

		
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