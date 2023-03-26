import pygame
from DongHo import *

BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((600, 640))
FPS = pygame.time.Clock()
running = True

clock = clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    clock.updateTime()
    clock.drawClock(screen)
    pygame.display.update()
    FPS.tick(60)

pygame.quit()