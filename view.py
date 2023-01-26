import pygame, model

# screen = pygame.display.set_mode([1000, 600], )
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
a = pygame.image.load('images/space_gun1.png')
a = pygame.transform.scale(a, [113, 89], )
a = pygame.transform.flip(a, True, False)
h = (screen.get_height() - 60) / 3



def rect(screen):
    pygame.draw.rect(screen, [255, 255, 255], [25, 25, screen.get_width() - 50, screen.get_height() - 50])
    pygame.draw.rect(screen, [0, 255, 0], [30, 30, screen.get_width() - 60, h], 1)
    pygame.draw.rect(screen, [255, 0, 0], [30, 30 + h, screen.get_width() - 60, h], 1)
    pygame.draw.rect(screen, [0, 0, 255], [30, 30 + h * 2, screen.get_width() - 60, h], 1)
    print(model.m)





def draw():
    pygame.display.flip()
    screen.blit(a, [10, 10])
    rect(screen)
