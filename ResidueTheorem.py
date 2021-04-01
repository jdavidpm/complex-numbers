# !/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from sympy import *
from math import pi
import math
import cmath
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x, y, z = symbols('x y z')
e = symbols('e')

root = Tk()

functions = [u'\u005A' + u'\u00B2', u'\u0065' + u'\u1DBB', 'cosh(Z)', 'senh(Z)']

def create_window(resA, resB):
	window = Toplevel(root)
	window.minsize(width = 440, height = 275)
	window.maxsize(width = 1000, height = 275)
	window.configure(bg = '#37474F', relief = SUNKEN) #place
	window.title('Resultados')
	bit = window.iconbitmap('integral.ico')
	tA = Label(window, bg = '#00838F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Resultado para Z0 = a')
	tA.place(x = 100, y = 20)
	Label(window, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Res = ' + str(resA)).place(x = 100, y = 50)
	tB = Label(window, bg = '#00838F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Resultado para Z0 = b')
	tB.place(x = 100, y = 150)
	Label(window, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Res = ' + str(resB)).place(x = 100, y = 200)

def create_windowC(resA):
	window = Toplevel(root)
	window.minsize(width = 440, height = 140)
	window.maxsize(width = 1000, height = 275)
	window.configure(bg = '#37474F', relief = SUNKEN) #place
	window.title('Resultados')
	bit = window.iconbitmap('integral.ico')
	tA = Label(window, bg = '#00838F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Resultado para Z0 = a = b')
	tA.place(x = 100, y = 20)
	Label(window, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'Res = ' + str(resA)).place(x = 100, y = 50)

def apliResi(function, N, Z0, t):
	fZ = parse_expr(function)
	res = diff(fZ, z, (N - 1))
	if (t == 'e**z'):
		res = res.subs(e, math.e)
	res = res.subs(z, complex(0, Z0))

	res = res / factorial (N - 1)

	return complex(res)
def getFunction(index):
	if (index == '0'):
		return 'z**2'
	if (index == '1'):
		return 'e**z'
	if (index == '2'):
		return 'cosh(z)'
	if (index == '3'):
		return 'sinh(z)'

def constructFunction():
	N = int(n.get())
	M = int(m.get())
	A = int(a.get())
	B = int(b.get())
	funct = getFunction(str(listFunction.curselection()[0]))
	fA = funct + '/((z-' + str(B) + 'j)**' + str(M) + ')'
	fB = funct + '/((z-' + str(A) + 'j)**' + str(N) + ')'
	if (A == B):
		fC = funct
		resC = apliResi(fC, N + M, A, funct)
		create_windowC(resC)
	else:
		resA = apliResi(fA, N, A, funct)
		resB = apliResi(fB, M, B, funct)
		create_window(resA, resB)

	return

#root.geometry('440x310') # anchura x altura
root.minsize(width = 440, height = 275)
root.maxsize(width = 440, height = 275)

root.configure(bg = '#37474F', relief = SUNKEN) #place

root.title('Residuos')
bit = root.iconbitmap('integral.ico')

title = Label(root, bg = '#00838F', fg = '#FFFFFF', font = ("Century Gothic", 20), text = 'Residuo de una función')
title.place(x = 65, y = 20)

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

Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = u'\u2713' + ' n: ' ).place(x = 15, y = 180)
n = Entry(root, bd = 1)
n.place (x = 75, y = 183, width = 30, height = 25)
Label(root, bg = '#37474F', fg = '#FFFFFF', font = ("Century Gothic", 15), text = 'm: ' ).place(x = 120, y = 180)
m = Entry(root, bd = 1)
m.place (x = 155, y = 183, width = 30, height = 25)

Label(root, text = u'\u2713' + " a:", font = ("Century Gothic", 15), bg = "#37474F", fg = "#FFFFFF").place(x = 15, y = 220)
a = Entry(root, bd = 1)
a.place(x = 75, y = 222, width = 30, height = 25)
Label (text = "b: ", bg = '#37474F', font = ("Century Gothic", 15), fg = "#FFFFFF").place(x = 120, y = 220)
b = Entry(root, bd = 1)
b.place(x = 155, y = 222, width = 30, height = 25)

a.insert(0, "0")
b.insert(0, "0")
n.insert(0, "0")
m.insert(0, "0")

botonAceptar = Button(root, text = "Aceptar", command = constructFunction, font = ("Century Gothic", 11)).place (x = 300, y = 155)
botonSalir = Button(root, text = "Salir", command = quit, font = ("Century Gothic", 11)).place (x = 315, y = 205)

root.mainloop()