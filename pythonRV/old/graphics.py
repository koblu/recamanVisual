import pygame
import math
import random
import recamanGen as rg


pygame.init()

nums = rg.recaman(int(input("Max Steps? \n")))

BLACK =     (0  ,  0,   0)
RED =       (255,  0,   0)
BLUE =      (0  ,  0, 255)
WHITE=      (255,255, 255)
PI = math.pi

size = (700,500)
scale = 500/(len(nums)+1)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recaman Visualization")
mode = "Bouncey"


done = False
increment = 60
clock = pygame.time.Clock()

while not done:
    up = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
        elif event.type == pygame.KEYDOWN:
            mode = "Bounce"
        elif event.type == pygame.KEYUP:
            mode = "Not Bounce"
            
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,250], [700,250], 3)
    
    for current_item, next_item in rg.curAndNext(nums):
        if mode == "Bounce":
            if next_item != None:
                if current_item < next_item:
                    circ = ((next_item-current_item)*scale)##circumfernce of circles
                    pygame.draw.arc(screen, BLUE, [current_item*scale, 250-(circ/2), circ, circ], 0, PI, 2)
                else:
                    circ = ((current_item-next_item)*scale)##circumfernce of circles
                    pygame.draw.arc(screen, BLUE, [next_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 2)
        else:
            if next_item != None:
                if current_item < next_item:
                    circ = ((next_item-current_item)*scale)##circumfernce of circles
                    if up:
                        pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], 0, PI, 2) 
                    else:
                        pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 2)
                        
                else:
                    circ = ((current_item-next_item)*scale)##circumfernce of circles
                    if up:
                        pygame.draw.arc(screen, RED, [next_item*scale, 250-(circ/2), circ, circ], 0, PI, 2)
                    else:
                        pygame.draw.arc(screen, RED, [next_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 2)
           # else:
            #    up = not up
            up = not up
        
    pygame.display.flip()
    increment += 0.0001
    clock.tick(math.floor(increment))