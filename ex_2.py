from random import *
import turtle 
import numpy as np
import pygame
from pygame.draw import *


pygame.init()
FPS = 0.5
clock = pygame.time.Clock()
display = pygame.display.set_mode((500, 800))


def sky(n):
    rect(display, (138, 43, 226, 255), (0, 0, 500, 80))
    rect(display, (0, 0, 139, 255), (0, 80, 500, 80))
    rect(display, (238, 154, 0, 255), (0, 160, 500, 80))
    rect(display, (255, 181, 197, 255), (0, 240, 500, 80))
    rect(display, (142, 229, 238, 255), (0, 320, 500, 480))
    
    
def bird(x_step, y_step, scale_x, scale_y, width_of_line):
    arc(display, (255, 255, 255, 255), [100 + x_step, 40 + y_step, scale_x, scale_y], 0, 3.14, width_of_line)
    arc(display, (255, 255, 255, 255), [100 + scale_x + x_step, 40 + y_step, scale_x, scale_y], 0, 3.14, width_of_line)

   
def all_birds(n):
    bird(0, 0, 70, 50, 3)  
    bird(150, 80, 70, 50, 3) 
    bird(90, 210, 70, 50, 3)
    bird(200, 50, 30, 25, 1)
    bird(220, 30, 30, 25, 1)
    bird(180, 10, 30, 25, 1)
    bird(160, 125, 30, 25, 1)
    bird(210, 145, 30, 25, 1)
    bird(180, 165, 30, 25, 1)
    bird(230, 185, 30, 25, 1)
    bird(90, 140, 30, 25, 1)
    bird(70, 170, 30, 25, 1)
    bird(110, 187, 30, 25, 1)
    bird(285, 145, 35, 30, 2)
    bird(320, 170, 33, 30, 2)
    bird(295, 200, 33, 30, 2)
 
 
