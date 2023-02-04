import pygame
from pygame.locals import *
pygame.init()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/bird.png")
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.bird1_x = screen_width/2
        self.bird1_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird1_x,self.bird1_y))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity -= 0.5

    def apply_gravity(self):
        self.gravity += 0.2
        self.rect.y += self.gravity
        if self.rect.bottom >= screen_height-200:
            self.rect.bottom = screen_height-200
        elif self.rect.top <= 0:
            self.rect.top = 0

    def update(self):
        self.player_input()
        self.apply_gravity()

class Bird2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/bird.png")
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.bird2_x = screen_width/5
        self.bird2_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird2_x,self.bird2_y))
        self.gravity2 = 0

    def player2_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.gravity2 -= 0.5

    def apply_gravity2(self):
        self.gravity2 += 0.2
        self.rect.y += self.gravity2
        if self.rect.bottom >= screen_height-200:
            self.rect.bottom = screen_height-200
        elif self.rect.top <= 0:
            self.rect.top = 0

    def update(self):
        self.player2_input()
        self.apply_gravity2()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/pipe.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = 0



# Game Window's variables
screen_width = 1000
screen_height = 1000 

# Game Variables
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

# Name and Icon of Game Window
pygame.display.set_caption('Flappy Bird')
flappybird_icon = pygame.image.load("Visuals/flappybird_icon.png")
pygame.display.set_icon(flappybird_icon)


# Game Window's textures
bg_top = pygame.image.load("Visuals/background_top.png")
bg_bottom = pygame.image.load("Visuals/background_bottom.png")

# Bird 1
bird = pygame.sprite.Group()
bird.add(Bird(), Bird2())

# Main Game Loop
while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       

    # Game Window Visuals
        # Sky
    screen.blit(bg_top, (0,0))
        # Bottom
    screen.blit(bg_bottom, (0,screen_height-200))
        # Bird 1
    bird.draw(screen)
    bird.update()

    # Update
    pygame.display.update()

    # FPS
    clock.tick(60)