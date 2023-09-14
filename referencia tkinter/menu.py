import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pygame
import os
import msvcrt



window = tk.Tk() #Creación ventana principal

# Configuración de la pantalla completa
window.attributes("-fullscreen", True)     #Pantalla completa

# Configuración de la imagen de fondo de pantalla raíz
fondo = tk.PhotoImage(file="Image/fotor_2023-4-21_17_36_5.png")
w, h = fondo.width(), fondo.height()                                 #Fuente:ChatBotGPT
window.geometry("%dx%d+0+0" % (w, h))                                #...
window.configure(cursor="star")                                      #...

# Mostrar la imagen de fondo en un label
background_label = tk.Label(window, image=fondo)                   #Fuente:ChatBotGPT
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Establecer musica de inicio                                        #Fuente:ChatBotGPT
pygame.init()                 #Inicia la librería pygame
volumen = 0.5
def cambiar_volumen():
    global volumen
    if 'Up' in window.teclas_pulsadas:
        if volumen < 1.0:
            volumen += 0.01
            pygame.mixer.music.set_volume(volumen)
    elif 'Down' in window.teclas_pulsadas:
        if volumen > 0.0:
            volumen -= 0.01
            pygame.mixer.music.set_volume(volumen)
    window.after(10, cambiar_volumen)

def tecla_pulsada(evento):
    window.teclas_pulsadas.add(evento.keysym)

def tecla_soltada(evento):
    window.teclas_pulsadas.remove(evento.keysym)

def iniciar():
    pygame.mixer.music.load('Sound/musica_inicio.mp3')
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play()


    window.teclas_pulsadas = set()
    window.bind('<KeyPress>', tecla_pulsada)      #Se enlaza "pulsada" con la función
    window.bind('<KeyRelease>', tecla_soltada)    #Se enlaza "tecla_soltada" con la función
    window.after(10, cambiar_volumen)   #Se establece a 10ms

# Iniciar automáticamente la configuración de volumen al ejecutar el juego
iniciar()

#Configuración botón salir del programa desde la pantalla principal
def salir():
    window.destroy()

boton1=tk.Button(window, text="Salir del juego",
                 command=salir,
                 fg="gray1",
                 bg="DodgerBlue4",
                 relief="sunken",
                font=("System 16 bold"),
                 cursor="exchange")
boton1.pack()
boton1.place(x=1190,y=700, height=45, width=130)

#Cinfiguración botón sobre el autor
def acerca_de():
    # Crear botón acerca_de
    acerca_de = Toplevel()
    acerca_de.attributes("-fullscreen", True)

    # Cargar la imagen de fondo
    imagen = Image.open("Image/acerca_de.png")
    imagen = ImageTk.PhotoImage(imagen)

    # Superpone la imagen sobre la window de acerca de    #Fuente: ChatBotGTP
    fondo = Label(acerca_de, image=imagen)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    acerca_de.configure(cursor = "star")

    def salir():
        acerca_de.destroy()

    boton1 = tk.Button(acerca_de, text="Volver",
                 command=salir,
                 fg="snow",
                 bg="gray15",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack()
    boton1.place(x=1150, y=20, height=80, width=180)



    # Mostrar ventana "acerca_de"
    acerca_de.mainloop()

#Configuración botón "como_jugar"
def como_jugar():
    # Crear botón "como_jugar
    como_jugar = Toplevel()
    como_jugar.attributes("-fullscreen", True)

    # Cargar la imagen de fondo
    imagen = Image.open("Image/fotor_2023-4-21_19_2_50.png")
    imagen = ImageTk.PhotoImage(imagen)

    # Superpone la imagen sobre la window de acerca de
    fondo = Label(como_jugar, image=imagen)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    como_jugar.configure(cursor = "star")

    def salir():
        como_jugar.destroy()

    boton1 = tk.Button(como_jugar, text="Volver",
                 command=salir,
                 fg="snow",
                 bg="RoyalBlue4",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack()
    boton1.place(x=1150, y=20, height=50, width=150)

    como_jugar.mainloop()  #Muestra ventana "como_jugar"

#Colorcar botón "acerca_de" en pantalla principal
boton2=tk.Button(window, text="Acerca de",fg="snow",
                 bg="azure4",
                 relief="sunken",
                 font=("System 30 bold"),command=acerca_de,
                 cursor="exchange")
boton2.pack
boton2.place(x=70,y=170,)

#Colorcar botón "cómo_jugar" en pantalla principal

boton3=tk.Button(window, text="Cómo jugar",fg="snow",
                 bg="dim gray",
                 relief="sunken",
                 font=("System 30 bold"), command=como_jugar,
                 cursor="exchange")
boton3.pack
boton3.place(x=300,y=275)

boton_principal= tk.Button(window, text="JUEGA!!",fg="snow",
                 bg="goldenrod",
                 relief="sunken",
                 font=("System 30 bold"), 
                 command=lambda: [detener(),os.system('game.py')],
                 cursor="exchange",)

def detener():
    pygame.mixer.music.stop()


boton_principal.pack
boton_principal.place(x=860,y=530)


   


window.mainloop()