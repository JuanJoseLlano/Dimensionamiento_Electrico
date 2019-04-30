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
from back_functions import *

root=Tk()
root.title('Herramienta selección óptima de conductores')
#--------------------------------------------------------------
#Variables creation
load=StringVar() #Circuit load
load.set(1000)

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

kwh_cost=IntVar() #Electricity cost in COP
kwh_cost.set(550)

conduit_materials=('PVC', 'Aluminio', 'Acero')
actual_conduit_material=StringVar()
actual_conduit_material.set('PVC')

wire_materials=('Cobre','Aluminio')
actual_wire_material=StringVar()
actual_wire_material.set('Cobre')


#--------------------------------------------------------------
#Input data creation 

data_frame=Frame(root)
data_frame.grid(row=0, column=0)

Label(data_frame, text='Carga[KW+JKVAR]').grid(row=0,column=0)
Entry(data_frame, textvariable=load, width="15").grid(row=1, column=0,padx=5)

Label(data_frame, text='Longitud[m]').grid(row=0,column=1)
Entry(data_frame, textvariable=length, width="10").grid(row=1, column=1,padx=5)

Label(data_frame, text='Voltaje[V]').grid(row=0,column=2)
Entry(data_frame, textvariable=voltage, width="8").grid(row=1, column=2, padx=5)

Label(data_frame, text='Tasa energía[%/Año]').grid(row=0,column=3)
Entry(data_frame, textvariable=rate, width="16").grid(row=1, column=3)

Label(data_frame, text='Vida útil[Años]').grid(row=0,column=4)
Entry(data_frame, textvariable=lifetime, width="12").grid(row=1, column=4, padx=5)

Label(data_frame, text='Costo kWh').grid(row=0,column=5)
Entry(data_frame, textvariable=kwh_cost, width="8").grid(row=1, column=5)

Label(data_frame, text='Canaleta').grid(row=0,column=6)
OptionMenu(data_frame,actual_conduit_material,*conduit_materials).grid(row=1,column=6,padx=5)

Label(data_frame, text='Conductor').grid(row=0,column=7)
OptionMenu(data_frame,actual_wire_material,*wire_materials).grid(row=1,column=7,padx=5)

Radiobutton(data_frame, text='Circuito monofásico', variable=phases,value=1 ).grid(row=0,column=8)
Radiobutton(data_frame, text='Circuito trifásico', variable=phases,value=3 ).grid(row=1,column=8)

Button(data_frame, text='Realizar análisis', command=lambda: voltage_drop_graph(root,
                                                                        actual_conduit_material,
                                                                        actual_wire_material,
                                                                        length,
                                                                        load,
                                                                        voltage)).grid(row=0, column=9)

#------------------------------------------------------------------

root.mainloop()
