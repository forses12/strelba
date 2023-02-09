import pygame

screen = pygame.display.set_mode([1000, 600], )
# screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
import model
a = pygame.image.load('images/space_gun1.png')
a = pygame.transform.flip(a, True, False)



def rect(screen):
    global a
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen, [255, 255, 255], model.k)

    for j in range(model.b):

        pygame.draw.rect(screen, [255, 33, 0], model.r[j],1)
        a = pygame.transform.scale(a, [(model.h - 2) * 1.2, model.h - 2])
        screen.blit(a, [31, j * model.h + 30])




def draw():
    pygame.display.flip()
    screen.blit(a, [10, 10])
    rect(screen)
