from random import randrange as rnd, choice
import pygame
import pygame.draw

import math
import time

# print (dir(math))

pygame.init()
width = 800
length = 600
screen = pygame.display.set_mode((width, length))
font = pygame.font.Font(None, 28)
FPS = 70
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, screen, width, length, x = 40, y = 450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(COLORS)
        self.screen = screen
        self.id = pygame.draw.ellipse(screen, self.color, 
                                      (self.x - self.r,
                                      self.y - self.r,
                                      self.x + self.r,
                                      self.y + self.r))
        self.live = 30

    def set_coords(self):
        self.id = (self.x - self.r,
                   self.y - self.r,
                   self.x + self.r,
                   self.y + self.r)
        pygame.draw.rect(self.id)           

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y -= self.vy**2/2/9.8
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        rho_1 = (self.x + self.r/2.0 - obj.x - obj.r/2.0)**2
        rho_2 = (self.y + self.r/2.0  - obj.y - obj.r/2.0)**2
        rho_3 = (self.r/2.0 + obj.r/2.0)**2
        condition = rho_1 + rho_2 <= rho_3
        if condition:
            return True
        else:
            return False
      


class Gun(Ball):
    def __init__(self, screen, width, length, x = 40, y = 450):
        super().__init__(screen, width, length, x, y)
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.screen = screen
        self.id = pygame.draw.line(screen, BLACK, [20, 450], [50, 420], 7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
       


class Target(Ball):
    def __init__(self, screen, width, length, x = 40, y = 450):
        super().__init__(screen, width, length, x, y)
        self.points = 0
        self.live = 1
        self.screen = screen
    # FIXME: don't work!!! How to call this functions when object is created?
        #self.id = screen.create_oval(0,0,0,0)
        self.id_points = font.render(str(self.points), True, BLUE)
        

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED
        pygame.draw.rect(screen, color, self.id)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        screen.coords(self.id, -10, -10, -10, -10)
        self.points += points
        screen.blit(self.id_points, (100, 100))


t1 = Target(screen, width, length)
g1 = Gun(screen, width, length)
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    #canv.bind('<Button-1>', g1.fire2_start)
    #canv.bind('<ButtonRelease-1>', g1.fire2_end)
    #canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                #canv.bind('<Button-1>', '')
                #canv.bind('<ButtonRelease-1>', '')
                #canv.itemconfig( text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        pygame.display.update()
        #time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    #canv.itemconfig(text='')
    # screen.delete(gun)
    #root.after(750, new_game)


new_game()

mainloop()
