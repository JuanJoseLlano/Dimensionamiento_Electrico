# -*- coding: utf-8 -*-
from tkinter import *
raiz=Tk()
raiz.title("Calculadora nivel cortocircuito")
miframe=Frame(raiz)
miframe.pack()

impedancias={'Cobre':{'PVC':{'14':10.1706+0.1903J,'12':6.5617+0.1772J,'10':3.9370+0.1640J,'8':2.5591+0.1706J,
        '6':1.6076+0.1673J,'4':1.0171+0.1575J,'2':0.6234+0.1476J,'1':0.5052+0.1509J,
        '0':0.3937+0.1444J,'00':0.3281+0.1411J,'000':0.2526+0.1378J,'0000':0.2034+0.1345J,
        '250':0.1706+0.1345J,'300':0.1444+0.1345J,'350':0.1247+0.1312J,'400':0.1083+0.1312J,
        '500':0.0886+0.1280J,'600':0.0755+0.1280,'750':0.0623+0.1247J,'1000':0.0492+0.1214J},
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

       
canaleta=StringVar()
canaleta.set('PVC')
calibre=StringVar()
calibre.set('8')
material=StringVar()
material.set('Cobre')
tension=IntVar()
tension.set(120)
corto=StringVar()
sim=IntVar()
resultado=StringVar()
resultado.set('Sin calcular')
long=IntVar()

calibres=['14','12','10','8','6','4','2','1','0','00','000','0000','250','300','350','400','500','600','750','1000']
canaletas=['PVC','Aluminio','Acero']
materiales=['Cobre','Aluminio']

def calcular():
    if long.get()==0:
        resultado.set('Circuito sin longitud')
    else:
        imp=impedancias[material.get()][canaleta.get()][calibre.get()]
        if corto.get()=='' or sim.get()==1:
            resultado.set(abs(int(tension.get())*0.8/(imp*int(long.get())/1000)))
        else:
            resultado.set(abs(int(tension.get())/((imp*int(long.get())/1000)+complex(corto.get()))))
    
Label(miframe, text="Calibre del cable").grid(row=0, column=0, padx=5, pady=5)
OptionMenu(miframe,calibre,*calibres).grid(row=0, column=1, padx=5, pady=5)

Label(miframe, text="Material de la canaleta").grid(row=1, column=0, padx=5, pady=5)
OptionMenu(miframe,canaleta,*canaletas).grid(row=1, column=1, padx=5, pady=5)

Label(miframe, text="Material del conductor").grid(row=2, column=0, padx=5, pady=5)
OptionMenu(miframe,material,*materiales).grid(row=2, column=1, padx=5, pady=5)

Label(miframe, text="Tensión de la fuente[V]").grid(row=3, column=0, padx=5, pady=5)
Entry(miframe, width=5, textvariable=tension).grid(row=3, column=1, padx=5, pady=5)

Label(miframe, text="Longitud del circuito[m]").grid(row=4, column=0, padx=5, pady=5)
Entry(miframe, width=5, textvariable=long).grid(row=4, column=1, padx=5, pady=5)

Label(miframe, text="Impedancia de cortocircuito").grid(row=5, column=0, padx=5, pady=5)
Entry(miframe, width=10, textvariable=corto).grid(row=5, column=1, padx=5, pady=5)

Label(miframe, text="Calcular sin impedacia CC[Ohm/Km]").grid(row=6, column=0, padx=5, pady=5)
Checkbutton(miframe,variable=sim).grid(row=6, column=1, padx=5, pady=5)

Button(miframe,text='Calcular',command=calcular).grid(row=7, column=0, padx=5, pady=5)
Label(miframe, textvariable=resultado).grid(row=7, column=1, padx=5, pady=5)



raiz.mainloop()

