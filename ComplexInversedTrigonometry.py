# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
import cmath

def sen(Z):
	res = complex(math.sin(Z.real) * math.cosh(Z.imag), (math.cos(Z.real) * math.sinh(Z.imag)))
	return res

def cos(Z):
	res = complex(math.cos(Z.real) * math.cosh(Z.imag), -(math.sin(Z.real) * math.sinh(Z.imag)))
	return res

def tan(Z):
	if (math.degrees(cmath.phase(Z)) == float(90) or cos(Z) == 0):
		print ("Error")
		return -1
	res = sen(Z) / cos(Z)
	return res

def csc(Z):
	if (sen(Z) == 0):
		print ("Error")
		return -1
	return (1 / sen(Z))

def sec(Z):
	if (cos(Z) == 0):
		print ("Error")
		return -1
	return (1 / cos(Z))

def cot(Z):
	if (tan(Z) == 0):
		print ("Error")
		return -1
	return (1 / tan(Z))

#Hiperbolicas

def senh(Z): #senh(z) = -i sen(iz)
	res = complex(0, -1) * sen((complex(0, 1) * Z))
	return res

def cosh(Z): #cosh(z) = cos(iz)
	res = cos((complex(0, 1) * Z))
	return res

def tanh(Z): #tanh(z) = -i tan(iz)
	res = complex(0, -1) * tan((complex(0, 1) * Z))
	return res

def csch(Z): #csch(z) = i csc(iz)
	res = complex(0, 1) * csc((complex(0, 1) * Z))
	return res

def sech(Z): #sech(z) = sec(iz)
	res = sec((complex(0, 1) * Z))
	return res

def coth(Z): #coth(z) = i cot(iz)
	res = complex(0, 1) * cot((complex(0, 1) * Z))
	return res

#logartmo

def Ln(Z):
	if (abs(Z) == 0):
		messagebox.showerror("Error", "Tiene que seleccionar una operación")
		return "er"
	res = complex(math.log(abs(Z)), math.degrees(cmath.phase(Z)))
	return res

#Inversas

def arcsen(Z): #senh(z) = -i sen(iz)
	res =  Ln((complex(0, 1) * Z) + cmath.sqrt(1 - (Z ** 2))) / complex(0, 1)
	return res

def arccos(Z): #cosh(z) = cos(iz)
	res =  Ln(Z + (complex(0, 1) * cmath.sqrt(1 - (Z ** 2)))) / complex(0, 1)
	return res

def arctan(Z): #tanh(z) = -i tan(iz)
	res = Ln((1 + (complex(0, 1) * Z)) / (1 - (complex(0, 1) * Z))) / (2 * complex(0, 1)) #hasta aqui me quedé
	return res

def arccsc(Z): #csch(z) = i csc(iz)
	res = arcsen(1 / Z)
	return res

def arcsec(Z): #sech(z) = sec(iz)
	res = arccos(1 / Z)
	return res

def arccot(Z): #coth(z) = i cot(iz)
	res = arctan(1 / Z)
	return res

def arcsenh(Z): #senh(z) = -i sen(iz) #no
	res = complex(0, -1) * sen((complex(0, 1) * Z))
	return res

def arccosh(Z): #cosh(z) = cos(iz)
	res = cos((complex(0, 1) * Z))
	return res

def arctanh(Z): #tanh(z) = -i tan(iz)
	res = complex(0, -1) * tan((complex(0, 1) * Z))
	return res

def arccsch(Z): #csch(z) = i csc(iz)
	res = complex(0, 1) * csc((complex(0, 1) * Z))
	return res

def arcsech(Z): #sech(z) = sec(iz)
	res = sec((complex(0, 1) * Z))
	return res

def arccoth(Z): #coth(z) = i cot(iz)
	res = complex(0, 1) * cot((complex(0, 1) * Z))
	return res




if __name__ == "__main__":

	print(arcsen(complex(0, 1)))
	print(arccos(.5))
	print(arctan(8))

