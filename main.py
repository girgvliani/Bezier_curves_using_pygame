import pygame
import os
from positions import Position
from curves import *

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("Bezier")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 32)

white = (240, 240, 240)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)
blue = (2, 146, 255)
purple = (205, 163, 255)

t = 0
speed = 0.005
linearPosition = [Position(100, 800, 'P0'), Position(300, 200, 'P1')]
quadraticPosition = [Position(600, 800, 'P0'), Position(
    880, 450, 'P1'), Position(720, 200, 'P0')]
cubicPosition = [Position(1050, 800, 'P0'), Position(
    1280, 450, 'P1'), Position(1420, 800, 'P2'), Position(1200, 200, 'P2')]

quadraticCurve = []
cubicCurve = []

run = True

while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    text = font.render(' T = ' + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (960, 100)
    screen.blit(text, textRect)

    LinearCurve(linearPosition, t, screen, red)
    QuadraticCurve(quadraticPosition, t, screen, red, quadraticCurve, green)
    CubicCurve(cubicPosition, t, screen, red, cubicCurve, green, blue)

    if len(cubicCurve) > 2:
        pygame.draw.lines(screen, red, False, cubicCurve, 5)

    if len(quadraticCurve) > 2:
        pygame.draw.lines(screen, red, False, quadraticCurve, 5)

    if t >= 1:
        t = 0
        quadraticCurve.clear()
        cubicCurve.clear()

    for point in linearPosition:
        point.display(screen, black)
    for point in quadraticPosition:
        point.display(screen, black)
    for point in cubicPosition:
        point.display(screen, black)

    t += speed
    pygame.display.update()

pygame.quit()
