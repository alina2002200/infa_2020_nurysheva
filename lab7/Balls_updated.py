import pygame
import pygame.draw
from random import randint
pygame.init()
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 30)
FPS = 70
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
    

class Target:
    '''
    class creates initial state of the object
    and functions to move check_border and check collision
    (move, check_border(width, length),
     collision(coords, r_1, r_2, figure_1, figure_2))
    '''
    def __init__(self, screen, width, length):
        '''
        creates initial state
        width: type int
        length: type int
        '''
        self.x = randint(100, width)
        self.y = randint(100, length)
        self.screen = screen
        self.v_x = randint(-3, 3)
        self.v_y = randint(-3, 3)
        self.rect = (self.x, self.y)
        self.score = randint(1, 5)
        
    
    def move(self):
        '''
        creates motion of the object on one step
        '''
        self.x += self.v_x
        self.y += self.v_y
        self.rect = (self.x, self.y)
        
        
    def check_border(self, width, length):
        '''
        checks if border can be crossed
        width: type int
        length: type int
        '''
        if self.x + self.v_x <= 0 or self.x + self.v_x >= width:
            self.v_x = -self.v_x
        if self.y + self.v_y <= 0 or  self.y + self.v_y >= length:
            self.v_y = -self.v_y
            
            
    def collision(self, coords, r_1, r_2, figure_1, figure_2):
        '''
        checkes collision of the figures
        cords: type list
        r_1: type int
        r_2: type int
        figure_1: type float 
        figure_2: type float
        (figure_1 and figure_2 differ
        while pictures or squares 1.43 balls 1)
        '''
        x_b, y_b = coords
        rho_1 = (self.x + r_1/2.0 - x_b - r_2/2.0)**2
        rho_2 = (self.y + r_1/2.0  - y_b - r_2/2.0)**2
        rho_3 = (r_1*figure_1/2.0 + r_2*figure_2/2.0)**2
        condition = rho_1 + rho_2 <= rho_3
        if condition:
            self.v_x = -self.v_x
            self.v_y = -self.v_y
            

# class that consists of functions for creating our objects
class Pictures(Target):
    '''
    creates picture objects and consists of functions
    draw, check_event(coords) that do the same as they 
    named
    '''
    def __init__(self, screen, width, length):
        '''
        creates our picture objects on screen
        width: type int
        length: type int
        '''
        super().__init__(screen, width, length)
        # we give different number of points for dif. pictures
        if randint(0, 1):
            self.image = pygame.image.load('shrek5.png')
            self.score = 2
        else:
            self.image = pygame.image.load('shrek6.png')
            self.score = 10 
        self.rect = self.image.get_rect()
        self.scal = randint(30, 50)
        self.image = pygame.transform.scale(self.image, (self.scal, self.scal))
        
        
    def draw(self):
        '''
        draws picture with cordinates
        that are in self.rect on left higher corner
        '''
        screen.blit(self.image, self.rect)
    
    
    def check_event(self, coords):
        '''
        coords in type list
        determines if we hit the object
        '''
        x_m, y_m = coords
        if x_m >= self.x and x_m <= self.x + self.scal:
            condition_x = True
        else:
            condition_x = False
        if self.y <= y_m and self.y + self.scal >= y_m:
            condition_y = True
        else:
            condition_y = False
        if  condition_x and condition_y:
            return True
        else:
            return False

            
class Ball(Target):
    '''
    class that creates balls and consists of functions
    draw, check_event(coords), first draws, second finds 
    if the ball was buttoned
    '''
    def __init__(self, screen, width, length):
        '''
        creates our ball objects on screen
        width: type int
        length: type int
        '''        
        super().__init__(screen, width, length)
        self.r = randint(10, 40)
        self.color = COLORS[randint(0, 5)]
        
        
    def draw(self):
        '''
        draws ball(ellipse) with cordinates
        that are in self.x and self.y from left higher corner
        '''    
        elps = pygame.draw.ellipse(self.screen, self.color, 
                                   (self.x, self.y, self.r, self.r))

        
    def check_event(self, coords):
        '''
        coords in type list
        determines if we hit the object
        '''
        x_m, y_m = coords
        if (self.x - x_m)**2 + (self.y - y_m)**2 <= self.r**2:
            return True
        else:
            return False


class Square(Target):
    def __init__(self, screen, width, length):
        '''
        creates our square objects on screen
        width: type int
        length: type int
        '''     
        super().__init__(screen, width, length)
        self.r = randint(10, 30)
        self.color = COLORS[randint(0, 5)]
        
        
    def draw(self):
        '''
        draws square(rectangle) with cordinates
        that are in self.x and self.y from left higher corner
        '''        
        rectangle = pygame.draw.rect(self.screen, self.color, [self.x, 
                                     self.y, self.r, self.r])
    
    
    def check_event(self, coords):
        '''
        coords in type list
        determines if we hit the object
        '''    
        x_m, y_m = coords
        if (self.x - x_m)**2 + (self.y - y_m)**2 <= self.r**2:
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


def table():
    '''
    prints table of the players on the screen
    '''
    file = open('out.txt', 'r')
    k = 0
    for line in file:
        text1 = font1.render(line + " ", True, BLACK)
        screen.blit(text1, (100, 200 + k))
        k += 20
    file.close()
    
    
clock = pygame.time.Clock()
finished = False
Score =  0 
# creates our objects
balls = [Ball(screen, width, length) for i in range(10)] 
squares = [Square(screen, width, length) for i in range(10)]
pictures = [Pictures(screen, width, length) for i in range(10)]
# creates every step of drawing, checks conditions
while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)  
    for ball in balls:
        ball.check_border(width, length) 
        for j in balls:
            if ball != j:
                ball.collision((j.x, j.y), ball.r, j.r, 1, 1)
        for j in squares:
            ball.collision((j.x, j.y), ball.r, j.r, 1, 1.43)
        for j in pictures:
            ball.collision((j.x, j.y), ball.r, j.scal, 1, 1.43)                
        ball.move()
        ball.draw()
    for square in squares:
        square.check_border(width, length) 
        for j in squares:
            if square != j:
               square.collision((j.x, j.y), square.r, j.r, 1.43, 1.43)
        for j in pictures:
            square.collision((j.x, j.y), square.r, j.scal, 1.43, 1.43)                     
        square.move()
        square.draw()
    for picture in pictures:
        picture.check_border(width, length) 
        for j in pictures:
            if picture != j:
               picture.collision((j.x, j.y), picture.scal, j.scal, 1.43, 1.43)
        picture.move()
        picture.draw()
    table()
    score(Score)                        
    pygame.display.flip()
    # score giving and creating objects on place of a hitted
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                if ball.check_event(event.pos):
                    Score += ball.score
                    balls.pop(i)
                    balls.append(Ball(screen, width, length))
            for i, square in enumerate(squares):
                if square.check_event(event.pos):
                    Score += square.score
                    squares.pop(i)
                    squares.append(Square(screen, width, length))  
            for i, picture in enumerate(pictures):
                if picture.check_event(event.pos):
                    Score += picture.score
                    pictures.pop(i)
                    pictures.append(Pictures(screen, width, length))                    
# writing number of points of a players in file                       
file1 = open('out.txt', 'a')
file1.write('Name: ' + name + ':   ' + str(Score) + '\n')  
file1.close()
pygame.quit()
  