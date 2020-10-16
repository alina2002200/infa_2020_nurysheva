import os
import pygame as pg
import random as rnd
import sys
pg.init()
font = pg.font.Font(None, 50)

white = 255, 255, 255
size = width, height = 1000, 600
screen = pg.display.set_mode(size)
screen.fill(white)

#name = input('Your name: ')

class Ball:
    def __init__(self, x, y, dx, dy, image):
        self.img = pg.transform.scale(image, (150, 150))
        self.dx = dx
        self.dy = dy
        self.rect = screen.blit(self.img, (x, y))
        if rnd.randint(-4, 4) == -4:
            self.image = pg.image.load(os.path.join(img_folder, 'ball.jpg'))
            self.cofe = -3
        elif rnd.randint(-4, 4) == -3:
            self.image = pg.image.load(os.path.join(img_folder, 'ball3.jpg'))
            self.cofe = -2
        elif rnd.randint(-4, 4) == -2:
            self.image = pg.image.load(os.path.join(img_folder, 'ball2.jpg'))
            self.cofe = -1
        elif rnd.randint(-4, 4) == -1:
            self.image = pg.image.load(os.path.join(img_folder, 'ball4.jpg'))
            self.cofe = 0
        elif rnd.randint(-4, 4) == 0:
            self.image = pg.image.load(os.path.join(img_folder, 'ball1.jpg'))
            self.cofe = 1
        elif rnd.randint(-4, 4) == 1:
            self.image = pg.image.load(os.path.join(img_folder, 'ball5.jpg'))
            self.cofe = 2
        elif rnd.randint(-4, 4) == 2:
            self.image = pg.image.load(os.path.join(img_folder, 'ball8.jpg'))
            self.cofe = 3
        elif rnd.randint(-4, 4) == 3:
            self.image = pg.image.load(os.path.join(img_folder, 'ball7.jpg'))
            self.cofe = 4
        else:
            self.image = pg.image.load(os.path.join(img_folder, 'ball6.jpg'))
            self.cofe = 5
        return



    def show(self):
        screen.blit(self.img, self.rect)

    def move(self):
        self.rect = self.rect.move([self.dx, self.dy])
        self.show()
        return

    def check_collide_with_walls(self, left_x, right_x, top_y, bottom_y):
        if self.rect.left < left_x or self.rect.right > right_x:
            self.dx *= -1

        if self.rect.top < top_y or self.rect.bottom > bottom_y:
            self.dy *= -1
        return

    def check_click(self, coords):
        if self.rect.left < coords[0] and self.rect.right > coords[0] and self.rect.top < coords[1]\
        and self.rect.bottom > coords[1]:
            return True
        return False


def score(Score):
    text = font.render("Score: " + str(Score), True, (0, 0, 255))
    screen.blit(text, (100, 100))


circles = ("ball.jpg", "ball1.jpg", "ball2.jpg", "ball3.jpg", "ball4.jpg",
           "ball5.jpg", "ball6.jpg", "ball7.jpg"
           )

balls_array = []
balls_n = rnd.randint(2, 7)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

for i in range(balls_n):
    balls_array.append(Ball(rnd.randint(100, width-100),
                            rnd.randint(100, height-100),
                            rnd.randint(1, 6),
                            rnd.randint(1, 6), pg.image.load(os.path.join(img_folder, rnd.choice(circles)))
                            )
                       )


clock = pg.time.Clock()
Score = 0

while True:
    score(Score)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for ball in balls_array:
                if ball.check_click(event.pos):
                    if ball.cofe == -3:
                        Score -= 3
                    

    for ball in balls_array:
        ball.move()
        ball.check_collide_with_walls(0, width, 0, height)

    pg.display.flip()
    clock.tick(30)

file = open("out.txt", "a")
file.write('Name:' + name + ': ' + str(Score) + '\n')

pygame.quit()