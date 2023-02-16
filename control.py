import pygame,model
# pygame.key.set_repeat(10)

def pain():
    z=pygame.event.get()
    for u in z:
        if u.type==pygame.QUIT:
            exit()
        if u.type==pygame.KEYDOWN and u.key==pygame.K_SPACE:
            if model.m<=4:
                model.m+=1
            model.rect()
        if u.type==pygame.MOUSEBUTTONDOWN and u.button==pygame.BUTTON_LEFT and model.k.collidepoint(u.pos):
            model.black_jack(u.pos)




