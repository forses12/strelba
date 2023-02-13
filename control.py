import pygame,model
# pygame.key.set_repeat(10)

def pain():
    z=pygame.event.get()
    for u in z:
        if u.type==pygame.QUIT:
            exit()
        if u.type==pygame.KEYDOWN and u.key==pygame.K_SPACE:
            model.m+=1
            model.rect()
        if u.type==pygame.MOUSEBUTTONDOWN and u.button==pygame.BUTTON_LEFT and model.k.collidepoint(u.pos):
            print(u.pos)
        if u.type == pygame.MOUSEBUTTONDOWN and u.button == pygame.BUTTON_LEFT and model.r.collidepoint(u.pos):
            model.k=True
            print(model.j)


