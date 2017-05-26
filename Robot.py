from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading

class Robot:
    def __init__ (self, nom, img, xpos, ypos):
        self.nom=nom
        self.img=img+".gif"
        self.xpos=xpos
        self.ypos=ypos
    def set_img(self, img):
        self.img=img+".gif"
    def get_img(self):
        return self.img
    def get_nom(self):
        return self.nom
    def set_xpos(self, xpos):
        self.xpos=xpos
    def get_xpos(self):
        return self.xpos
    def set_ypos(self, ypos):
        self.ypos=ypos
    def get_ypos(self):
        return self.ypos

    def izq(self):
        try:
            robot.set_img("left")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()-10
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("robot")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
        except Exception as errtxt:
            print ("Error en hilo")
    def ver_izq(self):
        a = Thread(target=self.izq, args=())   
        a.start()

    def der(self):
        try:
            robot.set_img("right")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()+10
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("robot")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
        except Exception as errtxt:
            print ("Error en hilo")
    def ver_der(self):
        b = Thread(target=self.der, args=())   
        b.start() 
    
robot=Robot("Carmen","Robot",400,0)

def cargarImagen(nombre):
    ruta = os.path.join('Material',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

root=Tk()
root.minsize(1000,500)
root.resizable(NO,NO)

cont=Canvas(root,width=1000,height=500,bg="#016101")
cont.place(x=0,y=0)

img=cargarImagen(robot.get_img())
lbl=Label(root,bg="#016101",image=img)
lbl.place(x=robot.get_xpos(),y=robot.get_ypos())
lbl.image=img

entrada=Entry(root,width=30)
entrada.place(x=30,y=0)

#boton=Button(root,command=robot.ver_izq,text="izquierda")
#boton.place(x=100,y=425)

def Left (event):
    robot.ver_izq() 
root.bind('<Left>', Left)

#boton=Button(root,command=robot.ver_der,text="derecha")
#boton.place(x=100,y=450)

def Right (event):
    robot.ver_der() 
root.bind('<Right>', Right)

root.mainloop()
