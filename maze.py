import pygame , sys
import time
import random
from tkinter import *
from pygame.locals import *



WIDTH =440
HEIGHT = 440
FPS = 200

WHITE =(255 , 255 , 255)
RED = ( 255, 0 , 0)
BLUE = (0 , 0, 255)
YELLOW = (255 , 255 , 0)
Black =(0,0,0)
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH , HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Maze")
main_font = pygame.font.SysFont("cambria", 50)
clock = pygame.time.Clock()

#maze variables
x= 0
y =0
w =20
grid=[]
visited=[]
stack=[]
solution={}


    
    

def build_grid(x , y , w):
    
    for i in range(1 , 21):
        x =20
        y = y+20
        for j in range (1 , 21 ):
            
            pygame.draw.line(screen , Black,[x, y] , [x + w ,y])
            pygame.draw.line(screen , Black , [ x+ w, y], [x+w , y+w])
            pygame.draw.line(screen , Black , [x +w,y+w] , [x ,y +w])
            pygame.draw.line(screen , Black , [x , y+w], [x,y])
            grid.append((x,y))
            x =x + 20

def push_up(x,y):
    pygame.draw.rect(screen , BLUE , (x+1 , y- w+ 1, 19 ,39) ,0)
    pygame.display.update()


def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, RED, (x +1, y +1, 18, 18), 0)          # draw a single width cell
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        # used to re-colour the path after single_cell
    pygame.display.update()                                        # has visited cell


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)             # used to show the solution
    pygame.display.update()    


def carve_out_maze(x,y):
    single_cell(x,y)
    stack.append((x,y))
    visited.append((x,y))
    while len(stack) > 0:
        time.sleep(.07)
        cell =[]
        if (x+w , y) not in visited and (x+w , y) in grid:
            cell.append("right")
        if (x-w , y) not in visited and (x-w , y) in grid :
            cell.append("left")
        if (x , y+w) not in visited and (x,y +w) in grid :
            cell.append("down")
        if (x,y-w) not in visited and (x , y-w) in grid :
            cell.append("up")   

        if len(cell) > 0 :
            cell_chosen = (random.choice(cell))

            if cell_chosen == "right":
                push_right(x, y)
                solution[(x +w ,y )]= x, y  
                x =x +w
                visited.append((x, y))
                stack.append((x,y))

            elif cell_chosen =="left":
                push_left(x,y)
                solution [(x -w ,y)] =x , y
                x=x-w
                visited.append((x,y))       
                stack.append((x,y))
            
            elif cell_chosen =="down":
                push_down(x, y)
                solution[(x, y+w)] = x,y
                y=y+w
                visited.append((x,y))
                stack.append((x,y))

            elif cell_chosen =="up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))

        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # slow program down a bit
            backtracking_cell(x, y) 


def plot_route_back(x,y):
    solution_cell(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (20,20):                                     # loop until cell position == start position
        x, y = solution[x, y]                                    # "key value" now becomes the new key
        solution_cell(x, y)                                      # animate route back
        time.sleep(.1)

x , y = 20 , 20


#build_grid(40, 0, 20)
#carve_out_maze(x, y)
#plot_route_back(400, 400)



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN :
            build_grid(40, 0, 20)
            carve_out_maze(20, 20)
            plot_route_back(400, 400)
        if event.type == pygame.QUIT:
            sys.exit()
            running =False

