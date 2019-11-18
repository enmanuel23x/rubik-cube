import pygame
from Rubik import Rubik
from pygame.locals import *
x1=0
y1=0
pos="none"
RUBIK_SPRITE_WIDTH = 300
RUBIK_SPRITE_HEIGHT = 300


class RubikSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        self.left = 50
        self.top = 50

        self.rubik = Rubik()

    def draw(self, screen,ColorSprites):
        
        current_top = self.top
        for row in self.rubik.front_face:
            current_left = self.left
            for color in row:
                current_color = ColorSprites.get(color)
                screen.blit(current_color, (current_left, current_top))
                current_left += 100
            current_top += 100
    def updatemouse1(selcf,click):
        #GUARDAMOS LA POSICION AL PRESIONAR EL CLICK_1 EN UNA VARIABLE GLOBAL
        global x1
        global y1
        global pos
        x=click[0]
        y=click[1]
        x1=x
        y1=y
        #FILA 1
        if y>=50 and y<=148:
            #COLUMNA 1   
            if x>=50 and x<=150:
                pos=11
            #COLUMNA 2    
            if x>=151 and x<=249:
                pos=12
            #COLUMNA 3    
            if x>=250 and x<=350:
                pos=13
                
        #FILA 2    
        if y>=151 and y<=249:
            #COLUMNA 1   
            if x>=50 and x<=150:
                pos=21
            #COLUMNA 2   
            if x>=151 and x<=249:
                pos=22    
            #COLUMNA 3    
            if x>=250 and x<=350:
                pos=23
        #FILA 3    
        if y>=250 and y<=350:
            #COLUMNA 1   
            if x>=50 and x<=150:
                pos=31
            #COLUMNA 2    
            if x>=151 and x<=249:
                pos=32
            #COLUMNA 3    
            if x>=250 and x<=350:
                pos=33
            
    def updatemouse2(self, click):
        global x1
        global y1
        global pos
        #GUARDAMOS LA POSICION AL PRESIONAR EL CLICK_1
        x2=click[0]
        y2=click[1]
        #COMPARAMOS SI EL MOVIMIENTO ES VERTICAL U HORIZONTAL
        if (abs(abs(x2)-abs(x1))>abs(abs(y2)-abs(y1))):
            #HORIZONTAL
            #FILA 1  
            if (y2>=50 and y2<=150) and (pos==11 or pos==12 or pos==13):
                if x1<x2:
                    self.rubik.rotate_top_face_left()
                else:
                    self.rubik.rotate_top_face_right()
            #FILA 2    
            if (y2>=151 and y2<=249) and (pos==21 or pos==22 or pos==23):
                if x1<x2:
                    self.rubik.rotate_top_face_right()
                    self.rubik.rotate_bottom_face_right()
                    self.rubik.rotate_cube_left()
                else:
                    self.rubik.rotate_top_face_left()
                    self.rubik.rotate_bottom_face_left()
                    self.rubik.rotate_cube_right()
                    
            #FILA 3    
            if (y2>=250 and y2<=350) and (pos==31 or pos==32 or pos==33):
                if x1<x2:
                    self.rubik.rotate_bottom_face_left()
                else:
                    self.rubik.rotate_bottom_face_right()
        elif (abs(abs(x2)-abs(x1))<abs(abs(y2)-abs(y1))):
            #VERTICAL
            #COLUMNA 1  
            if (x2>=50 and x2<=150) and (pos==11 or pos==21 or pos==31):
                if y1>y2:
                    self.rubik.rotate_left_face_downward()
                else:
                    self.rubik.rotate_left_face_upward()
            #COLUMNA 2    
            if (x2>=151 and x2<=249) and (pos==12 or pos==22 or pos==32):
                if y1>y2:
                    self.rubik.rotate_left_face_upward()
                    self.rubik.rotate_right_face_upward()
                    self.rubik.rotate_cube_downward()                    
                else:
                    self.rubik.rotate_left_face_downward()
                    self.rubik.rotate_right_face_downward()
                    self.rubik.rotate_cube_upward()
            #COLUMNA 3    
            if (x2>=250 and x2<=350) and (pos==13 or pos==23 or pos==33):
                if y1>y2:
                    self.rubik.rotate_right_face_downward()
                else:
                    self.rubik.rotate_right_face_upward()
        pos=0

    def updatekey(self, key):
        if key == K_w:
            self.rubik.rotate_cube_upward()
        if key == K_s:
            self.rubik.rotate_cube_downward()
        if key == K_a:
            self.rubik.rotate_cube_left()
        if key == K_d:
            self.rubik.rotate_cube_right()
        if key == K_q:
            self.rubik.rotate_cube_counter_clockwise()
        if key == K_e:
            self.rubik.rotate_cube_clockwise()
        if key == K_j:
            self.rubik.rotate_front_face_counter_clockwise()
        if key == K_k:
            self.rubik.rotate_front_face_clockwise()
        if key == K_u:
            self.rubik.rotate_top_face_left()
        if key == K_i:
            self.rubik.rotate_top_face_right()
        if key == K_n:
            self.rubik.rotate_bottom_face_left()
        if key == K_m:
            self.rubik.rotate_bottom_face_right()
        if key == K_y:
            self.rubik.rotate_left_face_upward()
        if key == K_h:
            self.rubik.rotate_left_face_downward()
        if key == K_o:
            self.rubik.rotate_right_face_upward()
        if key == K_l:
            self.rubik.rotate_right_face_downward()
        if key == K_r:
            self.rubik = Rubik()
