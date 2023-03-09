import pygame,random

screen=pygame.display.get_surface()
m=0

number=None
number_gun=[]
gun=[]


k=pygame.Rect([25, 25, screen.get_width() - 50, screen.get_height() - 50])
def black_jack(u):
    global number
    for g in gun:
        if g['rect'].collidepoint(u):
            number =g


def guns():
    gun1={'name':random.randint(0,7),
          'rect':None}
    gun.append(gun1)
guns()



def rect():
    global h
    b =len(gun)
    h =(screen.get_height() - 60) /b
    for j in range(b):
        v=pygame.Rect([30, j * h + 30, screen.get_width() - 60, h])
        gun[j]['rect']=v
    print(number_gun)
rect()













































































































































































































































print(gun)
