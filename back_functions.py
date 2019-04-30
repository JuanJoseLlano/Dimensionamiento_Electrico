#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:29:52 2019

@author: Juan llano
"""
#This class allow the user use the impendance values of the CENTELSA wires according to the diameter
# and the conduit material of the installation. UPDATED at 24/04/2019.
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class wire:
    def __init__(self):
        self.impedance ={'Cobre':{'PVC':{'14':10.1706+0.1903J,'12':6.5617+0.1772J,'10':3.9370+0.1640J,'8':2.5591+0.1706J,
        '6':1.6076+0.1673J,'4':1.0171+0.1575J,'2':0.6234+0.1476J,'1':0.5052+0.1509J,
        '0':0.3937+0.1444J,'00':0.3281+0.1411J,'000':0.2526+0.1378J,'0000':0.2034+0.1345J,
        '250':0.1706+0.1345J,'300':0.1444+0.1345J,'350':0.1247+0.1312J,'400':0.1083+0.1312J,
        '500':0.0886+0.1280J,'600':0.0755+0.1280J,'750':0.0623+0.1247J,'1000':0.0492+0.1214J},
        'Aluminio':{'14':10.1706+0.1903J,'12':6.5617+0.1772J,'10':3.9370+0.1640J,'8':2.5591+0.1706J,
        '6':1.6076+0.1673J,'4':1.0171+0.1575J,'2':0.6562+0.1476J,'1':0.5249+0.1509J,
        '0':0.4265+0.1444J,'00':0.3281+0.1411J,'000':0.2690+0.1378J,'0000':0.2198+0.1345J,
        '250':0.1870+0.1345J,'300':0.1608+0.1345J,'350':0.1411+0.1312J,'400':0.1247+0.1312J,
        '500':0.1050+0.1280J,'600':0.0919+0.1280,'750':0.0787+0.1247J,'1000':0.0623+0.1214J},
        'Acero':{'14':10.1706+0.2395J,'12':6.5617+0.2231J,'10':3.9370+0.2067J,'8':2.5591+0.2133J,
        '6':1.6076+0.21J,'4':1.0171+0.1969J,'2':0.6562+0.1870J,'1':0.5085+0.1870J,
        '0':0.3987+0.1804J,'00':0.3281+0.1772J,'000':0.2270+0.1706J,'0000':0.2067+0.1673J,
        '250':0.1772+0.1706J,'300':0.1476+0.1673J,'350':0.1280+0.1640J,'400':0.1148+0.1608J,
        '500':0.0951+0.1575J,'600':0.0820+0.1575,'750':0.0689+0.1575J,'1000':0.0591+0.15092J}}
        ,'Aluminio':{'PVC':{'12':10.4987+0.1772J,'10':6.5617+0.1640J,'8':4.2651+0.1706J,
        '6':2.6575+0.1673J,'4':1.6732+0.1575J,'2':1.0499+0.1476J,'1':0.8202+0.1509J,
        '0':0.6562+0.1444J,'00':0.5249+0.1411J,'000':0.4265+0.1378J,'0000':0.3281+0.1345J,
        '250':0.2789+0.1345J,'300':0.2329+0.1345J,'350':0.2001+0.1312J,'400':0.1772+0.1312J,
        '500':0.1411+0.1280J,'600':0.1181+0.1280,'750':0.0951+0.1247J,'1000':0.0755+0.1214J},
        'Aluminio':{'12':10.4987+0.1772J,'10':6.5617+0.1640J,'8':4.2651+0.1706J,
        '6':2.6575+0.1673J,'4':1.6732+0.1575J,'2':1.0499+0.1476J,'1':0.8530+0.1509J,
        '0':0.6890+0.1444J,'00':0.5249+0.1411J,'000':0.4265+0.1378J,'0000':0.3609+0.1345J,
        '250':0.2953+0.1345J,'300':0.2493+0.1345J,'350':0.2165+0.1312J,'400':0.1936+0.1312J,
        '500':0.1575+0.1280J,'600':0.1345+0.1280,'750':0.1115+0.1247J,'1000':0.0886+0.1214J},
        'Acero':{'12':10.4987+0.2231J,'10':6.5617+0.2067J,'8':4.2651+0.2133J,
        '6':2.6575+0.21J,'4':1.6732+0.1969J,'2':1.0499+0.1870J,'1':0.8202+0.1870J,
        '0':0.6562+0.1804J,'00':0.5249+0.1772J,'000':0.4265+0.1706J,'0000':0.3281+0.1673J,
        '250':0.2822+0.1706J,'300':0.2362+0.1673J,'350':0.2067+0.1640J,'400':0.1804+0.1608J,
        '500':0.1476+0.1575J,'600':0.1247+0.1575,'750':0.1017+0.1575J,'1000':0.0820+0.15092J}}}
        
def voltage_drop(load, impedance, voltage):
    #The units are load in W+JQ, impedane in ohms(complex) and voltage in volts
    #This function will calculate the voltage drop acording to the electrical moment method
    power_factor=load.real/load.__abs__() 
    efective_impedance=impedance.real + impedance.imag*(((1-(power_factor**2))**(1/2))/power_factor)
    k_factor=efective_impedance/(5*(voltage**2)/1000)
    drop= load.real*k_factor
    return drop

def voltage_iteration(conduit_material, 
                      wire_material, 
                      circuit_length, 
                      load,
                      voltage):
    #This function calculates the voltage drop for all the wires and returns a list with the
    #voltage drop values
    #Conduit_material, wire_material are strings. Cicuit_length and coltage are integers
    #Load is complex
    voltage_drop_list=[]
    reference_wire=wire()
    for i in reference_wire.impedance[wire_material][conduit_material]:
        
        circuit_impedance=(reference_wire.impedance[wire_material][conduit_material][i]
        * circuit_length/1000)
        
        voltage_drop_list.append(voltage_drop(load,circuit_impedance,voltage))
    return voltage_drop_list

def available_wires(wire_material, conduit_material):
    wire_list=[]
    reference_wire=wire()
    for i in reference_wire.impedance[wire_material][conduit_material]:
        wire_list.append(i)
    return wire_list
    
def voltage_drop_graph(master,
                       actual_conduit_material,
                       actual_wire_material,
                       length,
                       load,
                       voltage):
    graph_frame = Frame(master)
    graph_frame.grid(row=1, column=0)
    figure1=plt.Figure(figsize=(4,4))
    graph = figure1.add_subplot(111)
    
    x_data_drop=available_wires(actual_wire_material.get(),
                                actual_conduit_material.get())

    y_data_drop=voltage_iteration(actual_conduit_material.get(),
                             actual_wire_material.get(),
                             int(length.get()),
                             complex(load.get()),
                             int(voltage.get()))
   
    graph.plot(x_data_drop,y_data_drop)
    graph.set_xticklabels(x_data_drop,rotation='vertical')


    canvas = FigureCanvasTkAgg(figure1, graph_frame)
    canvas.get_tk_widget().grid(row=0, column=0)
    return 0