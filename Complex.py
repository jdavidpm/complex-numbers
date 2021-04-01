# -*- coding: utf-8 -*-

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import messagebox
import matplotlib.pyplot as plt

raiz = Tk()


AR = ""
AI = ""
BR = ""
BI = ""


#Funcioes
def selectOption():
   return str(var.get())


def resultadoOpera():
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
	else:
		messagebox.showerror("Error", "Tiene que seleccionar una operación")
		res = 0
	
	result.config(text = str(res))
	return res
def plotResult():
	tmp = resultadoOpera()
	xR = tmp.real
	yR = tmp.imag

	plt.title("Gráfica de Complejos")
	plt.xlabel('Reales')
	plt.ylabel('Imaginarios')

	plt.plot([float(AReal.get())], [float(AImag.get())], 'ro', label = '#1')
	plt.plot([float(BReal.get())], [float(BImag.get())], 'bo', label = '#2')
	plt.plot([xR], [yR], 'gs', label = 'Resultado')

	plt.grid(True)
	plt.legend()
	plt.savefig("output.png")
	plt.show()

#Diseño de Ventana Principal

raiz.geometry('640x300') # anchura x altura

raiz.configure(bg = 'beige')

raiz.title('Operaciones Básicas con Números Complejos')

label1 = Label(raiz, text = "Elige la operación: ", bg = "black", fg = "white")
label1.place (x = 0, y = 10, width = 640, height = 30);

var = IntVar()
R1 = Radiobutton(raiz, text = "Suma", variable = var, value = 1, command = selectOption, bg = "beige", fg = "black")
R1.place(x = 10, y = 50)

R2 = Radiobutton(raiz, text = "Resta", variable = var, value = 2, command = selectOption, bg = "beige", fg = "black")
R2.place(x = 10, y = 80)

R3 = Radiobutton(raiz, text = "Multiplicación", variable = var, value = 3, command = selectOption, bg = "beige", fg = "black")
R3.place(x = 10, y = 110)

R4 = Radiobutton(raiz, text = "División", variable = var, value = 4, command = selectOption, bg = "beige", fg = "black")
R4.place(x = 10, y = 140)

Label(raiz, text = "Número 1: ", bg = "beige", fg = "black").place(x = 10, y = 180, width = 60, height = 20)
AReal = Entry(raiz, bd = 4)
AReal.place(x = 80, y = 180, width = 35, height = 20)
AImag = Entry(raiz, bd = 4)
AImag.place(x = 120, y = 180, width = 35, height = 20)
Label (text = "i", bg = 'beige', font ="Times").place(x = 157, y = 177)

Label(raiz, text = "Número 2: ", bg = "beige", fg = "black").place(x = 10, y = 210, width = 60, height = 20)
BReal = Entry(raiz, bd = 4)
BReal.place(x = 80, y = 210, width = 35, height = 20)
BImag = Entry(raiz, bd = 4)
BImag.place(x = 120, y = 210, width = 35, height = 20)
Label (text = "i", bg = 'beige', font ="Times").place(x = 157, y = 207)

AReal.insert(0, "0")
AImag.insert(0, "0")
BReal.insert(0, "0")
BImag.insert(0, "0")


Label(raiz, text = "Resultado: ", bg = "beige", fg = "black").place(x = 450, y = 50)
result = Label(raiz, bg = "beige", fg = "black", font =("Times", 25))
result.place(x = 425, y = 85)

botonGraficar = Button (raiz, text = "Graficar", command = plotResult)
botonGraficar.place(x = 450, y = 150)

botonAceptar = Button (raiz, text = "Aceptar", command = resultadoOpera).place (x = 60, y = 240)

raiz.button = ttk.Button(raiz, text = 'Salir', command = quit)
raiz.button.place(x = 270, y = 270)

raiz.mainloop()