import atributos

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
			self.hasAtributos = True
			self.atributos = self.elementos[3]
		else:
			self.hasAtributos = False
			self.atributos = []
	def format(self,mRelacional):
		self.newRelacional = mRelacional

		if self.c[0] == '1' and self.c[1] == 'n':
			for pk in self.getPKs(self.eu):
				if self.hasPKs(self.ed):
					fk = pk[1]
					fk = 'fk:'+self.eu
				else:
					fk = pk[1]
				#def hasPk(self,entidad,atributo,propietaria):
				if not(self.hasPk(self.ed,pk[0],self.eu)):
					(self.newRelacional[self.ed]).append([pk[0],fk])
			if self.hasAtributos:
				for atributoVinculo in self.getAtributos():
					if not(self.hasPk(self.ed,pk[0],self.eu)):
						(self.newRelacional[self.ed]).append(atributoVinculo)
		elif self.c[0] == 'n' and self.c[1] == '1':
			for pk in self.getPKs(self.ed):
				if self.hasPKs(self.eu):
					fk = pk[1]
					fk = 'fk:'+self.ed
				else:
					fk = pk[1]
					
				if not(self.hasPk(self.eu,pk[0],self.ed)):
					(self.newRelacional[self.eu]).append([pk[0],fk])
			if self.hasAtributos:
				for atributoVinculo in self.getAtributos():
					if not(self.hasPk(self.eu,pk[0],self.ed)):
						(self.newRelacional[self.eu]).append(atributoVinculo)
		elif self.c[0] == '1' and self.c[1] == '1':
			if self.p[0] == 'p' and self.p[1] == 't':
				for pk in self.getPKs(self.eu):
					if self.hasPKs(self.ed):
						pk[1] = 'fk:'+self.eu

					if not(self.hasPk(self.ed,pk[0],self.eu)):
						(self.newRelacional[self.ed]).append(pk)
				if self.hasAtributos:
					for atributoVinculo in self.getAtributos():
						(self.newRelacional[self.ed]).append(atributoVinculo)
			elif self.p[0]=='t' and self.p[1]=='p':
				for pk in self.getPKs(self.ed):
					if self.hasPKs(self.eu):
						pk[1] = 'fk:'+self.ed7
					if not(self.hasPk(self.eu,pk[0],self.ed)):
						(self.newRelacional[self.eu]).append(pk)

				if self.hasAtributos:
					for atributoVinculo in self.getAtributos():
						(self.newRelacional[self.eu]).append(atributoVinculo)
			else:
				for pk in self.getPKs(self.eu):
					if self.hasPKs(self.ed):
						pk[1] = 'fk:'+self.eu

					if not(self.hasPk(self.ed,pk[0],self.eu)):
						(self.newRelacional[self.ed]).append(pk)
				if self.hasAtributos:
					for atributoVinculo in self.getAtributos():
						(self.newRelacional[self.ed]).append(atributoVinculo)
		elif self.c[0] == 'n' and self.c[1] == 'n':
			self.newRelacional[self.nombre] = []
			for pk in self.getPKs(self.eu):
				fk = pk[1]
				if fk == 'ppk':
					fk = fk.replace('ppk','ppk:'+self.eu)
				elif fk == 'pk':
					fk = fk.replace('pk','pk:'+self.eu)
				(self.newRelacional[self.nombre]).append([pk[0],fk])
			for pk in self.getPKs(self.ed):
				fk = pk[1]
				if fk == 'ppk':
					fk = fk.replace('ppk','ppk:'+self.ed)
				elif fk == 'pk':
					fk = fk.replace('pk','pk:'+self.ed)
				(self.newRelacional[self.nombre]).append([pk[0],fk])

			if self.hasAtributos:
				for atributoVinculo in self.getAtributos():
					(self.newRelacional[self.nombre]).append(atributoVinculo)

		return self.newRelacional
	def getAtributos(self):
		aL = len(self.atributos)
		if not(self.atributos[0] == '/' and self.atributos[aL-1] == '/'):
			raise SyntaxError

		self.atributos = self.atributos.replace('/','')
		self.a = (self.atributos).split(';')

		rAtributos = []
		for atributo in self.a:
			fChar = atributo[0]
			lChar = atributo[len(atributo) - 1]
			if fChar == "C" and atributo[1] == "(" and lChar	== ")":
				compuesto = atributos.Compuesto(atributo)
				for a in compuesto.getAtributos('v:'+self.nombre):
					rAtributos.append(a)
			else:
				rAtributos.append([atributo,'v:'+self.nombre])

		for r in rAtributos:
			yield r	
	def getPKs(self,nombreEntidad):
		for atributo in self.newRelacional[nombreEntidad]:
			if atributo.count('pk') > 0 or atributo.count('ppk') > 0:
				yield atributo
	def hasPKs(self,nombreEntidad):
		for atributo in self.newRelacional[nombreEntidad]:
			if atributo.count('pk') > 0:
				return True
		return False
	def hasPk(self,entidad,atributo,propietaria):
		try:
			eBuscando = self.newRelacional[entidad]
			for a in eBuscando:
				e = a[0]
				bk = a[1]
				vieneDe = bk.split(':')
				
				if len(vieneDe) > 1:
					vieneDe = vieneDe[1]
				else:
					return False

				if vieneDe == propietaria and e == atributo:
					return True
				else:
					return False

		except:
			print "Error en Vinculos"

class VinculoEneario(object):
	def __init__(self,lineasVinculo,entidades):
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