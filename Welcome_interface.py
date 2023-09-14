from pygame import *
import sys
import time  # Agregamos la importación del módulo time

init()


screen_info = display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = display.set_mode((screen_width, screen_height), FULLSCREEN)


images = []
images_left = []
images_right = []

for i in range(1, 50):
    name = "images/welcome-frame-main/frame-"+str(i)+" (Custom)"+".gif"
    images.append(image.load(name))

    name_left = "images/welcome-frame-right-left/frame-"+str(i)+" (Custom)"+".gif"
    images_left.append(image.load(name_left))

    name_right = "images/welcome-frame-right-left/frame-"+str(i)+" (Custom)"+".gif"
    images_right.append(image.load(name_right))

while True:
    for e in event.get():
        if e.type == QUIT: sys.exit()

    frame = int(time.time()*10)  
    frame %= len(images)  

    screen.fill((255, 255, 255))


    screen.blit(images[frame], (45,0))
    screen.blit(images_left[frame], (-1850, 0))  
    screen.blit(images_right[frame], (1200, 0))  

    display.flip()

