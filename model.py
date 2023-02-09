import pygame

screen=pygame.display.get_surface()
m=0
r=[]
j=''

k=pygame.Rect([25, 25, screen.get_width() - 50, screen.get_height() - 50])
def rect():
    global r,b,h
    b =m + 3
    h =(screen.get_height() - 60) / b
    for j in range(b):
        r.append(pygame.Rect([30, j * h + 30, screen.get_width() - 60, h]))
rect()


