# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
 
white = 255,255,255
blue = 100,0,200
 
pygame.init()
screen = pygame.display.set_mode((480, 852), pygame.RESIZABLE, 32)
pygame.display.set_caption("pygame学习（三）图片显示")
 
space = pygame.image.load('Classes/1.png')
  #2. 创建一个背景图片
background = pygame.image.load("Classes/feiji/background.png")

    #3. 创建一个飞机图片
hero = pygame.image.load("Classes/feiji/hero1.png")

space = pygame.transform.smoothscale(space,(100,100))

x, y = 210, 700
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            #键盘有按下？
            if event.key == K_LEFT:
                #按下的是左方向键的话，把x坐标减一
                move_x = -3
            elif event.key == K_RIGHT:
                #右方向键则加一
                move_x = 3
            elif event.key == K_UP:
                #类似了
                move_y = -3
            elif event.key == K_DOWN:
                move_y = 3
            elif event.key == K_SPACE:
                print('space')
        elif event.type == KEYUP:
            #如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0
    x+=move_x
    y+=move_y
 
    screen.blit(background, (0,0))
    screen.blit(hero, (x,y))
    pygame.display.update()