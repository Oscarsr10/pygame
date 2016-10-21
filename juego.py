import pygame
from pygame.locals import *
from pygame.tests.base_test import pygame_quit

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pygame")
    

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock() 
crashed = False
carImg = pygame.image.load('racecar.png')

def car(x,y):
    screen.blit(carImg, (x,y))

x =  (800 * 0.45)
y = (500 * 0.8)
x_change = 0
car_speed = 0


   
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change
    screen.fill(white)
    car(x,y)       

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()