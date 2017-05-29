from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading
import winsound

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
            robot.set_img("22")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()-5
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("21")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()-5
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
        except Exception as errtxt:
            print ("Error en hilo")
    def ver_izq(self):
        a = Thread(target=self.izq, args=())   
        a.start()

    def der(self):
        try:
            robot.set_img("1")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()+5
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("0")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.01)
            self.xpos=self.get_xpos()+5
            lbl.place(x=self.get_xpos(),y=self.get_ypos())
            time.sleep(0.01)
        except Exception as errtxt:
            print ("Error en hilo")
    def ver_der(self):
        b = Thread(target=self.der, args=())   
        b.start()

    def dance(self):
        imgnum = 7
        ciclo = 0
        try:
            while ciclo < 3:
                if imgnum == 17:
                    ciclo += 1
                    imgnum = 9
                robot.set_img(str(imgnum))
                img=cargarImagen(robot.get_img())
                lbl.configure(image=img)
                lbl.image=img
                time.sleep(0.1)
                imgnum += 1
            robot.set_img("7")
            img=cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image=img
            time.sleep(0.1)
        except Exception as errtxt:
            print ("Error en hilo")
    def ver_dance(self):
        c = Thread(target=self.dance, args=())   
        c.start()

    def music (self):
        global musica
        musica += 1
        if musica % 2 == 1:
            winsound.PlaySound('C:\\Users\\este0\\Desktop\\Tarea-Programada-2\\Material\\SuperMoon.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)  
    
robot=Robot("Carmen","0",300,0)
musica = 0 

def cargarImagen(nombre):
    ruta = os.path.join('Material',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

root=Tk()
root.minsize(1000,500)
root.resizable(NO,NO)

cont=Canvas(root,width=1000,height=500,bg="#000000")
cont.place(x=0,y=0)

img=cargarImagen(robot.get_img())
lbl=Label(root,bg="#000000",image=img,width=400,height=500)
lbl.place(x=robot.get_xpos(),y=robot.get_ypos())
lbl.image=img

def Left (event):
    robot.ver_izq() 
root.bind('<Left>', Left)

def Right (event):
    robot.ver_der() 
root.bind('<Right>', Right)   

def Up (event):
    robot.ver_dance() 
root.bind('<Up>', Up)

def Down (event):
    robot.music() 
root.bind('<Down>', Down)

root.mainloop()
