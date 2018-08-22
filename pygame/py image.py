# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
 
white = 255,255,255
blue = 100,0,200
 
pygame.init()
screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE, 0)
pygame.display.set_caption("pygame学习（三）图片显示")
 
space = pygame.image.load('Classes/1.png')
# pygame.image.save(space, '1.jpg')

space = pygame.transform.smoothscale(space,(100,100))
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello Pygame", True, blue)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
 
    screen.fill(blue)
    screen.blit(space, (10,20))
    pygame.display.update()