import pygame
import pygame.draw
from random import randint
pygame.init()
font = pygame.font.Font(None, 50)
FPS = 50
width = 1000
length = 500
# creating display
screen = pygame.display.set_mode((width, length))
name = input('Your name: ')
# cortege of colors that used in the picture
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# class that consists of functions for creting our objects
class Balls(pygame.sprite.Sprite):
    def __init__(self):
        '''
        creates our objects, their motion
        and their initial state
        '''
        pygame.sprite.Sprite.__init__(self)
        if randint(0, 1) == 0:
            self.image = pygame.image.load('shrek5.png')
            self.coefficient = 2
        else:
            self.image = pygame.image.load('shrek6.png')
            self.coefficient = 1            
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, width)
        self.rect.y = randint(100, length)
        self.scal = randint(40, 60)
        self.image = pygame.transform.scale(self.image, (self.scal, self.scal))
        self.v_x = randint(-3, 3)
        self.v_y = randint(-3, 3)
    
    
    def update(self):
        '''
        updates coordinates of the objects
        making them push off the walls
        '''
        if self.rect.x + self.v_x <=0 or  self.rect.x + self.v_x >= width - self.scal:
            self.v_x = -self.v_x
        if self.rect.y + self.v_y <=0 or  self.rect.y + self.v_y >= length - self.scal:
            self.v_y = -self.v_y
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        if(randint(1, 40) == 1):
            self.kill
    
    
    def condition_of_being_cought(self, coords):
        '''
        coords in type list
        determines if we hit the object
        '''
        x_m = coords[0]
        y_m = coords[1] 
        if x_m >= self.rect.x and x_m <= self.rect.x + self.scal:
            condition_x = True
        else:
            condition_x = False
        if self.rect.y <= y_m and self.rect.y + self.scal >= y_m:
            condition_y = True
        else:
            condition_y = False
        if  condition_x and condition_y:
            return True
        else:
            return False
    
    
def score(Score):
    '''
    Score - score of the person who pushes the mousebotton
    in type int
    prints score on the picture
    '''
    text = font.render("Score: " + str(Score), True, BLUE)
    screen.blit(text, (100, 100))


clock = pygame.time.Clock()
finished = False
Score =  0 
ball_class = Balls() 
ball = pygame.sprite.Group()
ball.add(ball_class)
ball.update()
pygame.display.flip()
# we create more objects that can disappear
# and we get different number of points for each of them
while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    score(Score)
    ball.update()
    ball.draw(screen)
    pygame.display.flip()
    if randint(1, 60) == 1:
        ball_class = Balls()
        ball.add(ball_class)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in ball:
                if i.condition_of_being_cought(event.pos):
                    if i.coefficient == 2:
                        Score += 1
                    elif i.coefficient == 1: 
                        Score += 5
                    i.kill()
# writing number of points of a players in file                    
file = open("out.txt", "a")
file.write('Name:' + name + ': ' + str(Score) + '\n')
    
pygame.quit()


