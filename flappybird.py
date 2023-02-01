import pygame
pygame.init()

# Game Window's variables
screen_width = 1000
screen_height = 1000 

# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

# Name and Icon of Game Window
pygame.display.set_caption('Flappy Bird')
flappybird_icon = pygame.image.load("Visuals/flappybird_icon.png")

# Game Window's textures
bg_top = pygame.image.load("Visuals/background_top.png")
bg_bottom = pygame.image.load("Visuals/background_bottom.png")

pygame.display.set_icon(flappybird_icon)

# Main Game Loop
while True:

    # Game Window     
    screen.blit(bg_top, (0,0))
    screen.blit(bg_bottom, (0,800))
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       

    pygame.display.update()