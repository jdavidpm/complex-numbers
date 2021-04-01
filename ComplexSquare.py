# -*- coding: utf-8 -*-

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import messagebox
import matplotlib.pyplot as plt
import math
import cmath

raiz = Tk()

AR = ""
AI = ""
BR = ""
BI = ""

tmp = complex(0)
Z = []

#Funcioes
def selectOption():
   return str(var.get())

def openResult(res, flag):
	strR = ''
	otraVentana = Toplevel(bg = 'beige')
	otraVentana.geometry('200x370')
	otraVentana.title ("Resultado")
	Label(otraVentana, text = "Resultado:", bg = "black", fg = "white").pack(side = TOP, fill = X)
	result = Label(otraVentana, bg = "beige", fg = "black", font =("Times", 25))
	result.pack(side=LEFT)
	if (flag == 0):
		result.config(text = str(res))
	elif(flag == -1):
		for i in range(0, len(res)):
			if (i == 0):
				strR = str(res[i]) + '\n'
			else:
				strR = strR + (str(res[i]) + '\n')
		result.config(text = strR)

	botonGraficar = Button (otraVentana, text = "Graficar", command = lambda: plotResult(res))
	botonGraficar.pack(anchor = CENTER, side = BOTTOM)

def nSquares(n):
	tmpZ = complex(AReal.get()) + complex(AImag.get() + 'j')
	tmpM = abs(tmpZ)
	tmpP = math.degrees(cmath.phase(tmpZ))
	for i in range(0, n):
		tmpR = (tmpM**(1/n)) * math.cos(math.radians((i*2*180) + tmpP) / n)
		tmpI = (tmpM**(1/n)) * math.sin(math.radians((i*2*180) + tmpP) / n)
		Z.append(complex(round(tmpR, 2), round(tmpI, 2)))

	return Z

def resultadoOpera():
	flag = 0
	AR = AReal.get()
	AI = AImag.get()
	BR = BReal.get()
	BI = BImag.get()
	A = complex(AR) + complex(AI + 'j')
	B = complex(BR) + complex(BI + 'j')

	if (selectOption() == '1'):
		res = A + B
	elif (selectOption() == '2'):
		res = A - B
	elif (selectOption() == '3'):
		res = A * B
	elif (selectOption() == '4'):
		if(B == 0):
			messagebox.showerror("Error", "División sobre 0 no valida")
		else:
			res = A / B
	elif (selectOption() == '5'):
		if (rootN.get() == '0'):
			messagebox.showerror ("Error", "# de raices invalido")
		else:
			Z = nSquares(int (rootN.get()))
			flag = 1
	elif (selectOption() == '6'):
		res = B ** int(powN.get())
	else:
		messagebox.showerror("Error", "Tiene que seleccionar una operación")
		res = -1

	if(flag == 1):
		openResult(Z, -1)
	else:
		if (res != -1):
			openResult(res, 0)
		
def plotResult(tmp):

	plt.title("Gráfica de Complejos")
	plt.xlabel('Reales')
	plt.ylabel('Imaginarios')

	if (selectOption() != '5' and selectOption() != '6'):
		xR = tmp.real
		yR = tmp.imag
		plt.plot([float(AReal.get())], [float(AImag.get())], 'ro', label = '#1')
		plt.plot([float(BReal.get())], [float(BImag.get())], 'bo', label = '#2')
		plt.plot([xR], [yR], 'gs', label = 'Resultado')
	elif (selectOption() == '5'):
		plt.plot([float(AReal.get())], [float(AImag.get())], 'ro', label = '#1')
		for i in range (0, int(rootN.get())):
			xR = Z[i].real
			yR = Z[i].imag
			if (i == 0):
				plt.plot([xR], [yR], 'gs', label = 'Resultados')
			else:
				plt.plot([xR], [yR], 'gs')
	elif (selectOption() == '6'):
		xR = tmp.real
		yR = tmp.imag
		plt.plot([float(BReal.get())], [float(BImag.get())], 'bo', label = '#2')
		plt.plot([xR], [yR], 'gs', label = 'Resultado')


	plt.grid(True)
	plt.legend()
	plt.savefig("output.png")
	plt.show()

#Diseño de Ventana Principal

raiz.geometry('200x370') # anchura x altura

raiz.configure(bg = 'beige')

raiz.title('Operaciones Básicas con Números Complejos')

Label(raiz, text = "Elige la operación: ", bg = "black", fg = "white").place (x = 0, y = 10, width = 200, height = 30)

var = IntVar()
R1 = Radiobutton(raiz, text = "Suma", variable = var, value = 1, command = selectOption, bg = "beige", fg = "black")
R1.place(x = 10, y = 50)

R2 = Radiobutton(raiz, text = "Resta", variable = var, value = 2, command = selectOption, bg = "beige", fg = "black")
R2.place(x = 10, y = 80)

R3 = Radiobutton(raiz, text = "Multiplicación", variable = var, value = 3, command = selectOption, bg = "beige", fg = "black")
R3.place(x = 10, y = 110)

R4 = Radiobutton(raiz, text = "División", variable = var, value = 4, command = selectOption, bg = "beige", fg = "black")
R4.place(x = 10, y = 140)

R5 = Radiobutton(raiz, text = "Raices: ", variable = var, value = 5, command = selectOption, bg = "beige", fg = "black")
R5.place(x = 10, y = 170)
rootN = Entry(raiz, bd = 4)
rootN.place(x = 90, y = 170, width = 35, height = 20)

R6 = Radiobutton(raiz, text = "Potencia: ", variable = var, value = 6, command = selectOption, bg = "beige", fg = "black")
R6.place(x = 10, y = 200)
powN = Entry(raiz, bd = 4)
powN.place(x = 90, y = 200, width = 35, height = 20)

Label(raiz, text = "Número 1: ", bg = "beige", fg = "black").place(x = 10, y = 240, width = 60, height = 20)
AReal = Entry(raiz, bd = 4)
AReal.place(x = 80, y = 240, width = 35, height = 20)
Label (text = "+", bg = 'beige', font ="Times").place(x = 118, y = 237)
AImag = Entry(raiz, bd = 4)
AImag.place(x = 140, y = 240, width = 35, height = 20)
Label (text = "i", bg = 'beige', font ="Times").place(x = 177, y = 237)

Label(raiz, text = "Número 2: ", bg = "beige", fg = "black").place(x = 10, y = 270, width = 60, height = 20)
BReal = Entry(raiz, bd = 4)
BReal.place(x = 80, y = 270, width = 35, height = 20)
Label (text = "+", bg = 'beige', font ="Times").place(x = 118, y = 267)
BImag = Entry(raiz, bd = 4)
BImag.place(x = 140, y = 270, width = 35, height = 20)
Label (text = "i", bg = 'beige', font ="Times").place(x = 177, y = 267)

AReal.insert(0, "0")
AImag.insert(0, "0")
BReal.insert(0, "0")
BImag.insert(0, "0")
powN.insert(0, "0")
rootN.insert(0, "0")


botonAceptar = Button (raiz, text = "Igual a", command = resultadoOpera).place (x = 80, y = 300)

raiz.button = ttk.Button(raiz, text = 'Salir', command = quit)
raiz.button.place(x = 65, y = 335)

raiz.mainloop()