import pygame, datetime, math

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class clock():
    def __init__(self) -> None:
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def updateTime(self) -> None:
        time = datetime.datetime.now()
        self.__hour = time.hour
        self.__minute = time.minute
        self.__second = time.second
    
    def drawClock(self, surface) -> None:
        radius = (300, 250)
        pygame.draw.circle(surface, WHITE, radius, 200, 1)

        for i in range(12):
            pygame.draw.circle(surface, RED,(300 + 190*math.sin((360/12)*i*math.pi/180), 
                                            (250 - 190*math.cos((360/12)*i*math.pi/180))), 2)

        pygame.draw.line(surface, WHITE, radius, (300 + 180*math.sin(6*math.pi/180*self.__second), 
                                                 (250 - 180*math.cos(6*math.pi/180*self.__second))), 1)

        pygame.draw.line(surface, WHITE, radius, (300 + 150*math.sin(6*math.pi/180*self.__minute), 
                                                 (250 - 150*math.cos(6*math.pi/180*self.__minute))), 2)
        if self.__hour >= 12:
            self.__hour -= 12
        pygame.draw.line(surface, WHITE, radius, (300 + 120*math.sin(30*math.pi/180*self.__hour + (math.pi/6*self.__minute/60)), 
                                                 (250 - 120*math.cos(30*math.pi/180*self.__hour + (math.pi/6*self.__minute/60)))), 3)
    
    def draw_time_bar(self, surface, width):
        font = pygame.font.SysFont("Lucida Sans", 50)
        img = font.render(f'{self.__hour}:{self.__minute}:{self.__second}', True, 'white')
        rect_txt = img.get_rect()
        surface.blit(img, (width //2 - rect_txt.width//2, 500))