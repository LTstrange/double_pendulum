from math import sin, cos, pi

import pygame
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen_rect = screen.get_rect()

canvas = pygame.Surface(screen_rect.size).convert_alpha()
canvas.fill((0, 0, 0, 0))

# hyper param
r1 = 140
r2 = 140
m1 = 50
m2 = 50

a1 = pi / 2
a2 = pi / 2
a1_v = 0
a2_v = 0
a1_a = 0.01
a2_a = -0.001

g = 1

px2 = -1
py2 = -1


# def set_up():
#     x1 = r1 * sin(a1) + screen_rect.width / 2
#     y1 = r1 * cos(a1) + screen_rect.height / 2
#
#     x2 = r2 * sin(a2) + x1
#     y2 = r2 * cos(a2) + y1


def draw():
    global a1, a2, a1_v, a2_v, a1_a, a2_a, g, px2, py2

    num1 = -g*(2*m1 + m2)*sin(a1)
    num2 = - m2 * g * sin(a1 - 2 * a2)
    num3 = -2*sin(a1 - a2)*m2*(a2_v * a2_v * r2 + a1_v * a1_v * r1*cos(a1 - a2))
    den = r1*(2*m1 + m2 - m2 * cos(2*a1 - 2 * a2))

    a1_a = (num1 + num2 + num3) / den

    num1 = 2*sin(a1 - a2)
    num2 = a1_v * a1_v * r1 * (m1 + m2)
    num3 = g * (m1 + m2) * cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2)
    den = r2*(2*m1 + m2 - m2 * cos(2*a1 - 2 * a2))

    a2_a = (num1 * (num2 + num3 + num4)) / den

    x1 = r1 * sin(a1) + screen_rect.width / 2
    y1 = r1 * cos(a1) + screen_rect.height / 2
    pygame.draw.line(screen, THECOLORS['black'], screen_rect.center, (int(x1), int(y1)))
    pygame.draw.circle(screen, THECOLORS['black'], (int(x1), int(y1)), int(m1 / 5))

    x2 = r2 * sin(a2) + x1
    y2 = r2 * cos(a2) + y1
    pygame.draw.line(screen, THECOLORS['black'], (int(x1), int(y1)), (int(x2), int(y2)))
    pygame.draw.circle(screen, THECOLORS['black'], (int(x2), int(y2)), int(m2 / 5))

    if px2 != -1:
        pygame.draw.line(canvas, THECOLORS['gray'], (int(px2), int(py2)), (int(x2), int(y2)))

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    px2 = x2
    py2 = y2

    # a1_v *= 0.999
    # a2_v *= 0.999


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        # set_up()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(THECOLORS['white'])
        screen.blit(canvas, canvas.get_rect())
        draw()

        pygame.display.flip()


if __name__ == '__main__':
    main()
