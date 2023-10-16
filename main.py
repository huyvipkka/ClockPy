import pygame
from DongHo import *
scr_w = 600
scr_h = 640
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption('Clock')
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
    clock.draw_time_bar(screen, scr_w)
    pygame.display.update()
    FPS.tick(60)

pygame.quit()