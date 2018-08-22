# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *

class Airpor(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.move_x = 0
        self.movr_y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('Classes/feiji/hero1.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def moveby_x(self):
        self.x-=self.move_x
   

def key_control(airpor_tem):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                airpor_tem.move_x = 5
            elif event.key == K_RIGHT:
                airpor_tem.move_x = -5
            elif event.key == K_SPACE:
                print('space')
        elif event.type == KEYUP:
            airpor_tem.move_x = 0

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("Classes/feiji/background.png")

    #3. 创建一个飞机对象
    hero = Airpor(screen)



    while True:
        screen.blit(background, (0,0))
        hero.display()
        hero.moveby_x()
        pygame.display.update()
        key_control(hero)

if __name__ == "__main__":
    main()