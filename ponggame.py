import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#Colours for intro page
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
# Set the height and width of the screen
size = [600, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("WELCOME TO PONG GAME 2.0")
 
# Loop until the user clicks the close button.
done = False

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
 
#Instructions 
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 4:
                display_instructions = False
 
    # Set the screen background
    screen.fill(Black)
 
    if instruction_page == 1:
        # Draw instructions for the first page
 
        text = font.render("WELCOME TO PONG GAME 2.0", True, Red) #text to display on screen
        screen.blit(text, [10, 10]) #coordinates to see where to place text 
        
        text = font.render("CLICK TO CONTINUE", True, Red) #text to display on screen
        screen.blit(text, [10, 50]) #coordinates to see where to place text 
 
        text = font.render("Page 1", True, Red) #text to display on screen
        screen.blit(text, [10, 350]) #coordinates to see where to place text 
  
    if instruction_page == 2:
        # Draw instructions for the second page
        text = font.render("IN THIS GAME YOU AND YOUR FRIEND WILL", True, Red) #text to display on screen
        screen.blit(text, [10, 10]) #coordinates to see where to place text 
        
        text = font.render("FACE OFF IN THE MOST ULTIMATE PONG GAME!", True, Red) #text to display on screen
        screen.blit(text, [10, 50]) #coordinates to see where to place text 
        
        text = font.render("CLICK TO LEARN HOW TO PLAY", True, Red) #text to display on screen
        screen.blit(text, [10, 100]) #coordinates to see where to place text 

 
        text = font.render("Page 2", True, Red) #text to display on screen
        screen.blit(text, [10, 350]) #coordinates to see where to place text 
     
    if instruction_page == 3: #Draws instructions for the 3 page
        text = font.render("PLAYER 1: W AND S", True, Red) #text to display on screen
        screen.blit(text, [10, 10]) #coordinates to see where to place text 
        
        text = font.render("PLAYER 2: UP AND DOWN", True, Red) #text to display on screen
        screen.blit(text, [10, 100]) #coordinates to see where to place text 
        
        text = font.render("Page 3", True, Red) #text to display on screen
        screen.blit(text, [10, 350])  #coordinates to see where to place text 

    pygame.display.flip()

#colours
WHITE = (0,255,255)
RED = (0,255,0)
GREEN = (255,0,0)
BLACK = (0,0,0)

#globals are functions you can call upon later in your code, when globals s called from a function or method, it returns the dictionary representing the global namespace of the module where the function or method is defined, not from where it is called.
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
BLOCK_WIDTH = 8
BLOCK_HEIGHT = 80
HALF_BLOCK_WIDTH = BLOCK_WIDTH / 2
HALF_BLOCK_HEIGHT = BLOCK_HEIGHT / 2
ball_pos = [0,0]
ball_vel = [0,0]
BLOCK1_VELOCITY = 0
BLOCK2_VELOCITY = 0
LEFT_score = 0
RIGHT_score = 0

#Window screen
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Cool Pong Game")

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_vel = [horz,-vert]

# 
def init():
    global BLOCK1_pos, BLOCK2_pos, BLOCK1_VELOCITY, BLOCK2_VELOCITY,l_score,r_score  # these are floats
    global score1, score2  # these are ints
    BLOCK1_pos = [HALF_BLOCK_WIDTH - 1,HEIGHT/2]
    BLOCK2_pos = [WIDTH +1 - HALF_BLOCK_WIDTH,HEIGHT/2]
    LEFT_score = 0
    RIGHT_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)


