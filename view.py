import pygame,model

screen=pygame.display.set_mode([1000,600],)
# screen=pygame.display.set_mode([0,0],pygame.FULLSCREEN)
a=pygame.image.load('images/space_gun1.png')
a=pygame.transform.scale(a,[113,89],)
a=pygame.transform.flip(a,True,False)
def rect(screen):
    pygame.draw.rect(screen,[255,255,255],[25,25,950,550])
rect(screen)
def draw():
    pygame.display.flip()
    screen.blit(a,[10,10])