def gull(scale, step_x, step_y, width_of_line, eye_radius):
    polygon(display, (255, 0, 0), [(13*scale + step_x, 28*scale + step_y), (12*scale + step_x, 29*scale + step_y), 
                                   (13*scale + step_x, 28.5*scale + step_y), (14*scale + step_x, 29*scale + step_y), 
                                   (13.5*scale + step_x, 28.3*scale + step_y), (14.5*scale + step_x, 29*scale + step_y), 
                                   (14*scale + step_x, 28.3*scale + step_y), (15*scale + step_x, 28*scale + step_y)])
    polygon(display, (255, 100, 100), [(13*scale + step_x, 28*scale + step_y), (12*scale + step_x, 29*scale + step_y), 
                                       (13*scale + step_x, 28.5*scale + step_y), (14*scale + step_x, 29*scale + step_y), 
                                       (13.5*scale + step_x, 28.3*scale + step_y), (14.5*scale + step_x, 29*scale + step_y), 
                                       (14*scale + step_x, 28.3*scale + step_y), (15*scale + step_x, 28*scale + step_y)], width_of_line)                                   
    polygon(display, (255, 0, 0), [(12*scale + step_x, 29*scale + step_y), (11*scale + step_x, 30*scale + step_y), 
                                   (12*scale + step_x, 29.5*scale + step_y), (13*scale + step_x, 30*scale + step_y), 
                                   (12.5*scale + step_x, 29.3*scale + step_y), (13.5*scale + step_x, 30*scale + step_y), 
                                   (13*scale + step_x, 29.3*scale + step_y), (14*scale + step_x, 29*scale + step_y)])  
    polygon(display, (255, 100, 100), [(12*scale + step_x, 29*scale + step_y), (11*scale + step_x, 30*scale + step_y), 
                                       (12*scale + step_x, 29.5*scale + step_y), (13*scale + step_x, 30*scale + step_y), 
                                       (12.5*scale + step_x, 29.3*scale + step_y), (13.5*scale + step_x, 30*scale + step_y), 
                                       (13*scale + step_x, 29.3*scale + step_y), (14*scale + step_x, 29*scale + step_y)], width_of_line)                                       
    polygon(display, (255, 255, 255, 255), [(7*scale + step_x, 25*scale + step_y), (4*scale + step_x, 26*scale + step_y), 
                                            (3*scale + step_x, 23*scale + step_y), (4*scale + step_x, 22*scale + step_y), 
                                            (7*scale + step_x, 23*scale + step_y), (6*scale + step_x, 22*scale + step_y), 
                                            (6*scale + step_x, 21*scale + step_y), (3*scale + step_x, 20*scale + step_y), 
                                            (1*scale + step_x, 18*scale + step_y), (3*scale + step_x, 19*scale + step_y), 
                                            (7*scale + step_x, 19*scale + step_y), (9*scale + step_x, 22*scale + step_y), 
                                            (7*scale + step_x, 19*scale + step_y), (5*scale + step_x, 18*scale + step_y), 
                                            (3*scale + step_x, 16*scale + step_y), (5*scale + step_x, 17*scale + step_y), 
                                            (9*scale + step_x, 18*scale + step_y), (10*scale + step_x, 22*scale + step_y), 
                                            (12*scale + step_x, 23*scale + step_y), (14*scale + step_x, 23*scale + step_y),
                                            (14*scale + step_x, 24*scale + step_y), (13*scale + step_x, 25*scale + step_y)])                               
    polygon(display, (0, 0, 0, 0), [(7*scale + step_x, 25*scale + step_y), (4*scale + step_x, 26*scale + step_y), 
                                    (3*scale + step_x, 23*scale + step_y), (4*scale + step_x, 22*scale + step_y), 
                                    (7*scale + step_x, 23*scale + step_y), (6*scale + step_x, 22*scale + step_y), 
                                    (6*scale + step_x, 21*scale + step_y), (3*scale + step_x, 20*scale + step_y), 
                                    (1*scale + step_x, 18*scale + step_y), (3*scale + step_x, 19*scale + step_y), 
                                    (7*scale + step_x, 19*scale + step_y), (9*scale + step_x, 22*scale + step_y), 
                                    (7*scale + step_x, 19*scale + step_y), (5*scale + step_x, 18*scale + step_y), 
                                    (3*scale + step_x, 16*scale + step_y), (5*scale + step_x, 17*scale + step_y), 
                                    (9*scale + step_x, 18*scale + step_y), (10*scale + step_x, 22*scale + step_y), 
                                    (12*scale + step_x, 23*scale + step_y), (14*scale + step_x, 23*scale + step_y),
                                    (14*scale + step_x, 24*scale + step_y), (13*scale + step_x, 25*scale + step_y)], width_of_line) 
    ellipse(display, (255, 255, 255, 255), (7*scale + step_x, 24*scale + step_y, 6*scale, 2*scale))
    arc(display, (0, 0, 0, 0), (7*scale + step_x, 24*scale + step_y, 6*scale, 2*scale), 3.14, 6.28, width_of_line)
    ellipse(display, (255, 255, 255, 255), (13*scale + step_x, 22*scale + step_y, 4*scale, 2*scale))
    arc(display, (0, 0, 0, 0), (13*scale + step_x, 22*scale + step_y, 4*scale, 2*scale), -2.1, 3.14, width_of_line)
    polygon(display, (255, 255, 255, 255), [(9*scale + step_x, 26*scale + step_y), (9*scale + step_x, 27*scale + step_y), 
                                            (10*scale + step_x, 29*scale + step_y), (13*scale + step_x, 29*scale + step_y), 
                                            (10*scale + step_x, 28*scale + step_y), (10*scale + step_x, 27*scale + step_y), 
                                            (12*scale + step_x, 28*scale + step_y), (14*scale + step_x, 28*scale + step_y), 
                                            (11*scale + step_x, 27*scale + step_y), (11*scale + step_x, 26*scale + step_y)])
    polygon(display, (0, 0, 0, 0), [(9*scale + step_x, 26*scale + step_y), (9*scale + step_x, 27*scale + step_y), 
                                    (10*scale + step_x, 29*scale + step_y), (13*scale + step_x, 29*scale + step_y), 
                                    (10*scale + step_x, 28*scale + step_y), (10*scale + step_x, 27*scale + step_y), 
                                    (12*scale + step_x, 28*scale + step_y), (14*scale + step_x, 28*scale + step_y), 
                                    (11*scale + step_x, 27*scale + step_y), (11*scale + step_x, 26*scale + step_y)], width_of_line)
    polygon(display, (255, 255, 255, 255),[(9*scale + step_x, 26.2*scale + step_y), (11*scale + step_x, 26.2*scale + step_y), 
                                           (11*scale + step_x, 25.9*scale + step_y), (9*scale + step_x, 25.9*scale + step_y),
                                           (10*scale + step_x, 25.9*scale + step_y)])
    circle(display, (0, 0, 0, 0), (16*scale + step_x, 23*scale + step_y), eye_radius)
    polygon(display, (255, 100, 100), [(17*scale + step_x, 22.9*scale + step_y), (19*scale + step_x, 22.3*scale + step_y), 
                                       (19.5*scale + step_x, 23*scale + step_y), (19*scale + step_x, 23.7*scale + step_y),
                                       (17*scale + step_x, 23.1*scale + step_y)])
    polygon(display, (255, 0, 0), [(17*scale + step_x, 22.9*scale + step_y), (19*scale + step_x, 22.3*scale + step_y), 
                                       (19.5*scale + step_x, 23*scale + step_y), (19*scale + step_x, 23.7*scale + step_y),
                                       (17*scale + step_x, 23.1*scale + step_y)], width_of_line)
    line(display, (255, 0, 0), (17*scale + step_x, 23*scale + step_y), (19.5*scale + step_x, 23*scale + step_y))                                   

    
