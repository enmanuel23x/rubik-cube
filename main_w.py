from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.image import Image
import os
import random
import pygame
import sys
from pygame.locals import *
from kivy.uix.popup import Popup
from os import scandir, getcwd
from kivy.core.window import Window
Window.borderless = True
import glob
from Color import Color
prev=0
colors=""
# Declaración de constantes y variables
WHITE = (255, 255, 255)
BLACK = (0,0,0)
name=""
SCREEN_WIDTH = 725
SCREEN_HEIGTH = 530
direct=""
ruta=''
route=''
rutap='../src/resources/'
band=0
temas=['blue.png', 'green.png', 'muestra.png', 'orange.png', 'red.png', 'white.png', 'yellow.png']
#diseño de la ventana
Builder.load_string("""
#: kivy 1.9.0
<Popup_no>:
    size_hint: .5, .5
    auto_dismiss: False
    title: "Error"
    Label:
        text: "Ningun tema seleccionado Por favor seleccione un tema"
        text_size: 240, None
        on_touch_down: root.dismiss()
        font_size: 18
<Window_1>:
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Cubo de Rubik"
        color: (0,0,0,1)
        font_size: 35
        center_x: root.width * 0.5
        center_y: root.top * 0.9
#Tema
    Label:
        text: "Tema: "
        color: (0,0,0,1)
        font_size: 25
        right: root.width * 0.49
        center_y: root.top * 0.8
    Spinner:
        id: s_tema
        text: ""
        font_size: 25
        values: [""]
        size: (110,50)
        center_x: root.width * 0.54
        center_y: root.top * 0.8
        on_text: root.spinner_text(s_tema,img)
        on_press: root.spinner_clicked(s_tema,img)
#Imagen
    Image:
        id: img
        size_hint: None, None
        size: 300,300
        center_x: root.width * 0.5
        center_y: root.top * 0.5
        source: None
#Terminar
    Button:
        id: close
        font_size: 20
        center_x: root.width * 0.2
        center_y: root.top * 0.15
        text: "Salir"
        size: (130,70)
        on_press: root.exit()
    Button:
        id: save
        font_size: 20
        center_x: root.width * 0.8
        center_y: root.top * 0.15
        text: "Continuar"
        size: (130,70)
        on_press: root.save(s_tema.text)
""")
#Main del cubo en pygame
class Cubo:
    def render_text(text, font, screen, pos_x, pos_y):
        TextSurf = font.render(text, True, BLACK)
        TextRect = TextSurf.get_rect()
        TextRect.left, TextRect.top = (pos_x, pos_y)
        screen.blit(TextSurf, TextRect)

    def render_text_center(text, font, screen, pos_x, pos_y):
        TextSurf = font.render(text, True, BLACK)
        TextRect = TextSurf.get_rect()
        TextRect.center = (pos_x, pos_y)
        screen.blit(TextSurf, TextRect)

    def main():
        # Se inicializa el juego
        global name
        global band
        pygame.init()
        pygame.display.set_caption("Rubik "+name)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        #Inicializar los colores
        if band==1:
            ColorSprites.main()
            band=0
        from RubikSprite import RubikSprite
        rubik_sprite = RubikSprite(SCREEN_WIDTH, SCREEN_HEIGTH)
        global rutap
        font = pygame.font.Font(rutap+'NotoSerif-Regular.ttf', 15)
        font_big = pygame.font.Font(rutap+'NotoSerif-Regular.ttf', 20)

        clock = pygame.time.Clock()

        # Bucle principal
        while True:
            # keys = pygame.key.get_pressed()
            clock.tick()

            # Se comprueban los eventos para ver si se solicitó cerrar la aplicación
            if pygame.event.get(QUIT):
                pygame.quit()
                sys.exit(0)
            # Si es un evento de soltar tecla, se manda a actualizar el cubo
            global prev
            event = pygame.event.poll()
            click = pygame.mouse.get_pressed()[0]
            
            if event.type == KEYUP:
                rubik_sprite.updatekey(event.key)
            if event.type == MOUSEBUTTONDOWN and click==1:
                prev=1
                rubik_sprite.updatemouse1(pygame.mouse.get_pos())
            if event.type == MOUSEBUTTONUP and prev==1:
                rubik_sprite.updatemouse2(pygame.mouse.get_pos())
                prev=0
            # 1.- Se dibuja la pantalla
            screen.fill(WHITE)

            # pygame.draw.rect(screen, color, pygame.Rect(10, 10, 60, 60))
            global colors
            rubik_sprite.draw(screen,colors)

            Cubo.render_text("Instrucciones", font_big, screen, 400, 50)
            Cubo.render_text("w: rotar cubo hacia arriba", font, screen, 400, 85)
            Cubo.render_text("s: rotar cubo hacia abajo", font, screen, 400, 100)
            Cubo.render_text("a: rotar cubo hacia izquierda", font, screen, 400, 115)
            Cubo.render_text("d: rotar cubo hacia derecha", font, screen, 400, 130)
            Cubo.render_text("u: rotar fila superior hacia izquierda", font, screen, 400, 145)
            Cubo.render_text("i: rotar fila superior hacia derecha", font, screen, 400, 160)
            Cubo.render_text("j: rotar cara frontal hacia izquierda", font, screen, 400, 175)
            Cubo.render_text("k: rotar cara frontal hacia derecha", font, screen, 400, 190)
            Cubo.render_text("n: rotar fila inferior hacia izquierda", font, screen, 400, 205)
            Cubo.render_text("m: rotar fila inferior hacia derecha", font, screen, 400, 220)
            Cubo.render_text("y: rotar primera columna hacia arriba", font, screen, 400, 235)
            Cubo.render_text("h: rotar primera columna hacia abajo", font, screen, 400, 250)
            Cubo.render_text("o: rotar última columna hacia arriba", font, screen, 400, 265)
            Cubo.render_text("l: rotar última columna hacia abajo", font, screen, 400, 280)
            Cubo.render_text("r: reiniciar cubo", font, screen, 400, 295)

            Cubo.render_text_center("Integrantes", font_big, screen, 400, 400)
            Cubo.render_text_center("Josue Márquez, C.I.: 24.471.739", font, screen, 400, 435)
            Cubo.render_text_center("Emmanuel León, C.I.: 27.725.294", font, screen, 400, 450)
            Cubo.render_text_center("Gabriel Sieralta, C.I.: 27.725.235", font, screen, 400, 465)
            Cubo.render_text_center("Estefanía Gainza, C.I.: 23.570.742", font, screen, 400, 480)

            # 3.- Se actualiza la pantalla
            pygame.display.update()
