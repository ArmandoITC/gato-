from tkinter import *
import time
#matriz de 5x5 centro otro colo 4 botones arriba abajo 
global A,T,L,B,ganador,vacio
A=[["A","A","A"],["A","A","A"],["A","A","A"]]
B=[["","",""],["","",""],["","",""]]
T=[["","",""],["","",""],["","",""]]
ganador=1
EMPATE=0
vacio=2
def apagado ():
    cuadro00.config(state="disable")
    cuadro10.config(state="disable")
    cuadro20.config(state="disable")
    cuadro01.config(state="disable")
    cuadro11.config(state="disable")
    cuadro21.config(state="disable")
    cuadro02.config(state="disable")
    cuadro12.config(state="disable")
    cuadro22.config(state="disable")

def empate():
    global A,ganador,vacio
    i=0
    e=0
    vacio=0
    for i in [0,1,2]:
        for e in [0,1,2]:
            if(A[i][e]=="x" or A[i][e]=="o"):
                vacio=vacio+1
    if(vacio==9):
        l=Label(ventana,text="empate").grid(column=12,row=12)
        apagado()           
  
     #l=Label(ventana,text=("A","[",i,"]","[",e,"]","=",A[i][e])).grid(column=6+i,row=6+e)




def ganador ():
    global A
    i=0
    for i in [0,1,2]:
        if(A[i][0]==A[i][1]==A[i][2]=="x" or A[i][0]==A[i][1]==A[i][2]=="o"):
            l=Label(ventana,text=("Has ganado ",A[i][0])).grid(column=12,row=12)
            apagado()
    i=0
    for i in [0,1,2]:
        if(A[0][i]==A[1][i]==A[2][i]=="x" or A[0][i]==A[1][i]==A[2][i]=="o"):
            l=Label(ventana,text=("Has ganado ",A[0][i])).grid(column=12,row=12)
            apagado()
    if(A[0][0]==A[1][1]==A[2][2]=="x" or A[0][0]==A[1][1]==A[2][2]=="o"):
        l=Label(ventana,text=("Has ganado ",A[0][0])).grid(column=12,row=12)
        apagado()
    if(A[0][2]==A[1][1]==A[2][0]=="x" or A[0][2]==A[1][1]==A[2][0]=="o"):
        l=Label(ventana,text=("Has ganado ",A[0][2])).grid(column=12,row=12)
        apagado()
    



    
def obtener ():
    global A
    i=0
    e=0
    for e in [0,1,2]:
        for i in [0,1,2]:
            if(A[i][e]!="o" or A[i][e]!="x"):
                A[i][e]=T[i][e].get()
                #l=Label(ventana,text=("A","[",i,"]","[",e,"]","=",A[i][e])).grid(column=6+i,row=6+e)
    ganador()      
    empate()

ventana=Tk()
for i in [0,1,2]:
    L=0
    for e in [0,1,2]:
        T[i][e]=StringVar()
    print()
l=Label(ventana,text="usa o, x minusculas").grid(column=13,row=13)
cuadro00=Entry(ventana,textvariable=T[0][0],state="normal",width=2)
cuadro00.grid(column=1,row=1)
B=Button(ventana,text="terminar turno",command=obtener).grid(column=10,row=1)
cuadro10=Entry(ventana,textvariable=T[1][0],state="normal",width=2)
cuadro10.grid(column=1,row=2)

cuadro20=Entry(ventana,textvariable=T[2][0],state="normal",width=2)
cuadro20.grid(column=1,row=3)

cuadro01=Entry(ventana,textvariable=T[0][1],state="normal",width=2)
cuadro01.grid(column=2,row=1)

cuadro11=Entry(ventana,textvariable=T[1][1],state="normal",width=2)
cuadro11.grid(column=2,row=2)

cuadro21=Entry(ventana,textvariable=T[2][1],state="normal",width=2)
cuadro21.grid(column=2,row=3)

cuadro02=Entry(ventana,textvariable=T[0][2],state="normal",width=2)
cuadro02.grid(column=3,row=1)

cuadro12=Entry(ventana,textvariable=T[1][2],state="normal",width=2)
cuadro12.grid(column=3,row=2)

cuadro22=Entry(ventana,textvariable=T[2][2],state="normal",width=2)
cuadro22.grid(column=3,row=3)



ventana.mainloop()
