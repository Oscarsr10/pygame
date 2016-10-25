import pygame
from pygame.locals import *
import time
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame")
    

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,128,0)
cyan = (0,255,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 73
clock = pygame.time.Clock() 
carImg = pygame.image.load('racecar.png')
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    screen.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])

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
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(cyan)
        largeText = pygame.font.SysFont('comicsansms',115)
        TextSurf, TextRect = text_objects("Race Dodge", largeText)
        TextRect.center = ((800/2),(600/2))
        screen.blit(TextSurf, TextRect)
        
 #       mouse = pygame.mouse.get_pos()
        
#        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
#            pygame.draw.rect(screen, bright_green,(150,450,100,50))
#        else:
#            pygame.draw.rect(screen, green,(150,450,100,50))
#        smallText = pygame.font.Font("freesansbold.ttf",20)
#        textSurf, textRect = text_objects("START!", smallText)
#        textRect.center = ( (150+(100/2)), (450+(50/2)) )
#        screen.blit(textSurf, textRect)
        
#        pygame.draw.rect(screen, red,(550,450,100,50))
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()  
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def quitgame():
    pygame.quit()
    quit()

def game_loop():
    x =  (800 * 0.45)
    y = (500 * 0.8)
    x_change = 0
    
    thing_startx = random.randrange(0, 800)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    
    thingCount = 1

    dodged = 0
    
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
        screen.fill(cyan)
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
    
        if x > 800 - car_width or x < 0:
            crash()
            
        if thing_starty > 600:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,800) 
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 0.8)
        
        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
    

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()    
pygame.quit()
quit()