import pygame, model

# screen = pygame.display.set_mode([1000, 600], )
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
a = pygame.image.load('images/space_gun1.png')
a = pygame.transform.flip(a, True, False)


def rect(screen):
    global a
    screen.fill([0,0,0])
    pygame.draw.rect(screen, [255, 255, 255], [25, 25, screen.get_width() - 50, screen.get_height() - 50])
    b = model.m + 3
    h = (screen.get_height() - 60) / b
    for j in range(b):
        pygame.draw.rect(screen, [0, 255,0],[30,j*h+30, screen.get_width() - 60, h], 1)
        a = pygame.transform.scale(a, [(h-2)*1.2, h-2] )
        screen.blit(a,[31,j*h+30])
    print(model.m)





def draw():
    pygame.display.flip()
    screen.blit(a, [10, 10])
    rect(screen)
