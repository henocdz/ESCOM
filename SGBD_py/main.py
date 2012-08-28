#encoding utf-8

import os
import time
class BD:
	"""Crear nueva base de datos"""
	def __init__(self):
		self.metadata = {}
		self.bd = {}
		self.lastItem = 0

	def defNombreAttr(self):
		"""Obtener nombre del nuevo campo"""
		nombre = raw_input("Nombre del nuevo campo: ")
		try:
			nombre = str(nombre)
		except ValueError:
			print "Valor no valido"
			time.sleep(1)
			self.defNombreAttr()

		if self.metadata.has_key(nombre):
			print "Ese campo ya existe, intenta con otro"
			time.sleep(1)
			nombre = self.defNombreAttr()

		return nombre


	def defTipo(self):
		"""Obtener tipo de dato en nuevo campo"""
		tipo = raw_input("Tipo de dato del nuevo campo [int,float,string]: ")
		try:
			
			tipo = tipo.lower()
			if(tipo == "int" or tipo == "float" or tipo == "string"):
				tipo = str(tipo)
			else:
				print "Valor no valido"
				time.sleep(1)
				self.defTipo()


		except ValueError:
			print "Valor no valido"
			time.sleep(1)
			self.defTipo()
		return tipo

	def agregarCampo(self):
		""" Agregar un nuevo atributo a la tabla """
		os.system("cls")

		nombre = self.defNombreAttr()
		tipo = self.defTipo()
		self.metadata[nombre] = tipo

		try:
			for r in self.bd:
				for i in range(len(self.bd[r])):
					self.bd[r].append([nombre,None])

		except ValueError:
			print "Error critico, adios! :("
			time.sleep(1)
			self.menu()


		print "Configuracion Guardada"
		time.sleep(1)
		self.menu()

	def regValue(self,campo,tipo):
		value = raw_input("Introduce el valor para %s (%s): " % (campo,tipo))
		tipo = tipo.lower()
		try:
			if tipo == "int":
				int(value)
			elif tipo == "float":
				float(value)
			elif tipo == "string":
				str(tipo)
		except ValueError:
			print "Valor no valido debe ser de tipo ",tipo
			time.sleep(1)
			self.regValue(campo,tipo)

		return value

	def agregarRegistro(self):
		os.system("cls")

		if len((self.metadata).keys()) <= 0:
			print "Debes definir por lo menos un atributo"
			time.sleep(1)
			self.menu()
			return None

		newReg = []
		ln = self.lastItem + 1

		print "Estas agregando el elemento [", ln,"] \n\t"
		for r in self.metadata:
			dato = self.regValue(r,self.metadata[r])
			newReg.append([r,dato])
		try:
			self.bd[ln] = newReg
		except ValueError:
			print "Error critico,vuelve a intentar! :("
			time.sleep(1)
			self.menu()

		self.lastItem = self.lastItem + 1
		print "Registro agregado"
		time.sleep(1)
		self.menu()

	def rawString(self,cad):
		myStr= raw_input("Introduce %s (debe ser STRING): " % cad)

		try:
			myStr= str(myStr)
		except ValueError:
			print "Valor no valido debe ser de tipo STRING (CADENA)"
			time.sleep(1)
			self.rawStr(cad)

		return myStr

	def modificarDato(self):
		os.system("cls")
		key = self.rawInt("la clave del elemento que deseas modificar")

		if(not (self.bd.has_key(key)) ):
			print "Registro no encontrado"
			time.sleep(1)
			self.menu()

		field = self.rawString("el nombre del campo a modificar")
		
		valor = self.regValue(field,self.metadata[field])

		if self.metadata.has_key(field):
			for r in self.bd:
				for i in range(len(self.bd[r])):
					if self.bd[r][i-1][0]  == field:
						self.bd[r][i-1][1] = valor 
		else:
			print "No existe ese campo"
			time.sleep(1)
			self.menu()

		self.menu()

	def eliminarRegistro(self):
		os.system("cls")
		key = self.rawInt("la clave del elemento que deseas eliminar")
		if(self.bd.has_key(key)):
			del self.bd[key]
			print "Registro eliminado"
		else:
			print "No existe ese registro"
			time.sleep(1)
			self.menu()

		self.menu()

	def rawInt(self,cad):
		myInt = raw_input("Introduce %s (debe ser INT): " % cad)

		try:
			myInt = int(myInt)
		except ValueError:
			print "Valor no valido debe ser de tipo INT (ENTERO)"
			time.sleep(1)
			self.rawInt(cad)

		return myInt

	def buscarRegistro(self):
		os.system("cls")
		key = self.rawInt("la clave del elemento que buscas")

		if(not (self.bd.has_key(key)) ):
			print "Registro no encontrado"
			time.sleep(1)
			self.menu()
		else:
			for d in range(len(self.bd[key])):
				print self.bd[key][d-1][0]," = ",self.bd[key][d-1][1]

		os.system("pause")
		self.menu()

	def eliminarDB(self):
		os.system("cls")
		self.bd.clear()
		self.metadata.clear()

		print "Informacion eliminada"
		time.sleep(1)
		self.menu()

	def eliminarRegistros(self):
		os.system("cls")
		self.bd = {}

		print "Registros Eliminados"
		time.sleep(1)
		self.menu()

	def imprimirMD(self):
		for r in self.metadata:
			print self.metadata[r]

		os.system("pause")
		self.menu()

	def imprimirBD(self):
		if len((self.bd).keys()) <= 0:
			print "Debes agregar por lo menos un registro primero"
			time.sleep(1)
			self.menu()
			return None

		for r in self.bd:
			print "> Registro [",r,"]"
			for i in range(len(self.bd[r])):
				print "\t",self.bd[r][i-1][0]," = ",self.bd[r][i-1][1]

		print "\n\n"		
		os.system("pause")
		self.menu()

	def menu(self):
		os.system("cls")
		print """
BIENVENIDO!  
Elige la opcion que desees
  [1] Agregar nuevo campo
  [2] Agregar registro
  [3] Modificar dato
  [4] Eliminar Registro
  [5] Buscar
  [6] Eliminar BD
  [7] Imprimir DB
  [8] Eliminar TODOS los registros
  [9] Salir
	"""

		op = raw_input("\t Escribe la opcion: ")

		try:
			op = int(op)
		except ValueError:
			print "El valor no introducido no es valido"
			time.sleep(1)
			self.menu()

		if op == 1:
			self.agregarCampo()
		elif op == 2:
			self.agregarRegistro()
		elif op == 3:
			self.modificarDato()
		elif op == 4:
			self.eliminarRegistro()
		elif op == 5:
			self.buscarRegistro()
		elif op == 6:
			self.eliminarDB()
		elif op == 7:
			self.imprimirBD()
		elif op == 8:
			self.eliminarRegistros()
		elif op >= 9 or op <= 0:
			print "Adios!"
			time.sleep(1)
			exit()



bd1 = BD()

bd1.menu()