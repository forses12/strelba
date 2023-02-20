import pygame

# screen = pygame.display.set_mode([1000, 600], )
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
import model
a = pygame.image.load('images/space_gun6.png')
a = pygame.transform.flip(a, True, False)
a=pygame.transform.scale(a,[a.get_width()/2,a.get_height()/2])



def rect(screen):
    global a
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen, [255, 255, 255], model.k)

    for j in range(model.b):
        if j==model.number:
            pygame.draw.rect(screen, [40,255, 0], model.r[j],5)
        else:
            pygame.draw.rect(screen, [255, 33, 0], model.r[j],1)

        g=pygame.transform.scale(a,[(screen.get_width()-50)/5,a.get_height()/a.get_width()*((screen.get_width()-50)/5)])
        f=pygame.transform.scale(a,[(model.h-2)*a.get_width()/a.get_height(),model.h-2])
        if g.get_width()<f.get_width():
            screen.blit(g, [31, j * model.h + 30])
        else:
            screen.blit(f, [31, j * model.h + 30])





def draw():
    pygame.display.flip()
    screen.blit(a, [10, 10])
    rect(screen)
