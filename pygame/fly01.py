# -*- coding:utf-8 -*-
import pygame,math
from pygame.locals import *
import sys
 
pygame.init()
screen = pygame.display.set_mode((480,853),pygame.RESIZABLE,0)
pygame.display.set_caption("Python.pygame学习（二）绘制图形");
 
blue = 0,0,200
color = 255,255,0
position = 140,400
radius = 100
width = 2
colorrect = 200,200,0
positionX = 100
positionY = 100
movX = 2
movY = 2
rectposition = 100,100,100,100
 
while True:
    for event in pygame.event.get():
        if event.type in(QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    # 圆绘制
    pygame.draw.circle(screen, color, position, radius, width)
  
    positionX += movX
    positionY += movY
 
    if positionX>380 or positionX<0:
        movX = -movX
    if positionY>753 or positionY<0:
        movY = -movY
    posNew = positionX,positionY,100,100
    # 矩形绘制
    pygame.draw.rect(screen,colorrect,posNew,0)
    # 多边形绘制
    sixpos = ((150,150),(150,300),(50,200))
    pygame.draw.polygon(screen,color,sixpos,3)
    # 椭圆
    pygame.draw.ellipse(screen, (0xCC, 0xCC, 0x00), ((150, 150), (120, 150)), 0)
    #弧形绘制 cgrct(圆心，半径相同为圆)
    pygame.draw.arc(screen,color,((240, 150), (200, 200)), 0, math.pi, 2)
    #线段绘制
    pygame.draw.line(screen,color,(100,100),(300,200),3)
    #绘制多个连续的线段   线条（Surface，color，closed，pointlist，width = 1）
    #  closed为true 最后一个点和开始点会连接
    pygame.draw.lines(screen,color,True,((400,100),(400,200),(350,400)),2)
    #绘制抗锯齿线段 aaline（Surface，color，startpos，endpos，blend = 1） - > Rect  
    #  如果blend为true，则阴影将与现有像素阴影混合而不是覆盖它们
    pygame.draw.aaline(screen,color,(200,500),(300,700),1)
     #绘制多个抗锯齿线段 aalines（Surface，color，closed，pointlist，blend = 1） - > Rect 
     # closed参数是一个简单的布尔值，如果为true，则在第一个和最后一个点之间绘制一条线
 
    pygame.draw.aalines(screen,color,True,((200,500),(300,700),(400,750)),1)
    pygame.display.update()

