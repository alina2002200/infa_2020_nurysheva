from random import randrange as rnd, choice
from random import randint, random
import tkinter as tk
import math
import time
from PIL import Image, ImageTk

print(dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
image1 = Image.open('shrek5.png')
image1 = image1.resize((50, 50), Image.ANTIALIAS)
lion_image = ImageTk.PhotoImage(image1)
image2 = Image.open('shrek6.png')
image2 = image2.resize((50, 50), Image.ANTIALIAS)
fiksik_image = ImageTk.PhotoImage(image2)


class Picture1():
    '''
    class that describes picture
    '''

    def __init__(self):
        '''
        sets initial characteristics of picture
        '''
        self.points = 0
        self.live = 1
        self.r = 25
        self.id = canv.create_image(0, 0, anchor='nw', image=lion_image)

    def new_target(self):
        ''' 
        Creates new picture 
        '''
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        color = self.color = 'red'
        canv.coords(self.id, self.x, self.y)

    def hit(self, points=1):
        '''
        points in type int
        '''
        canv.coords(self.id, -100, -100)
        self.points += points

    def check_border(self):
        '''
        checks if border was hiiten 
        changes sign of velocities 
        '''
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = -self.vy

    def move(self):
        '''
        moves picture on one step in time
        '''
        self.check_border()
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x + self.vx, self.y + self.vy)


class Picture2():
    '''
    class that describes picture
    '''

    def __init__(self):
        '''
        sets initial characteristics of picture
        '''
        self.points = 0
        self.live = 1
        self.r = 25
        self.id = canv.create_image(0, 0, anchor='nw', image=fiksik_image)

    def new_target(self):
        '''
        Creates new picture
        '''
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        color = self.color = 'red'
        canv.coords(self.id, self.x, self.y)

    def hit(self, points=1):
        '''
        points in type int
        '''
        canv.coords(self.id, -100, -100)
        self.points += points

    def check_border(self):
        '''
        checks if border was hiiten
        changes sign of velocities
        '''
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = -self.vy

    def move(self):
        '''
        moves picture on one step in time
        '''
        self.check_border()
        if self.vx > 0:
            self.vx += 0.05
        else:
            self.vx -= 0.05
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x + self.vx, self.y + self.vy)


class Ball():
    def __init__(self, x=40, y=450):
        """
        Constructor of class Ball
        Args:
        x - horisontal initial state of ball
        y - vertical initial state of ball
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        # draws ball
        if randint(0, 1):
            self.id = canv.create_oval(self.x - self.r,
                                       self.y - self.r,
                                       self.x + self.r,
                                       self.y + self.r,
                                       fill=self.color)
        else:
            self.id = canv.create_rectangle(self.x - self.r,
                                            self.y - self.r,
                                            self.x + self.r,
                                            self.y + self.r,
                                            fill=self.color)
        self.live = 30

    def set_coords(self):
        '''
        sets coords of ball
        '''
        canv.coords(self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r)

    def move(self):
        '''
        Moves ball on one step in time
        Updates self.x and self.y    
        '''
        self.vy -= 1
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        if self.live < 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
            self.live -= 1
        self.set_coords()

    def hittest(self, obj):
        '''
        Checks if object hits target that defined later
        Args:
            obj: our target with which ball strikes
        Returns:
            Returns true if hitting took place, else brings false
        '''
        rho_1 = (self.x + self.r - obj.x - obj.r) ** 2
        rho_2 = (self.y + self.r - obj.y - obj.r) ** 2
        rho_3 = (self.r + obj.r) ** 2
        condition = rho_1 + rho_2 <= rho_3
        if condition:
            return True
        else:
            return False


class Target():
    '''
    class that describes target
    '''

    def __init__(self):
        '''
        sets initial characteristics of target
        '''
        self.points = 0
        self.live = 1
        if randint(0, 1):
            self.id = canv.create_oval(0, 0, 0, 0)
        else:
            self.id = canv.create_rectangle(0, 0, 0, 0)

    def new_target(self):
        ''' 
        Creates new target 
        '''
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        '''
        points in type int
        '''
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points

    def check_border(self):
        '''
        checks if border was hiiten 
        changes sign of velocities 
        '''
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = -self.vy

    def move(self):
        '''
        moves target on one step in time
        '''
        self.check_border()
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x - self.r, self.y - self.r,
                    self.x + self.r, self.y + self.r)


class Point():
    '''
    class that creates text which reflects points of game
    '''

    def __init__(self, point1, point2, point3, point4):
        '''
        points1, points2 in type int
        creates text - number of points
        '''
        # contains number of hitten targets
        self.id_points = canv.create_text(30, 30, text=point1 + point2, font='28')

    def if_hitted(self, point5, point6, point7, point8):
        '''
        updates number of points if strike came out
        points1, points2 in type int
        '''
        # writes number of points
        canv.itemconfig(self.id_points, text=point5 + point6 + point7 + point8)


class Gun():
    '''
    class that discribes Gun
    '''

    def __init__(self, x=40, y=450):
        '''
        x in type int
        y in type int
        '''
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        # draws gun
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        '''
        sets regime of fire
        event in type list
        '''
        self.f2_on = 1

    def fire2_end(self, event):
        '''
        strikes when we push the mouse button
        event in type list
        '''
        global balls, pictures, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        '''
        event in type int
        '''
        if event:
            if event.x - 20 != 0:
                self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        '''
        sets power of throw
        '''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


t1 = Target()
t2 = Target()
im1 = Picture1()
im2 = Picture2()
p = Point(t1.points, t2.points, im1.points, im2.points)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    '''
    creates new game
    '''
    global Gun, t1, t2, im1, im2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    im1.new_target()
    im2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    t1.live = 1
    t2.live = 1
    im1.live = 1
    im2.live = 1
    while t1.live or t2.live or im1.live or im2.live or balls:
        if t1.live > 0:
            t1.move()
        if t2.live > 0:
            t2.move()
        if im1.live > 0:
            im1.move()
        if im2.live > 0:
            im2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                p.if_hitted(t1.points, t2.points, im1.points, im2.points)
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                p.if_hitted(t1.points, t2.points, im1.points, im2.points)
            if b.hittest(im1) and im1.live:
                im1.live = 0
                im1.hit()
                p.if_hitted(t1.points, t2.points, im1.points, im2.points)
            if b.hittest(im2) and im2.live:
                im2.live = 0
                im2.hit()
                p.if_hitted(t1.points, t2.points, im1.points, im2.points)
            if t1.live == 0 and t2.live == 0 and im1.live == 0 and im2.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
        # updates screen after every step
        canv.update()
        # time between two updates
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
        canv.delete(balls)
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()
root.mainloop()
