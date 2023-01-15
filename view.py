import pygame

screen=pygame.display.set_mode([1000,600],)
a=pygame.image.load('images/space_gun1.png')
a=pygame.transform.scale(a,[113,89],)
a=pygame.transform.flip(a,True,False)
def draw():
    pygame.display.flip()
    screen.blit(a,[10,10])