#draw function of the whole game field
def draw(field):
    global  LEFT_score, RIGHT_score, BLOCK1_pos, BLOCK2_pos, ball_pos, ball_vel
           
    field.fill(BLACK)
    pygame.draw.line(field, WHITE, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(field, WHITE, [BLOCK_WIDTH, 0],[BLOCK_WIDTH, HEIGHT], 1)
    pygame.draw.line(field, WHITE, [WIDTH - BLOCK_WIDTH, 0],[WIDTH - BLOCK_WIDTH, HEIGHT], 1)
    pygame.draw.circle(field, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if BLOCK1_pos[1] > HALF_BLOCK_HEIGHT and BLOCK1_pos[1] < HEIGHT - HALF_BLOCK_HEIGHT:
        BLOCK1_pos[1] += BLOCK1_VELOCITY
    elif BLOCK1_pos[1] == HALF_BLOCK_HEIGHT and BLOCK1_VELOCITY > 0:
        BLOCK1_pos[1] += BLOCK1_VELOCITY
    elif BLOCK1_pos[1] == HEIGHT - HALF_BLOCK_HEIGHT and BLOCK1_VELOCITY < 0:
        BLOCK1_pos[1] += BLOCK1_VELOCITY
    
    if BLOCK2_pos[1] > HALF_BLOCK_HEIGHT and BLOCK2_pos[1] < HEIGHT - HALF_BLOCK_HEIGHT:
        BLOCK2_pos[1] += BLOCK2_VELOCITY
    elif BLOCK2_pos[1] == HALF_BLOCK_HEIGHT and BLOCK2_VELOCITY > 0:
        BLOCK2_pos[1] += BLOCK2_VELOCITY
    elif BLOCK2_pos[1] == HEIGHT - HALF_BLOCK_HEIGHT and BLOCK2_VELOCITY < 0:
        BLOCK2_pos[1] += BLOCK2_VELOCITY

    #update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    #draw paddles and ball polygon(Surface, color, pointlist, width=0)
    pygame.draw.circle(field, RED, ball_pos, 20, 0)
    pygame.draw.polygon(field, GREEN, [[BLOCK1_pos[0] - HALF_BLOCK_WIDTH, BLOCK1_pos[1] - HALF_BLOCK_HEIGHT], [BLOCK1_pos[0] - HALF_BLOCK_WIDTH, BLOCK1_pos[1] + HALF_BLOCK_HEIGHT], [BLOCK1_pos[0] + HALF_BLOCK_WIDTH, BLOCK1_pos[1] + HALF_BLOCK_HEIGHT], [BLOCK1_pos[0] + HALF_BLOCK_WIDTH, BLOCK1_pos[1] - HALF_BLOCK_HEIGHT]], 0)
    pygame.draw.polygon(field, GREEN, [[BLOCK2_pos[0] - HALF_BLOCK_WIDTH, BLOCK2_pos[1] - HALF_BLOCK_HEIGHT], [BLOCK2_pos[0] - HALF_BLOCK_WIDTH, BLOCK2_pos[1] + HALF_BLOCK_HEIGHT], [BLOCK2_pos[0] + HALF_BLOCK_WIDTH, BLOCK2_pos[1] + HALF_BLOCK_HEIGHT], [BLOCK2_pos[0] + HALF_BLOCK_WIDTH, BLOCK2_pos[1] - HALF_BLOCK_HEIGHT]], 0)

    #ball collision check on top and bottom walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # This is the ball collison to check when the ball goes in the net or hits the blocks
    if int(ball_pos[0]) <= BALL_RADIUS + BLOCK_WIDTH and int(ball_pos[1]) in range(BLOCK1_pos[1] - HALF_BLOCK_HEIGHT,BLOCK1_pos[1] + HALF_BLOCK_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + BLOCK_WIDTH:
        RIGHT_score += 1
        ball_init(True)
        
    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - BLOCK_WIDTH and int(ball_pos[1]) in range(BLOCK2_pos[1] - HALF_BLOCK_HEIGHT,BLOCK2_pos[1] + HALF_BLOCK_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - BLOCK_WIDTH:
        LEFT_score += 1
        ball_init(False)

    #This is the score update
    myfont1 = pygame.font.SysFont("Times New Roman", 20)
    label1 = myfont1.render("Goals "+str(LEFT_score), 1, (0,255,0))
    field.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Times New Roman", 20)
    label2 = myfont2.render("Goals "+str(RIGHT_score), 1, (0,255,0))
    field.blit(label2, (470, 20))  
    
    
#keys for moving down for users to play with
def keydown(event):
    global BLOCK1_VELOCITY, BLOCK2_VELOCITY
    
    if event.key == K_UP:
        BLOCK2_VELOCITY = -8
    elif event.key == K_DOWN:
        BLOCK2_VELOCITY = 8
    elif event.key == K_w:
        BLOCK1_VELOCITY = -8
    elif event.key == K_s:
        BLOCK1_VELOCITY = 8

#keys for moving up for users to play with
def keyup(event):
    global BLOCK1_VELOCITY, BLOCK2_VELOCITY
    
    if event.key in (K_w, K_s):
        BLOCK1_VELOCITY = 0
    elif event.key in (K_UP, K_DOWN):
        BLOCK2_VELOCITY = 0

init()


#game loop
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)