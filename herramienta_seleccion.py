#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:49:38 2019

@author: Juan llano
"""
#Trial version for electrical development 
#The objetive of this code is to show programming skills and
#their aplicattion in the electrical industry
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root=Tk()
root.title('Herramienta selección óptima de conductores')
principal_frame=Frame(root)
principal_frame.pack()
#--------------------------------------------------------------
#Variables creation
load=StringVar() #Circuit load

length=IntVar() #Circuit length
length.set(100)

voltage=IntVar() # Circuit voltage
voltage.set(240)

rate=IntVar() #Increasing rate of the energy cost year per year
rate.set(3)

lifetime=IntVar() # Life years expected for the installation
lifetime.set(20)

phases=IntVar() #Phases number of the circuit
phases.set(1)

kwh_cost=IntVar() #Electricty cost in COP
kwh_cost.set(550)
#--------------------------------------------------------------
#Input data creation 
Label(principal_frame, text='Carga[KW+JKVAR]').grid(row=0,column=0)
Entry(principal_frame, textvariable=load, width="15").grid(row=1, column=0,padx=5)

Label(principal_frame, text='Longitud[m]').grid(row=0,column=1)
Entry(principal_frame, textvariable=length, width="10").grid(row=1, column=1,padx=5)

Label(principal_frame, text='Voltaje[V]').grid(row=0,column=2)
Entry(principal_frame, textvariable=voltage, width="8").grid(row=1, column=2, padx=5)

Label(principal_frame, text='Tasa energía[%/Año]').grid(row=0,column=3)
Entry(principal_frame, textvariable=rate, width="16").grid(row=1, column=3)

Label(principal_frame, text='Vida útil[Años]').grid(row=0,column=4)
Entry(principal_frame, textvariable=lifetime, width="12").grid(row=1, column=4, padx=5)

Label(principal_frame, text='Costo kWh').grid(row=0,column=5)
Entry(principal_frame, textvariable=kwh_cost, width="8").grid(row=1, column=5)

Radiobutton(principal_frame, text='Circuito monofásico', variable=phases,value=1 ).grid(row=0,column=6)
Radiobutton(principal_frame, text='Circuito trifásico', variable=phases,value=3 ).grid(row=1,column=6)

Button(principal_frame, text='Realizar análisis').grid(row=0, column=7)

figure1=plt.Figure(figsize=(4,3))
graph = figure1.add_subplot(111)
graph.plot([1,2,3,4,5,6],[1,2,3,4,5,6])
canvas = FigureCanvasTkAgg(figure1, principal_frame)
canvas.get_tk_widget().grid(row=2)

root.mainloop()
