import pygame as pg
import quadtree
from quadtree import *

import numpy as np

from random import randint
import random as rd


import os

# Get the size
# of the terminal
size = os.get_terminal_size()

# set the size of terminal
x, y = size
x *= 20
y *= 20
size = (x, y)
width, height = size

pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption('bBOX')
radius = 3
SIZE = 4


def genPoints(bbox, x=500):

    points = []
    for p in range(x):
        x = randint(radius, bbox.w - radius)
        y = randint(radius, bbox.h - radius)
        points.append(Point(x, y))
    return points


def highlightPoints(foundPoints):
    for p in foundPoints:
        
        pg.draw.circle(screen, (230, 99, 60), [p.x, p.y], radius + 3)

if __name__ == '__main__':

    bbox = Rect(size[0]//2,size[1]//2,size[0],size[1])
    qt = QuadTree(bbox)

    points = genPoints(bbox, 500)

    for p in points:
        qt.insert(p)

    foundPoints = []

    wh = []
    xy = []

  
    start = (0, 0)
    size = (0, 0)
  
    switch = pg.Rect(351.00, 325.00, 401.00, 375.00)

    running = True
    drawing = False
    r = pg.Rect(0,0,40,40)
    # Game loop
    # keep game running till running  true
    while running:
   
        screen.fill((255,255,255))
           
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                
            elif event.type == pg.MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == pg.MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                wh.append(size)
                xy.append(end)
                drawing = False

          
              
            if drawing == True:
              wh.clear()
              xy.clear()
              foundPoints.clear()
              
                
  
        
        for x,y in xy:
          print("x,y:", x , y)
         
          for w,h in wh:
              nw = w /2
              nh = h/2
              box = Rect(x,y,w,h)
              displayBox = pg.Rect(x - nw ,y -nh,w,h)
              pg.draw.rect(screen,(155,33,0),displayBox,SIZE)
              qt.query(box, foundPoints)
             
            
                   
                
              
      
      
        
      

  
              
   
     
        
  
        highlightPoints(foundPoints)
        qt.draw(screen,radius)
        pg.display.update
        pg.display.flip()

      

