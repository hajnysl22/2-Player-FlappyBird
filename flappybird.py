import pygame
pygame.init()

# Game Window's variables
width = 600
height = 600 

# Game Window
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Flappy Bird')
flappybird_icon = pygame.image.load("flappybird_icon.png")

pygame.display.set_icon(flappybird_icon)

# Main Game Loop
while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Game Window     
    screen.fill((255, 255, 255))        