def gull_mirrored(scale, step_x, step_y, width_of_line, eye_radius):
    polygon(display, (255, 0, 0), [(500 - 13*scale + step_x, 28*scale + step_y), (500 - 12*scale + step_x, 29*scale + step_y), 
                                   (500 - 13*scale + step_x, 28.5*scale + step_y), (500 - 14*scale + step_x, 29*scale + step_y), 
                                   (500 - 13.5*scale + step_x, 28.3*scale + step_y), (500 - 14.5*scale + step_x, 29*scale + step_y), 
                                   (500 - 14*scale + step_x, 28.3*scale + step_y), (500 - 15*scale + step_x, 28*scale + step_y)])
    polygon(display, (255, 100, 100), [(500 - 13*scale + step_x, 28*scale + step_y), (500 - 12*scale + step_x, 29*scale + step_y), 
                                       (500 - 13*scale + step_x, 28.5*scale + step_y), (500 - 14*scale + step_x, 29*scale + step_y), 
                                       (500 - 13.5*scale + step_x, 28.3*scale + step_y), (500 - 14.5*scale + step_x, 29*scale + step_y), 
                                       (500 - 14*scale + step_x, 28.3*scale + step_y), (500 - 15*scale + step_x, 28*scale + step_y)], width_of_line)                                   
    polygon(display, (255, 0, 0), [(500 - 12*scale + step_x, 29*scale + step_y), (500 - 11*scale + step_x, 30*scale + step_y), 
                                   (500 - 12*scale + step_x, 29.5*scale + step_y), (500 - 13*scale + step_x, 30*scale + step_y), 
                                   (500 - 12.5*scale + step_x, 29.3*scale + step_y), (500 - 13.5*scale + step_x, 30*scale + step_y), 
                                   (500 - 13*scale + step_x, 29.3*scale + step_y), (500 - 14*scale + step_x, 29*scale + step_y)])  
    polygon(display, (255, 100, 100), [(500 - 12*scale + step_x, 29*scale + step_y), (500 - 11*scale + step_x, 30*scale + step_y), 
                                       (500 - 12*scale + step_x, 29.5*scale + step_y), (500 - 13*scale + step_x, 30*scale + step_y), 
                                       (500 - 12.5*scale + step_x, 29.3*scale + step_y), (500 - 13.5*scale + step_x, 30*scale + step_y), 
                                       (500 - 13*scale + step_x, 29.3*scale + step_y), (500 - 14*scale + step_x, 29*scale + step_y)], width_of_line)    
    polygon(display, (255, 255, 255, 255), [(500 - 7*scale + step_x, 25*scale + step_y), (500 - 4*scale + step_x, 26*scale + step_y), 
                                            (500 - 3*scale + step_x, 23*scale + step_y), (500 - 4*scale + step_x, 22*scale + step_y), 
                                            (500 - 7*scale + step_x, 23*scale + step_y), (500 - 6*scale + step_x, 22*scale + step_y), 
                                            (500 - 6*scale + step_x, 21*scale + step_y), (500 - 3*scale + step_x, 20*scale + step_y), 
                                            (500 - 1*scale + step_x, 18*scale + step_y), (500 - 3*scale + step_x, 19*scale + step_y), 
                                            (500 - 7*scale + step_x, 19*scale + step_y), (500 - 9*scale + step_x, 22*scale + step_y), 
                                            (500 - 7*scale + step_x, 19*scale + step_y), (500 - 5*scale + step_x, 18*scale + step_y), 
                                            (500 - 3*scale + step_x, 16*scale + step_y), (500 - 5*scale + step_x, 17*scale + step_y), 
                                            (500 - 9*scale + step_x, 18*scale + step_y), (500 - 10*scale + step_x, 22*scale + step_y), 
                                            (500 - 12*scale + step_x, 23*scale + step_y), (500 - 14*scale + step_x, 23*scale + step_y),
                                            (500 - 14*scale + step_x, 24*scale + step_y), (500 - 13*scale + step_x, 25*scale + step_y)])                                      
    polygon(display, (0, 0, 0, 0), [(500 - 7*scale + step_x, 25*scale + step_y), (500 - 4*scale + step_x, 26*scale + step_y), 
                                    (500 - 3*scale + step_x, 23*scale + step_y), (500 - 4*scale + step_x, 22*scale + step_y), 
                                    (500 - 7*scale + step_x, 23*scale + step_y), (500 - 6*scale + step_x, 22*scale + step_y), 
                                    (500 - 6*scale + step_x, 21*scale + step_y), (500 - 3*scale + step_x, 20*scale + step_y), 
                                    (500 - 1*scale + step_x, 18*scale + step_y), (500 - 3*scale + step_x, 19*scale + step_y), 
                                    (500 - 7*scale + step_x, 19*scale + step_y), (500 - 9*scale + step_x, 22*scale + step_y), 
                                    (500 - 7*scale + step_x, 19*scale + step_y), (500 - 5*scale + step_x, 18*scale + step_y), 
                                    (500 - 3*scale + step_x, 16*scale + step_y), (500 - 5*scale + step_x, 17*scale + step_y), 
                                    (500 - 9*scale + step_x, 18*scale + step_y), (500 - 10*scale + step_x, 22*scale + step_y), 
                                    (500 - 12*scale + step_x, 23*scale + step_y), (500 - 14*scale + step_x, 23*scale + step_y),
                                    (500 - 14*scale + step_x, 24*scale + step_y), (500 - 13*scale + step_x, 25*scale + step_y)], width_of_line)   
    ellipse(display, (255, 255, 255, 255), (500 - 7*scale + step_x - 6*scale, 24*scale + step_y, 6*scale, 2*scale))
    arc(display, (0, 0, 0, 0), (500 - 7*scale + step_x - 6*scale, 24*scale + step_y, 6*scale, 2*scale), 3.14, 6.28, width_of_line)
    ellipse(display, (255, 255, 255, 255), (500 - 13*scale + step_x - 4*scale, 22*scale + step_y, 4*scale, 2*scale))
    arc(display, (0, 0, 0, 0), (500 - 13*scale + step_x - 4*scale, 22*scale + step_y, 4*scale, 2*scale), 0, 5.3, width_of_line) 
    polygon(display, (255, 255, 255, 255), [(500 - 9*scale + step_x, 26*scale + step_y), (500 - 9*scale + step_x, 27*scale + step_y), 
                                            (500 - 10*scale + step_x, 29*scale + step_y), (500 - 13*scale + step_x, 29*scale + step_y), 
                                            (500 - 10*scale + step_x, 28*scale + step_y), (500 - 10*scale + step_x, 27*scale + step_y), 
                                            (500 - 12*scale + step_x, 28*scale + step_y), (500 - 14*scale + step_x, 28*scale + step_y), 
                                            (500 - 11*scale + step_x, 27*scale + step_y), (500 - 11*scale + step_x, 26*scale + step_y)])    
    polygon(display, (0, 0, 0, 0), [(500 - 9*scale + step_x, 26*scale + step_y), (500 - 9*scale + step_x, 27*scale + step_y), 
                                    (500 - 10*scale + step_x, 29*scale + step_y), (500 - 13*scale + step_x, 29*scale + step_y), 
                                    (500 - 10*scale + step_x, 28*scale + step_y), (500 - 10*scale + step_x, 27*scale + step_y), 
                                    (500 - 12*scale + step_x, 28*scale + step_y), (500 - 14*scale + step_x, 28*scale + step_y), 
                                    (500 - 11*scale + step_x, 27*scale + step_y), (500 - 11*scale + step_x, 26*scale + step_y)], width_of_line)
    polygon(display, (255, 255, 255, 255),[(500 - 9*scale + step_x, 26.2*scale + step_y), (500 - 11*scale + step_x, 26.2*scale + step_y), 
                                           (500 - 11*scale + step_x, 25.9*scale + step_y), (500 - 9*scale + step_x, 25.9*scale + step_y),
                                           (500 - 10*scale + step_x, 25.9*scale + step_y)])
    circle(display, (0, 0, 0, 0), (500 - 16*scale + step_x, 23*scale + step_y), eye_radius)   
    polygon(display, (255, 100, 100), [(500 - 17*scale + step_x, 22.9*scale + step_y), (500 - 19*scale + step_x, 22.3*scale + step_y), 
                                       (500 - 19.5*scale + step_x, 23*scale + step_y), (500 - 19*scale + step_x, 23.7*scale + step_y),
                                       (500 - 17*scale + step_x, 23.1*scale + step_y)])
    polygon(display, (255, 0, 0), [(500 - 17*scale + step_x, 22.9*scale + step_y), (500 - 19*scale + step_x, 22.3*scale + step_y), 
                                       (500 - 19.5*scale + step_x, 23*scale + step_y), (500 - 19*scale + step_x, 23.7*scale + step_y),
                                       (500 - 17*scale + step_x, 23.1*scale + step_y)], width_of_line)
    line(display, (255, 0, 0), (500 - 17*scale + step_x, 23*scale + step_y), (500 - 19.5*scale + step_x, 23*scale + step_y))  
 

