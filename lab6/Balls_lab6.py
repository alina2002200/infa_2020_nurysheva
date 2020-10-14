import pygame
from pygame.draw import *
from random import randint
pygame.init()
font = pygame.font.Font(None, 50)
FPS = 1
screen = pygame.display.set_mode((1200, 900))

# cortege of colors that used in the picture
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(list_coords, list_velocities):
    '''
    draws new ball
    '''
    t = 0.1
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    v_x = randint(0, 30)
    v_y = randint(0, 30)
    list_coords.append(x)
    list_coords.append(y)
    list_coords.append(r)
    list_velocities.append(v_x)
    list_velocities.append(v_y)
    color = COLORS[randint(0, 5)]
    while pygame.MOUSEMOTION:
        x = x + v_x*t
        y = y + v_y*t
        circle(screen, color, (x, y), r)
    
    
    
def score(Score):
    '''
    Score - score of the person who pushes the mousebotton
    in type int
    '''
    text = font.render("Score: " + str(Score), True, BLUE)
    screen.blit(text, (100, 100))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
Score =  0    
list_of_coords = []
list_of_velocities = []
while not finished:
    new_ball(list_of_coords, list_of_velocities)
    score(Score)
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if ((list_of_coords[0] - x)**2 + (list_of_coords[1] - y)**2) <= list_of_coords[2]**2:
                Score += 1
                
    list_of_coords = []
    list_of_velocities = []

pygame.quit()


