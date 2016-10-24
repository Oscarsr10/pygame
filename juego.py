import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame")
    

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73
clock = pygame.time.Clock() 
carImg = pygame.image.load('racecar.png')

def car(x,y):
    screen.blit(carImg,(x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(600/2))
    screen.blit(TextSurf, TextRect)
    
    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')

def game_loop():
    x =  (800 * 0.45)
    y = (500 * 0.8)
    x_change = 0
    
    gameExit = False
   
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
    
        if x > 800 - car_width or x < 0:
            crash()      

        pygame.display.update()
        clock.tick(60)

game_loop()    
pygame.quit()
quit()