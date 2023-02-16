import pygame

screen=pygame.display.get_surface()
m=0
r=[]
number=None


k=pygame.Rect([25, 25, screen.get_width() - 50, screen.get_height() - 50])
def black_jack(u):
    global number
    for g in r:
        if g.collidepoint(u):
            number =r.index(g)


def rect():
    global r,b,h,l
    r.clear()
    b =m + 3
    l=b
    h =(screen.get_height() - 60) / b
    for j in range(b):
        r.append(pygame.Rect([30, j * h + 30, screen.get_width() - 60, h]))
    print(r)
rect()


