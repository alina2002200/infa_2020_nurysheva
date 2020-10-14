from random import *
import turtle 
import numpy as np
import pygame
from pygame.draw import *

pygame.init()
FPS = 0.1
clock = pygame.time.Clock()
display = pygame.display.set_mode( (800, 800) )
pygame.draw.circle(display, (255,255,0), (400, 400), 200)
pygame.draw.circle(display, (255,0,0), (470, 330), 30 )
pygame.draw.circle(display, (0,0,0), (470, 330), 15 )
pygame.draw.circle(display, (255,0,0), (330, 330), 40)
pygame.draw.circle(display, (0,0,0), (330, 330), 15)
pygame.draw.polygon(display, (0,0,0), ((280, 270), (315, 275), (360, 300), (355, 305)))
pygame.draw.polygon(display, (0,0,0), ((440, 300), (450, 305), (515, 285), (510, 280)))
pygame.draw.rect(display,(0,0,0), (300, 470, 200, 30))
pygame.display.update()
clock.tick(FPS)