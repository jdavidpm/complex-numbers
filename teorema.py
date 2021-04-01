# !/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math
from math import pi
import cmath

root = Tk()


functions = [u'\u005A' + u'\u207F', u'\u0065' + u'\u1DBB', 'sen(Z)', 'cosh(Z)', 'ln(Z)']

#Funciones Matematicas
def circle(re, im):
    return (re ** 2 + im ** 2)
def fact(n):
    if n == 0:
        r = 1
    else:
        r = n * fact(n - 1)
    return r
def sen(Z):
	res = complex(math.sin(Z.real) * math.cosh(Z.imag), (math.cos(Z.real) * math.sinh(Z.imag)))
	return res

def cos(Z):
	res = complex(math.cos(Z.real) * math.cosh(Z.imag), -(math.sin(Z.real) * math.sinh(Z.imag)))
	return res

def senh(Z):
	res = complex(0, -1) * sen((complex(0, 1) * Z))
	return res

def cosh(Z):
	res = cos((complex(0, 1) * Z))
	return res

#Funciones para Derivar
def DzPot (n, t, Z0):
	e = n - t
	if (e == 0):
		return fact(n)
	if (e < 0):
		return 0
	else:
		return ((fact(n)/fact(e)) * ((Z0) ** e))

def DzExp(Z0):
	return (np.exp(Z0))

def DzSen(t, Z0):
	return (sen(Z0 + complex(((t * 180)/2), 0)))

def DzCsh(t, Z0):
	if ((t % 2) == 0 and t > 1):
		return (cosh(Z0))
	else:
		return (senh(Z0))

def DzLn(t, Z0):
	if (Z0 == 0):
		messagebox.showerror('Error', 'Ln de 0 no valido')
		return 0
	return (((-1) ** (t + 1)) * (fact(t - 1) / (Z0 ** t)))

#funcion para graficar
def plotResult(radio, re, im):
	arr = np.arange(0.0, 180, 0.5)

	plt.grid(True)

	for i in arr:
		plt.plot(radio*np.cos(i), radio*np.sin(i), 'go')
	plt.plot(re, im, 'ro')

	plt.title("Circunferencia de radio " + str(radio) + '\n y Z0 = ' + str(re) + ' + ' + str(im) + 'i')
	plt.xlabel('Reales')
	plt.ylabel('Imaginarios')
	plt.gca().set_aspect('equal')
	plt.show()

def teoremApl(N, n, re, ima):

	Z0 = complex(re, ima)
	cad = str(listFunction.curselection()[0])


	if (cad  == '0'):
		fun = DzPot(n, N - 1, Z0)
	if (cad == '1'):
		fun = DzExp(Z0)
	if (cad == '2'):
		fun = DzSen(N - 1, Z0)
	if (cad == '3'):
		fun = DzCsh(N - 1, Z0)
	if (cad == '4'):
		fun = DzLn(N - 1, Z0)

	res = ((2 * pi * complex(0, 1)) * fun) / fact(N - 1)

	return res

def resultadoOpera ():
	x = int(ZReal.get())
	y = int(ZImag.get())
	rad = int(r.get())
	pot = int(n.get())
	fpt = int(N.get())

	if (circle (x, y) == rad ** 2):
		messagebox.showerror("Z0 en la Circunferencia", u'\u222B' + 'Indeterminado')
	if (circle (x, y) > rad ** 2):
		messagebox.showerror("Z0 fuera", u'\u222B' + 'f(z)dz = 0')
	else:
		messagebox.showinfo("Resultado", u'\u222B' + 'f(z)dz = ' + str(teoremApl(fpt, pot, x, y)))

	plotResult(rad, x, y)
	return

#root.geometry('440x310') # anchura x altura
root.minsize(width = 440, height = 310)
root.maxsize(width = 440, height = 310)

root.configure(bg = '#37474F', relief = SUNKEN) #place

root.title('Teorema Integral')

#bit = PhotoImage(file='integral.ico',format='iconbitmap')
bit = root.iconbitmap('integral.ico')

title = Label(root, bg = '#00838F', fg = '#FFFFFF', font = ("Century Gothic", 20), text = 'Teorema Integral\nde Cauchy Generalizado')
title.place(x = 50, y = 20)

enter = Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Ingrese los datos necesarios.' )
enter.place(x = 10, y = 100) #Cambria Math

function = Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = u'\u2713' + ' Función:' )
function.place(x = 15, y = 140)
scrollFunction = Scrollbar(root, elementborderwidth = 1)
scrollFunction.place (x = 190, y = 143, width = 20, height = 25)
listFunction = Listbox(root, yscrollcommand = scrollFunction.set, bd = 1, font = ("Cambria", 13))
for line in functions:
   listFunction.insert(END, line)
listFunction.place(x = 130, y = 143, width = 60, height = 25)
scrollFunction.config(command = listFunction.yview)

Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'n:' ).place(x = 210, y = 143, width = 30, height = 25)
n = Entry(root, bd = 1)
n.place (x = 240, y = 143, width = 30, height = 25)

Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = u'\u2713' + ' N:' ).place(x = 15, y = 180)
N = Entry(root, bd = 1)
N.place (x = 70, y = 183, width = 30, height = 25)

Label(root, text = u'\u2713' + " Z0:", font = ("Century Gothic", 15), bg = "#37474F", fg = "#FFFFFF").place(x = 15, y = 220)
ZReal = Entry(root, bd = 1)
ZReal.place(x = 75, y = 222, width = 30, height = 25)
Label (text = "+", bg = '#37474F', font = ("Century Gothic", 15), fg = "#FFFFFF").place(x = 105, y = 220)
ZImag = Entry(root, bd = 1)
ZImag.place(x = 125, y = 222, width = 30, height = 25)
Label (text = "i", bg = '#37474F', font = ("Century Gothic", 15), fg = "#FFFFFF").place(x = 155, y = 220)

Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = u'\u2713' + ' Radio:' ).place(x = 15, y = 260)
r = Entry(root, bd = 1)
r.place (x = 110, y = 262, width = 30, height = 25)

r.insert(0, "0")
ZReal.insert(0, "0")
ZImag.insert(0, "0")
N.insert(0, "0")
n.insert(0, "0")

botonAceptar = Button(root, text = "Aceptar", command = resultadoOpera, font = ("Century Gothic", 11)).place (x = 300, y = 180)
botonSalir = Button(root, text = "Salir", command = quit, font = ("Century Gothic", 11)).place (x = 315, y = 230)

root.mainloop()