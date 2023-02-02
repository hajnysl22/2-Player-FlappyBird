import pygame
pygame.init()

# Game Window's variables
screen_width = 1000
screen_height = 1000 

# Game Variables
bird_position = 500 
bird_gravity = -1




# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

# Name and Icon of Game Window
pygame.display.set_caption('Flappy Bird')
flappybird_icon = pygame.image.load("Visuals/flappybird_icon.png")
pygame.display.set_icon(flappybird_icon)
clock = pygame.time.Clock()

# Game Window's textures
bg_top = pygame.image.load("Visuals/background_top.png")
bg_bottom = pygame.image.load("Visuals/background_bottom.png")

bird = pygame.image.load("Visuals/bird.png")



# Main Game Loop
while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            bird_position -= 5

    # Bird Gravity
    bird_position -= bird_gravity

    # Game Window     
        # Sky
    screen.blit(bg_top, (0,0))
        # Bottom
    screen.blit(bg_bottom, (0,800))
        # Bird
    screen.blit(bird, (200,bird_position))

    # Update
    pygame.display.update()
    pygame.display.flip()

    # FPS
    clock.tick(60)