#Popup(sin tema seleccionado)
class Popup_no(Popup):
    pass
#Clase para inicializar los colores(caras)
class ColorSprites:
    def main():
        global route
        global colors
        red = pygame.image.load(route+'red.png').convert()
        blue = pygame.image.load(route+'blue.png').convert()
        white = pygame.image.load(route+'white.png').convert()
        yellow = pygame.image.load(route+'yellow.png').convert()
        green = pygame.image.load(route+'green.png').convert()
        orange = pygame.image.load(route+'orange.png').convert()
        colors = {Color.red: red, Color.blue: blue,
                  Color.white: white, Color.yellow: yellow, Color.green: green, Color.orange: orange}
#Clase que maneja las funciones de la ventana
class Window_1(Widget):
    #abrir popup(sin tema seleccionado)
    def open_popup_no(self):
        the_popup = Popup_no()
        the_popup.open()
    #inicio
    def __init__(self,**kwargs):
        self.update_dir_data()
        super(Window_1,self).__init__(**kwargs)
    #funcion para actualizar directorios
    def update_dir_data(self):
        global direct
        global rutap
        direct =self.ls(rutap+'textures/')
    #Funcion que devuelve directorios
    def scan(self,path):
        dirs = os.listdir(path)
        return dirs
    #Actualizar valores del spinner
    def spinner_clicked(self,spinner,img):
        global direct
        spinner.values=direct
    #funcion para actualizar directorios
    def ls(self,path):
        global band
        global rutap
        dirs = os.listdir(path)
        for i in range(len(dirs)):
            if dirs[i]=="NotoSerif-Regular.ttf":
                del dirs[i]
                break
        if band==0:
            band=1
            k=0
            leng=len(dirs)
            contleng=0
            for dfile in dirs:
                route=rutap+'textures/'+str(dfile)+'/'
                arch=len(glob.glob(rutap+'textures/'+str(dfile)+'/*'))
                if arch>=7:
                    files = self.ls(route)
                    cont=0
                    global temas
                    i=0
                    rang=len(files)-1
                    for file in files:
                        for j in range(7):
                            if file==temas[j]:
                                cont+=1
                                break
                        if cont!=7 and i==rang:
                            del dirs[k]
                        i+=1
                    
                    contleng+=1
                    if contleng==(leng):
                        band=0
                else:
                    del dirs[k]
                k+=1
        return dirs
    #funcion para actualizar la imagen
    def img_update(self,img):
        global ruta
        global route
        img.source = ruta
        img.reload()
    #funcion para salir
    def exit(self):
        App.get_running_app().stop()
        Window.close()
    #funcion para actualizar imagen, la variable route y la variables ruta
    def spinner_text(self,spinner,img):
        global ruta
        global route
        global rutap
        route=rutap+'textures/'+str(spinner.text)+'/'
        ruta=str(route)+"muestra.png"
        self.img_update(img)
    #funcion para modificar las rutas y abrir la ventana de pygame
    def save(self,nam):
        if nam!="":
            global route
            global name
            name=nam
            #confirmar
            self.exit()
            Cubo.main()
            
        else:
            self.open_popup_no()
        
class LatihanApp(App):
    def build(self):
        return Window_1()



if __name__ == '__main__':
    LatihanApp().run()
