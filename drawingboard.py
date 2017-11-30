import pygame
import numpy as np
import HWRecog as hwr
import dataprep as prep

size=84
digitSize=int(size/3)
data = np.zeros( (size, size), dtype=np.uint8 )
digit=np.zeros( (int(size/3), int(size/3)), dtype=np.uint8 )
screen = pygame.display.set_mode((size,size))
begingDrawing = False
last_pos = (0, 0)
color = (255, 255, 0)
radius = 1

def drawline(surf, start, end, color, radius=2):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(surf, color, (x, y), radius)
        data[y][x]=253
        for i in range(1,9):
            if x + i < size:
                for j in range(1,9):
                    if y+j <size:
                        data[y+j][x+i] = 220
try:
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise StopIteration
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, event.pos, radius)
            begingDrawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            begingDrawing = False
        if event.type == pygame.MOUSEMOTION:
            if begingDrawing:
                pygame.draw.circle(screen, color, event.pos, radius)
                drawline(screen, event.pos, last_pos,  color, radius)
            last_pos = event.pos
        pygame.display.flip()
except StopIteration:
#step1: recoganize the handwriting digit by reshaping the array data, and call the function
# digitRecog(digit) to print the output, whiich is the recognized digit.
    digit=data.reshape([digitSize, size//digitSize, digitSize, size//digitSize]).mean(3).mean(1)
#"*** YOUR CODE HERE ***"


pygame.quit()