def fish(scale, step_x, step_y, width_of_line, eye_radius, pupil_radius):
    ellipse(display, (0, 240, 100), (3*scale + step_x, 28*scale + step_y, 4*scale, 2*scale))
    ellipse(display, (0, 100, 0), (3*scale + step_x, 28*scale + step_y, 4*scale, 2*scale), width_of_line)
    polygon(display, (100, 0, 100), [(1*scale + step_x, 28*scale + step_y), (1.5*scale + step_x, 29*scale + step_y), 
                                     (1*scale + step_x, 30*scale + step_y), (3*scale + step_x, 29*scale + step_y)])
    polygon(display, (100, 0, 0), [(1*scale + step_x, 28*scale + step_y), (1.5*scale + step_x, 29*scale + step_y), 
                                   (1*scale + step_x, 30*scale + step_y), (3*scale + step_x, 29*scale + step_y)], width_of_line)
    polygon(display, (100, 0, 100), ((5*scale + step_x, 28*scale + step_y), (5*scale + step_x, 27*scale + step_y), 
                                     (3*scale + step_x, 27*scale + step_y), (4*scale + step_x, 28*scale + step_y)))                               
    polygon(display, (100, 0, 0), ((5*scale + step_x, 28*scale + step_y), (5*scale + step_x, 27*scale + step_y), 
                                   (3*scale + step_x, 27*scale + step_y), (4*scale + step_x, 28*scale + step_y)), width_of_line)                                    
    ellipse(display, (100, 0, 100), (4.5*scale + step_x, 27*scale + step_y, 1*scale, 1*scale))  
    arc(display, (100, 0, 0), (4.5*scale + step_x, 27*scale + step_y, 1*scale, 1*scale), -1.57, 1.57, width_of_line)
    polygon(display, (100, 0, 100), [(5*scale + step_x, 30*scale + step_y), (6*scale + step_x, 30*scale + step_y),
                                     (6*scale + step_x, 31*scale + step_y)])
    polygon(display, (100, 0, 0), [(5*scale + step_x, 30*scale + step_y), (6*scale + step_x, 30*scale + step_y), 
                                   (6*scale + step_x, 31*scale + step_y)], width_of_line)
    polygon(display, (100, 0, 100), [(3*scale + step_x, 30*scale + step_y), (4*scale + step_x, 29.8*scale + step_y), 
                                     (3.8*scale + step_x, 30.6*scale + step_y), (3*scale + step_x, 31*scale + step_y)])   
    polygon(display, (100, 0, 0), [(3*scale + step_x, 30*scale + step_y), (4*scale + step_x, 29.8*scale + step_y), 
                                   (3.8*scale + step_x, 30.6*scale + step_y), (3*scale + step_x, 31*scale + step_y)], width_of_line)  
    circle(display, (0, 0, 240), (6*scale + step_x, 29*scale + step_y), eye_radius)  
    circle(display, (0, 0, 0), (6*scale + step_x, 29*scale + step_y), pupil_radius) 
    ellipse(display, (255, 255, 255), (5.7*scale + step_x, 28.7*scale + step_y, pupil_radius*0.7, pupil_radius*0.5))
    
    
sky(1) 
all_birds(1)
fish(25, 0, 0, 2, 10, 6)
fish(20, 350, 90, 2, 10, 6)
fish(10, 270, 230, 2, 4, 2)
gull(25, 0, 0, 2, 6)
gull(5, 200, 300, 1, 1)
gull_mirrored(10, 0, 200, 1, 3)
pygame.display.update()
clock.tick(FPS)