import pygame
from pygame.draw import *

# cortege of colors that are used in the picture
BROWN = (66, 33, 11)
ORANGE = (252, 142, 49)
BURGUNDY = (172, 67, 52)
VIOLET = (48, 16, 38)
YELLOW = (255, 255, 0)
SANDY = (254, 213, 148)
PINKISH = (254, 213, 196)
PURPLE = (179, 134, 148)


# creates a bird in form of check mark
# which lower point is described by coordinates x, y in type int
# and color by color in type tuple
def bird(screen, scale, x, y, color):
    '''
    scale - scale of the bird in type float
    x - x_coordinate of lower point in type int
    y - y_coordinate of lower point in type int
    color - color of bird in type tuple
    '''
    list_of_coordinates = [(x, y), (x + scale * 87, y - scale * 50)]
    for j in range(78):
        list_of_coordinates.append((x + scale * 87 - scale * j,
                                    y - scale * 50 + scale * 33 * j ** 2 / (77 ** 2)))
    for j in range(-82, 1):
        list_of_coordinates.append((x - scale * 72 - scale * j,
                                    y - scale * 50 + scale * 33 * j ** 2 / (82 ** 2)))
    for j in range(-3, 1):
        list_of_coordinates.append((x - scale * 77 + scale * 10 * j ** 2 / 9,
                                    y - scale * 47 + scale * j))
    for j in range(10):
        list_of_coordinates.append((x - scale * 77 + scale * j ** 2 / 8,
                                    y - scale * 47 + scale * j))
    polygon(screen, color, list_of_coordinates)


# creates a sun in form of circle with radius in type int,
# coordinates in type tuple,
# and color in type tuple
def sun(radius, coordinates, color):
    '''
    radius - radius of a circle of sun in type int
    coordinates - coordinates of the center of the sun in type tuple
    color - color of the sun in type tuple
    '''
    circle(screen, color, coordinates, radius)


# creates background of the picture, four different strips
def background(sky_color, far_mountains_sky_color,
               middle_mountains_sky_color, near_mountains_sky_color):
    '''
    sky_color - color of higher part of background in type tuple
    far_mountains_sky_color - color of the second
    from top part of background in type tuple
    middle_mountains_sky_color - color of the third
    from top part of background in type tuple
    near_mountains_sky_color - color of the forth
    from top part of background in type tuple
    '''
    rect(screen, sky_color, (0, 0, width_of_background,
                             0.223 * lenght_of_background))
    rect(screen, far_mountains_sky_color, (0, 0.222 * lenght_of_background,
                                           width_of_background,
                                           0.223 * lenght_of_background))
    rect(screen, middle_mountains_sky_color, (0, 0.444 * lenght_of_background,
                                              width_of_background,
                                              0.223 * lenght_of_background))
    rect(screen, near_mountains_sky_color, (0, 0.666 * lenght_of_background,
                                            width_of_background,
                                            0.335 * lenght_of_background))


