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
    boundX = 0
    boundY = 0
    boundw = 100
    boundh = 100
    # make box
    bound = Rect(boundX, boundY,boundw,boundh)
    
 
    
    switch = pg.Rect(351.00, 325.00, 401.00, 375.00)

    running = True
    r = pg.Rect(0,0,40,40)
    # Game loop
    # keep game running till running  true
    while running:
   
        screen.fill((255,255,255))
           
        for event in pg.event.get():

          if event.type == pg.QUIT:
            running = False

  
        boundX += 4
        bound = Rect(boundX, boundY, boundw, boundh)
       
        foundPoints.clear()
        

        displayBox = pg.Rect(boundX - 25, boundY - 25, boundw, boundh)


        qt.query(bound, foundPoints)

        if bound.east_edge > width:
            boundX = 0
            boundY += 50
            bound = Rect(boundX, boundY, boundw, boundh)
        
        
              
   
     
        
        pg.draw.rect(screen, (225, 101,37), displayBox, SIZE)
        highlightPoints(foundPoints)
        qt.draw(screen,radius)
        pg.display.update
        pg.display.flip()
        pg.time.delay(1) 
      

