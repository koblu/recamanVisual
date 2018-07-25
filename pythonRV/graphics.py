import pygame
import math
import recamanGen as rg


pygame.init()

nums = rg.recaman(int(input("Max Steps? \n")))

BLACK =     (0  ,  0,   0)
RED =       (255,  0,   0)
BLUE =      (0  ,  0, 255)
WHITE=      (255,255, 255)
PI = math.pi

size = (700,500)
scale = 500/len(nums)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recaman Visualization")
mode = "Bounce"
up =tu

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
            
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,250], [700,250], 3)
    
    for current_item, next_item in rg.curAndNext(nums):
        if mode = "Bounce":
            if next_item != None:
                if current_item < next_item:
                    circ = ((next_item-current_item)*scale)##circumfernce of circles
                    #print(radius, radius/2, "BITCH")
                    pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], 0, PI, 2)
                else:
                    circ = ((current_item-next_item)*scale)##circumfernce of circles
                    #print(radius, radius/2, "BITCH")
                    #print("BLUIE", current_item, next_item)
                    pygame.draw.arc(screen, BLUE, [next_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 2)
            
    pygame.display.flip()
    
    clock.tick(60)