from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading
import winsound
import serial

class Robot:
    #Inicializa una instancia
    #E: nombre, imagen, posición en x, posición en y
    #S: instancia del objeto Robot
    #R: ---
    def __init__(self, nom, img, xpos, ypos):
        self.nom = nom
        self.img = img + ".gif"
        self.xpos = xpos
        self.ypos = ypos

    #Define la imagen de la instancia de Robot
    #E: string
    #S: ---
    #R: ---
    def set_img(self, img):
        self.img = img + ".gif"

    #Retorna la imagen de la instancia de Robot
    #E: ---
    #S: imagen
    #R: ---
    def get_img(self):
        return self.img

    #Retorna el nombre de la instancia de Robot
    #E: ---
    #S: nombre
    #R: ---
    def get_nom(self):
        return self.nom

    #Define la posición en el eje x de la instancia de Robot
    #E: num
    #S: ---
    #R: ---
    def set_xpos(self, xpos):
        self.xpos = xpos

    #Retorna la posición en el eje x de la instancia de Robot
    #E: ---
    #S: posición en el eje x
    #R: ---
    def get_xpos(self):
        return self.xpos

    #Define la posición en el eje y de la instancia de Robot
    #E: num
    #S: ---
    #R: ---
    def set_ypos(self, ypos):
        self.ypos = ypos

    #Retorna la posición en el eje y de la instancia de Robot
    #E: ---
    #S: posición en el eje y
    #R: ---
    def get_ypos(self):
        return self.ypos

    #Mueve a la izquierda al robot
    #E: ---
    #S: ---
    #R: ---
    def izq(self):
        try:
            robot.set_img("22")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.01)
            self.xpos = self.get_xpos() - 5
            lbl.place(x=self.get_xpos(), y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("21")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.01)
            self.xpos = self.get_xpos() - 5
            lbl.place(x=self.get_xpos(), y=self.get_ypos())
            time.sleep(0.01)
        except Exception as errtxt:
            print("Error en hilo")

    #Hilo para la función self.izq()
    #E: ---
    #S: Inicia un hilo
    #R: ---
    def ver_izq(self):
        a = Thread(target=self.izq, args=())
        a.start()

    #Mueve a la derecha al robot
    #E: ---
    #S: ---
    #R: ---
    def der(self):
        try:
            robot.set_img("1")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.01)
            self.xpos = self.get_xpos() + 5
            lbl.place(x=self.get_xpos(), y=self.get_ypos())
            time.sleep(0.01)
            robot.set_img("0")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.01)
            self.xpos = self.get_xpos() + 5
            lbl.place(x=self.get_xpos(), y=self.get_ypos())
            time.sleep(0.01)
        except Exception as errtxt:
            print("Error en hilo")

    #Hilo para la función self.der()
    #E: ---
    #S: Inicia un hilo
    #R: ---
    def ver_der(self):
        b = Thread(target=self.der, args=())
        b.start()

    #Pone a bailar al robot
    #E: ---
    #S: ---
    #R: ---
    def dance(self):
        imgnum = 7
        ciclo = 0
        try:
            while ciclo < 3:
                if imgnum == 17:
                    ciclo += 1
                    imgnum = 9
                robot.set_img(str(imgnum))
                img = cargarImagen(robot.get_img())
                lbl.configure(image=img)
                lbl.image = img
                time.sleep(0.1)
                imgnum += 1
            robot.set_img("7")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.1)
        except Exception as errtxt:
            print("Error en hilo")

    #Hilo para la función self.dance()
    #E: ---
    #S: Inicia un hilo
    #R: ---
    def ver_dance(self):
        c = Thread(target=self.dance, args=())
        c.start()

    #Inicia / Detiene la reproducción de música
    #E: ---
    #S: Reproduce o detiene la música
    #R: ---
    def music(self):
        global musica
        musica += 1
        if musica % 2 == 1:
            winsound.PlaySound('C:\\Users\\este0\\PycharmProjects\\Progra\\Material\\SuperMoon.wav',
                               winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)

    #El robot se presenta
    #E: ---
    #S: Reproduce audio
    #R: ---
    def presentation(self):
        winsound.PlaySound('C:\\Users\\este0\\PycharmProjects\\Progra\\Material\\Sony.wav', winsound.SND_ASYNC)
        self.ver_hablar()

    #Animación del robot hablando
    #E: ---
    #S: ---
    #R: ---
    def hablar(self):
        imgnum = 2
        ciclo = 0
        try:
            while ciclo < 7:
                if imgnum == 4:
                    ciclo += 1
                    imgnum = 2
                robot.set_img(str(imgnum))
                img = cargarImagen(robot.get_img())
                lbl.configure(image=img)
                lbl.image = img
                time.sleep(0.25)
                imgnum += 1
            robot.set_img("0")
            img = cargarImagen(robot.get_img())
            lbl.configure(image=img)
            lbl.image = img
            time.sleep(0.25)
        except Exception as errtxt:
            print("Error en hilo")

    #Hilo para la función self.hablar()
    #E: ---
    #S: Inicia un hilo
    #R: ---
    def ver_hablar(self):
        d = Thread(target=self.hablar, args=())
        d.start()

robot = Robot("Sony", "0", 300, 0)
musica = 0

#Carga una imagen en la carptea 'Material'
#E: string
#S: Una imagen
#R: ---
def cargarImagen(nombre):
    ruta = os.path.join('Material', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


root = Tk()
root.title('Sony')
root.minsize(1000, 500)
root.resizable(NO, NO)

cont = Canvas(root, width=1000, height=500, bg="#000000")
cont.place(x=0, y=0)

img = cargarImagen(robot.get_img())
lbl = Label(cont, bg="#000000", image=img, width=400, height=500)
lbl.place(x=robot.get_xpos(), y=robot.get_ypos())
lbl.image = img

ser = serial.Serial('COM3', 9600, timeout=0)
#Función con 2 usos: 1) leer los datos entrantes del arduino; 2) Reproducir acciones de acuerdo a los datos entrantes
#E: ---
#S: Reproduce funciones
#R: ---
def leerArduino():
    while 1:
        try:
            entrada = str(ser.readline());
            datos = str (entrada)
            datos = int(datos[2])
            print(datos)
            if datos == 1:
                robot.ver_izq()
            if datos == 2:
                robot.ver_dance()
            if datos == 3:
                robot.presentation()
            if datos == 4:
                robot.music()
            if datos == 5:
                robot.ver_der()
            time.sleep(0.1)
        except:
            print('Data could not be read')
            time.sleep(0.1)
#Hilo para la función leerArduino()
#E: ---
#S: Inicia un hilo
#R: ---
def verArduino():
    e = Thread(target=leerArduino, args=())
    e.start()
verArduino()
root.mainloop()