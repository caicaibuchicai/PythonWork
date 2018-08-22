# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *

class Airpor(object):
    def __intit__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load('Classes/feiji/hero1.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5


def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("Classes/feiji/background.png")

    #3. 创建一个飞机对象
    # hero = Airpor(screen)



    while True:

        for event in pygame.event.get():
          if event.type in (QUIT):
              sys.exit()
        screen.fill(blue)
        screen.blit(space, (10,20))
        pygame.display.update()


if __name__ == "__main__":
    main()