# creates far_mountains
def far_mountains(color):
    '''
    color - color of far_mountains in type tuple
    '''
    # creates a right polygon that is the part of the right far mountains
    polygon(screen, color, [(0, 307), (width_of_background, 225),
                            (0.928 * width_of_background, 195), (0.880 * width_of_background, 217),
                            (0.840 * width_of_background, 172), (0.784 * width_of_background, 187),
                            (0.744 * width_of_background, 142), (0.744 * width_of_background, 202),
                            (0.500 * width_of_background, 266)])
    # creates a middle polygon that is the part of the right far mountains
    polygon(screen, color, [(0.500 * width_of_background, 266), (0.536 * width_of_background, 232),
                            (0.560 * width_of_background, 247), (0.592 * width_of_background, 217),
                            (width_of_background, 225), (0.500 * width_of_background, 266)])
    # creates a left part of the right spike of the far mountain
    list_of_coordinates1 = []
    for i in range(97 * width_of_background // 1000):
        j = i
        list_of_coordinates1.append((0.592 * width_of_background + i * width_of_background / 1000,
                                     217 - j ** 2 / 136))
    list_of_coordinates1.append((0.688 * width_of_background, 225))
    polygon(screen, color, list_of_coordinates1)
    # creates pike of the right spike of the far mountain
    list_of_coordinates2 = []
    for i in range(33):
        list_of_coordinates2.append((0.720 * width_of_background - i, 120 + i ** 2 / 34))
    list_of_coordinates2.append((0.688 * width_of_background, 225))
    list_of_coordinates2.append((0.744 * width_of_background, 225))
    list_of_coordinates2.append((0.744 * width_of_background, 142))
    polygon(screen, color, list_of_coordinates2)
    # creates a rounding of the pike of the spike of far mountain
    list_of_coordinates3 = []
    for i in range(25):
        list_of_coordinates3.append((0.720 * width_of_background + i, 120 + i ** 2 / 26))
    polygon(screen, color, list_of_coordinates3)
    # creates left part of the left spike of far mountains
    list_of_coordinates4 = [(0, 307)]
    for i in range(120):
        list_of_coordinates4.append((0.008 * width_of_background + i, 277 - i ** 2 / 128))
    list_of_coordinates4.append((0.128 * width_of_background, 262))
    polygon(screen, color, list_of_coordinates4)
    # creates the main body of the left part of far mountains
    polygon(screen, color, [(0, 307), (8, 277), (128, 262),
                            (128, 165), (168, 180), (184, 195),
                            (400, 255), (480, 240), (500, 266)])


# creates middle_mountains
def middle_mountains(color):
    '''
    color - color of middle_mountains in type tuple
    '''
    # creates left spike of mountain
    ellipse(screen, color, [0.040 * width_of_background, 285, 0.160 * width_of_background, 300])
    # creates lower part of middle_mountains
    polygon(screen, color, [(0, 450), (0, 337),
                            (0.016 * width_of_background, 337), (0.200 * width_of_background, 435),
                            (0.240 * width_of_background, 375), (0.280 * width_of_background, 397),
                            (0.320 * width_of_background, 307), (0.432 * width_of_background, 322),
                            (0.500 * width_of_background, 375), (0.600 * width_of_background, 360),
                            (0.800 * width_of_background, 367), (0.840 * width_of_background, 307),
                            (0.880 * width_of_background, 337), (0.920 * width_of_background, 307),
                            (0.960 * width_of_background, 337), (width_of_background, 285),
                            (width_of_background, 450), (0, 465)])
    # creates middle spike of mountain
    list_of_coordinates5 = []
    for i in range(97):
        list_of_coordinates5.append((696 - i, 293 + i ** 2 / 136))
    list_of_coordinates5.append((696, 367))
    polygon(screen, color, list_of_coordinates5)
    # creates left part of the right spike
    list_of_coordinates6 = []
    for i in range(53):
        list_of_coordinates6.append((696 + i, 293 + i ** 2 / 74))
    list_of_coordinates6.append((696, 330))
    polygon(screen, color, list_of_coordinates6)
    # creates lower left part of the right spike
    list_of_coordinates7 = []
    for i in range(53):
        list_of_coordinates7.append((801 - i, 367 - i ** 2 / 72))
    list_of_coordinates7.append((696, 330))
    list_of_coordinates7.append((696, 367))
    polygon(screen, color, list_of_coordinates7)


# creates near_mountains
def near_mountains(color):
    '''
    color - color of near_mountains in type tuple
    '''
    # creates left part of the near_mountains
    polygon(screen, color, [(0, 360), (120, 390), (240, 510),
                            (320, 600), (320, 675), (0, 675),
                            (0, 360)])
    # creates middle part of the near_mountains
    list_of_coordinates8 = []
    for i in range(181):
        list_of_coordinates8.append((500 - i, 660 - i ** 2 / 540))
    list_of_coordinates8.append((320, 675))
    list_of_coordinates8.append((500, 675))
    polygon(screen, color, list_of_coordinates8)
    polygon(screen, color, [(500, 659), (700, 550), (760, 590),
                            (760, 675), (500, 675), (500, 659)])
    # creates middle part of the right part of near_mountains
    list_of_coordinates9 = []
    for i in range(-60, 1):
        list_of_coordinates9.append((820 + i, 610 - i ** 2 / 180))
    list_of_coordinates9.append((820, 675))
    list_of_coordinates9.append((760, 675))
    polygon(screen, color, list_of_coordinates9)
    # creates right part of the near_mountains
    list_of_coordinates10 = []
    for i in range(121):
        list_of_coordinates10.append((1000 - i, 430 + i ** 2 / 144))
    list_of_coordinates10.append((880, 675))
    list_of_coordinates10.append((1000, 675))
    polygon(screen, color, list_of_coordinates10)
    # creates middle part of the right near_mountains
    list_of_coordinates11 = []
    for i in range(61):
        list_of_coordinates11.append((820 + i, 610 - i ** 2 / 45))
    list_of_coordinates11.append((880, 675))
    list_of_coordinates11.append((820, 675))
    polygon(screen, color, list_of_coordinates11)


# creates higher birds in the sky with color in type tuple
def all_birds_from_above(screen, color):
    '''
    color - color of birds in type tuple
    screen - screen in type pygame.Surface
    '''
    bird(screen, 0.45, 400, 245, color)
    bird(screen, 0.45, 500, 246, color)
    bird(screen, 0.45, 510, 300, color)
    bird(screen, 0.45, 440, 324, color)


# creates lower birds in the sky with color in type tuple
def all_birds_from_below(screen, color):
    '''
    screen - screen in type pygame.Surface
    color - color of birds in type tuple
    '''
    bird(screen, 0.55, 800, 560, color)
    bird(screen, 0.3, 820, 500, color)
    bird(screen, 0.4, 700, 520, color)
    bird(screen, 0.45, 660, 460, color)


# creates transparent birds in the top (Added function)
def transparent_birds_from_above(surface_bird, color):
    '''
    surface_bird - screen in type pygame.Surface
    color - color of birds in type tuple
    '''
    surface_bird.fill((0, 0, 255))
    all_birds_from_above(surface_bird, color)
    surface_bird.set_alpha(150)
    surface_bird.set_colorkey((0, 0, 255))
    screen.blit(surface_bird, [0, 0])


pygame.init()

FPS = 30
# creates a screen with width and length given by width_of_background
# and length_of_background in type int
width_of_background = 1000
length_of_background = 675
screen = pygame.display.set_mode((width_of_background, lenght_of_background))
# creates all background, sun, far_mountains, middle_mountains 
background(SANDY, PINKISH, SANDY, PURPLE)
sun(56, (500, 150), YELLOW)
far_mountains(ORANGE)
middle_mountains(BURGUNDY)
near_mountains(VIOLET)
# creates birds s number of them transparent
surface_bird = pygame.Surface((1000, 675))
transparent_birds_from_above(surface_bird, BROWN)
all_birds_from_below(screen, BROWN)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

