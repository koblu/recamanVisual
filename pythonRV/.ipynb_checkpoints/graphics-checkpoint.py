#Kody Bloodworth
#Recaman Sequence Visualizer

import pygame
import math
import pythonRV.recamanGen as rg

def setup_vis():
    pygame.init()

    maxsteps = 0
    while(maxsteps <=0 or maxsteps > 100):
        maxsteps = int(input("Max Steps? (1-100) \n"))
    nums = rg.recaman(maxsteps)


    #Constants
    BLACK =     (0  ,  0,   0)
    RED =       (255,  0,   0)
    BLUE =      (0  ,  0, 255)
    WHITE=      (255,255, 255)
    PI = math.pi

    size = (700,500)
    scale = 700/(max(nums))
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Recaman Visualization")
    mode = "Bouncey"

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True;
            elif event.type == pygame.KEYDOWN:
                mode = "Bounce" #Jumps forward appear "bounce" above the axis; jumps backwards, below
            elif event.type == pygame.KEYUP:
                mode = "Not Bounce" #Jumps cycle between above and below the axis, appearing circular

        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, [0,250], [700,250], 3)
        up = True

        for current_item, next_item in rg.curAndNext(nums):
            if mode == "Bounce":
                if next_item != None:
                    if current_item < next_item:
                        circ = ((next_item-current_item)*scale)##circumfernce of circles
                        pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], 0, PI, 1)
                    else:
                        circ = ((current_item-next_item)*scale)
                        pygame.draw.arc(screen, BLUE, [next_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 1)
            else:
                if next_item != None:
                    if current_item < next_item:
                        circ = ((next_item-current_item)*scale)##circumfernce of circles
                        #print(circ)
                        if up:
                            pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], 0, PI, 1)
                        else:
                            pygame.draw.arc(screen, RED, [current_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 1)
                    else:
                        circ = ((current_item-next_item)*scale)
                        #print(circ)
                        if up:
                            pygame.draw.arc(screen, BLUE, [next_item*scale, 250-(circ/2), circ, circ], 0, PI, 1)
                        else:
                            pygame.draw.arc(screen, BLUE, [next_item*scale, 250-(circ/2), circ, circ], PI, 2*PI, 1)
                up = not up
        pygame.display.flip()

        clock.tick(60)