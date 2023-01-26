import pygame,model

def pain():
    z=pygame.event.get()
    for u in z:
        if u.type==pygame.QUIT:
            exit()
        if u.type==pygame.KEYDOWN and u.key==pygame.K_SPACE:
            model.j=True

