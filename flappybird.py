import pygame
import random
from pygame.locals import *
from pipe import Pipe
from bird import Bird
pygame.init()

# Game Window's variables
screen_width = 1920
screen_height = 1080

# Game Variables
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
bird_speed = 0
collision = False

# Status of birds
bird1_alive = True
bird2_alive = True

# Bird visualization
bird1_visual = pygame.image.load("Visuals/bird.png")
bird2_visual = pygame.image.load("Visuals/bird2.png")

# Scores
bird1_score = 0
bird2_score = 0
font = pygame.font.SysFont("Visuals/square-deal.ttf",50)

# Pipe Variables
pipe_speed = 3.5
pipe_timer = 0

# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

# Name and Icon of Game Window
pygame.display.set_caption('Flappy Bird')
flappybird_icon = pygame.image.load("Visuals/flappybird_icon.png")
pygame.display.set_icon(flappybird_icon)

# Game Window's textures
    # Background
bg = pygame.image.load("Visuals/background.png").convert()

    # Pipes
pipe_top = pygame.image.load("Visuals/pipe_top.png").convert_alpha()
pipe_bottom = pygame.image.load("Visuals/pipe_bottom.png").convert_alpha()

bird1 = Bird(50, 100,bird1_visual,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
# druhy hrac
bird2 = Bird(150, 200,bird2_visual,pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)


# Pipes
pipe = pygame.sprite.Group()

# Main Game Loop
while bird1_alive or bird2_alive:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       

    # Pipe Spawner
    pipe_timer -= 10
    if pipe_timer <= 0:
        # Start position of pipe
        x_top, x_bottom = 2000,2000
        # Height of pipe
        y_top = random.randint(-900,-100)
        # Gap between pipes
        y_bottom = y_top + random.randint(80,120) + pipe_bottom.get_height()
        # Adding the pipe to the background
        pipe.add(Pipe(x_top, y_top, pipe_top))
        pipe.add(Pipe(x_bottom, y_bottom, pipe_bottom))
        # Generating new timer
        pipe_timer = random.randint(1500,1800)

    # Score counter
        # Player 1
    if bird1_alive:
        bird1_score = int(pygame.time.get_ticks() / 1000)
        score1 = font.render(f'Player 1:  {bird1_score}', False, (255,102,178))
        score1_rect = score1.get_rect(center = (120, 50))

        # Player 2
    if bird2_alive:
        bird2_score = int(pygame.time.get_ticks() / 1000)
        score2 = font.render(f'Player 2:  {bird2_score}', False, (255,102,178))
        score2_rect = score1.get_rect(center = (120, 100))
 
    if pygame.sprite.groupcollide(bird1, pipe, False, False):
        collision = True
    else:
        collision = False

    # Game Window Visuals
        # Sky
    screen.blit(bg, (0,0))
        # Obstacles
    pipe.draw(screen)
    pipe.update()
        # Bird 1
    bird1.draw(screen)      
        # Bird 2
    bird2.draw(screen)
        # Score 1
    screen.blit(score1, score1_rect)
        # Score 2
    screen.blit(score2, score2_rect)

    # Update
    pygame.display.update()

    # FPS
    clock.tick(60)