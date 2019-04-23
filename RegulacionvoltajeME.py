from tkinter import *
matriz=[]
for i in range(15):
    matriz.append([0]*4)#carga,momento eléctrico,regulación y calibre
raiz=Tk()
raiz.title("Calculadora regulación de voltajes")
miframe=Frame(raiz)
miframe.pack()
#Definicion de variables, crear vector para potencias y distancias
pot=[]
dis=[]
aux=[]
for i in range(8):
    pot.append(IntVar())
    dis.append(IntVar())
    aux.append(0)
tension=IntVar()
factor=StringVar()
calibre=StringVar()
reg=float
reg=0
regu=StringVar()
cont=0
me=0
#La interfaz tendra capacidad para 8 cargas que en general es más que suficiente
#Diccionario de los calibres y sus respectivas impedancias
calibres={}
#Cargas
for i in range(8):
    Label(miframe, text="Potencia(W) #"+str(i+1)).grid(row=i,column=0,padx=5,pady=5)
    Entry(miframe,width=5, textvariable=pot[i]).grid(row=i,column=1,padx=5,pady=5)
    Label(miframe, text="Distancia(m) #"+str(i+1)).grid(row=i,column=2,padx=10,pady=10)
    Entry(miframe,width=3,textvariable=dis[i]).grid(row=i,column=3,padx=5,pady=5)
#Voltaje, factor de potencia y calibre
    
Label(miframe, text=("Nivel de tensión del circuito(V)")).grid(row=0,column=6,padx=5,pady=5)
Entry(miframe, width=5, textvariable=tension).grid(row=0,column=7,padx=5,pady=5)
tension.set(120)
Label(miframe, text=("Factor potencia del circuito")).grid(row=1,column=6,padx=5,pady=5)
Entry(miframe,width=5,textvariable=factor).grid(row=1,column=7,padx=5,pady=5)
factor.set(1)
Label(miframe, text=("Calibre(AWG)")).grid(row=2,column=6,padx=5,pady=5)
Entry(miframe,width=5,textvariable=calibre).grid(row=2,column=7,padx=5,pady=5)
calibre.set(12)
Label(miframe, text="Regulación en %").grid(row=3,column=6,padx=5,pady=5)
Label(miframe,text=0,textvariable=regu).grid(row=3,column=7,padx=5,pady=5)

#Ahora los botones Calcular regulación, Cargar y Resumen
def calcular():
    global reg
    global me
    global aux
    global calibres
    if material.get()=='PVC':
        calibres={'14':10.1706+0.1903J,'12':6.5617+0.1772J,'10':3.9370+0.1640J,'8':2.5591+0.1706J,
        '6':1.6076+0.1673J,'4':1.0171+0.1575J,'2':0.6234+0.1476J,'1':0.5052+0.1509J,
        '0':0.3937+0.1444J,'00':0.3281+0.1411J,'000':0.2526+0.1378J,'0000':0.2034+0.1345J,
        '250':0.1706+0.1345J,'300':0.1444+0.1345J,'350':0.1247+0.1312J,'400':0.1083+0.1312J,
        '500':0.0886+0.1280J,'600':0.0755+0.1280,'750':0.0623+0.1247J,'1000':0.0492+0.1214J}
    elif material.get()=='Aluminio':
        calibres={'14':10.1706+0.1903J,'12':6.5617+0.1772J,'10':3.9370+0.1640J,'8':2.5591+0.1706J,
        '6':1.6076+0.1673J,'4':1.0171+0.1575J,'2':0.6562+0.1476J,'1':0.5249+0.1509J,
        '0':0.4265+0.1444J,'00':0.3281+0.1411J,'000':0.2690+0.1378J,'0000':0.2198+0.1345J,
        '250':0.1870+0.1345J,'300':0.1608+0.1345J,'350':0.1411+0.1312J,'400':0.1247+0.1312J,
        '500':0.1050+0.1280J,'600':0.0919+0.1280,'750':0.0787+0.1247J,'1000':0.0623+0.1214J}
    elif material.get()=='Acero':
         calibres={'14':10.1706+0.2395J,'12':6.5617+0.2231J,'10':3.9370+0.2067J,'8':2.5591+0.2133J,
        '6':1.6076+0.21J,'4':1.0171+0.1969J,'2':0.6562+0.1870J,'1':0.5085+0.1870J,
        '0':0.3987+0.1804J,'00':0.3281+0.1772J,'000':0.2270+0.1706J,'0000':0.2067+0.1673J,
        '250':0.1772+0.1706J,'300':0.1476+0.1673J,'350':0.1280+0.1640J,'400':0.1148+0.1608J,
        '500':0.0951+0.1575J,'600':0.0820+0.1575,'750':0.0689+0.1575J,'1000':0.0591+0.15092J}
        
    for i in range (8):
        aux[i]=(pot[i].get()*dis[i].get())
    me=sum(aux)
    r=calibres[calibre.get()]
    fp=float(factor.get())
    ref=r.real+r.imag*(((1-(fp**2))**(1/2))/fp)
    k=ref/(5*(tension.get()**2))
    reg=me*ref/(5*(tension.get()**2))
    regu.set(reg)

Button(miframe,text="Calcular regulación",command=calcular).grid(row=4,column=6,padx=5,pady=5)
def cargar():
    calcular()
    global cont
    global matriz
    global me
    global reg
    a=0   
    for i in range(8):
        a=a+pot[i].get()
    matriz[cont][0]=a
    matriz[cont][1]=me
    matriz[cont][2]=reg
    matriz[cont][3]=calibre.get()
    cont=cont+1
    for i in range(8):
        pot[i].set(0)
        dis[i].set(0)
    regu.set(0)

Button(miframe,text="Cargar",command=cargar).grid(row=5,column=6,padx=5,pady=5)

def resumen():
    resumen=Tk()
    resuframe=Frame(resumen)
    resuframe.pack()
    Label(resuframe, text=("Circuito #")).grid(row=0,column=0,padx=5,pady=5)
    Label(resuframe, text=("Potencia[W]")).grid(row=0,column=1,padx=5,pady=5)
    Label(resuframe, text=("Momento eléctrico[W*m]")).grid(row=0,column=2,padx=5,pady=5)
    Label(resuframe, text=("Regulación [%]")).grid(row=0,column=3,padx=5,pady=5)
    Label(resuframe, text=("Calibre")).grid(row=0,column=4,padx=5,pady=5)
    global cont
    global matriz
    for i in range(cont):
        Label(resuframe, text=(str(i+1))).grid(row=(i+1),column=0,padx=5,pady=5)
        Label(resuframe, text=(str(matriz[i][0]))).grid(row=(i+1),column=1,padx=5,pady=5)
        Label(resuframe, text=(str(matriz[i][1]))).grid(row=(i+1),column=2,padx=5,pady=5)
        Label(resuframe, text=(str(matriz[i][2]))).grid(row=(i+1),column=3,padx=5,pady=5)
        Label(resuframe, text=(str(matriz[i][3]))).grid(row=(i+1),column=4,padx=5,pady=5)
        
    resumen.mainloop()
    
Button(miframe,text="Resumen",command=resumen).grid(row=6,column=6,padx=5,pady=5)
material=StringVar()
material.set('PVC')

materiales=('PVC', 'Aluminio', 'Acero')

OptionMenu(miframe,material,*materiales).grid(row=6,column=7,padx=5,pady=5)


    
raiz.mainloop()
