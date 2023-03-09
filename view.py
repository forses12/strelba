import pygame,random

screen = pygame.display.set_mode([1000, 600], )
# screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
import model

m=[]

def app_images():
    for a in range(1,9):
        s=pygame.image.load('images/space_gun' + str(a) + '.png')
        s=pygame.transform.flip(s, True, False)
        m.append(s)

app_images()
def rect(screen):
    global a
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen, [255, 255, 255], model.k)
    for j in model.gun:
        if j is model.number:
            pygame.draw.rect(screen, [40,255, 0],j['rect'],5)
        else:
            pygame.draw.rect(screen, [255, 33, 0],j['rect'],1)
        a = m[j['name']]
        g=pygame.transform.scale(a,[(screen.get_width()-50)/5,a.get_height()/a.get_width()*((screen.get_width()-50)/5)])
        f=pygame.transform.scale(a,[(model.h-2)*a.get_width()/a.get_height(),model.h-2])

        if g.get_width()<f.get_width():
            screen.blit(g,j['rect'])
        else:
            screen.blit(f,j['rect'])
        pygame.draw.ellipse(screen,[0,0,0],[600,j['rect'].h/2+j['rect'].y,25,15],100)








def draw():
    pygame.display.flip()
    # screen.blit(a, [10, 10])
    rect(screen)
