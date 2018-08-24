# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
import time

class Airpor(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.move_x = 0
        self.movr_y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/hero1.png')
        self.bullet_list = []#子弹存储对象

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def moveby_x(self):
        self.x-=self.move_x

    def fire(self):
        but = Bullet(self.screen,self.x,self.y)
        self.bullet_list.append(but)

class enumpyAirpor(object):
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.move_x = 5
        self.movr_y = 3
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/enemy0.png')
        self.bullet_list = []#子弹存储对象

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        # for bullet in self.bullet_list:
        #     bullet.display()
        #     bullet.move()
        self.moveby_x()

    def moveby_x(self):
        self.x+=self.move_x
        self.y+=self.movr_y
        if self.x >480-50:
            self.move_x = -5
        elif self.x <0 :
            self.move_x = 5

    def fire(self):
        but = Bullet(self.screen,self.x,self.y)
        self.bullet_list.append(but)

class Bullet(object):
    def __init__(self,screen_tem,x,y):
        self.x = x+40
        self.y = y-20
        self.screen = screen_tem
        self.image = pygame.image.load('./feiji/bullet.png')
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -=5

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
                airpor_tem.fire()
        elif event.type == KEYUP:
            airpor_tem.move_x = 0

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load(r'/Users/xc/Documents/PythonWork/pygame/feiji/background.png')

    #3. 创建一个飞机对象
    hero = Airpor(screen)
    #4.创建敌机
    enumpy = enumpyAirpor(screen)


    while True:
        screen.blit(background, (0,0))
        hero.display()
        enumpy.display()
        hero.moveby_x()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()