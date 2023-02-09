import pygame
import random
from pygame.locals import *
pygame.init()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/bird.png").convert_alpha()
        self.bird1_x = screen_width/2
        self.bird1_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird1_x,self.bird1_y))
        self.bird_height = 0
        self.bird_speed = 0

    def player_input(self):
        self.rect.y += self.bird_height
        self.rect.x -= self.bird_speed
        keys = pygame.key.get_pressed()
        # Height
        if keys[pygame.K_UP]:
            self.bird_height -= 0.1
        if keys[pygame.K_DOWN]:
            self.bird_height += 0.1

        # Movement
        if keys[pygame.K_LEFT]:
            self.bird_speed += 0.1
        if keys[pygame.K_RIGHT]:
            self.bird_speed -= 0.1

        # Border
        if self.rect.y <= 0-5:
            self.rect.y = 0-5

        if self.rect.bottom >= screen_height+10:
            self.rect.bottom = screen_height+10

        if self.rect.right >= screen_width:
            self.rect.right = screen_width

    def bird_death(self):
        global bird1_alive
        if self.rect.right <= -10:
            bird1_alive = False
            self.kill()

    def update(self):
        self.player_input()
        self.bird_death()

class Bird2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/bird2.png").convert_alpha()
        self.bird2_x = screen_width/5
        self.bird2_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird2_x,self.bird2_y))
        self.bird_height = 0
        self.bird_speed = 0

    def player2_input(self):
        self.rect.y += self.bird_height
        self.rect.x -= self.bird_speed
        keys = pygame.key.get_pressed()
        # Height
        if keys[pygame.K_w]:
            self.bird_height -= 0.1
        if keys[pygame.K_s]:
            self.bird_height += 0.1
        # Movement  
        if keys[pygame.K_a]:
            self.bird_speed += 0.1
        if keys[pygame.K_d]:
            self.bird_speed -= 0.1

        # Border
        if self.rect.y <= 0-10:
            self.rect.y = 0-10

        if self.rect.bottom >= screen_height+10:
            self.rect.bottom = screen_height+10

        if self.rect.right >= screen_width:
            self.rect.right = screen_width

    def collision(self):
        print(1)

    def bird_death(self):
        global bird2_alive 
        if self.rect.right <= -10:
            bird2_alive = False
            self.kill()

    def update(self):
        self.player2_input()
        self.bird_death()

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
       
    def update(self):
        self.rect.x -= pipe_speed
        if self.rect.x <= -200: 
            self.kill()

    # Game Window's variables
screen_width = 1000
screen_height = 1000 

# Game Variables
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

# Status of birds
bird1_alive = True
bird2_alive = True

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

# Birds
bird1 = pygame.sprite.Group()
bird1.add(Bird(),)

bird2 = pygame.sprite.Group()
bird2.add(Bird2(),)

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
        x_top, x_bottom = 1200,1200
        y_top = random.randint(-900,-100)
        y_bottom = y_top + 100 + pipe_bottom.get_height()
        pipe.add(Pipe(x_top, y_top, pipe_top))
        pipe.add(Pipe(x_bottom, y_bottom, pipe_bottom))
        pipe_timer = random.randint(1200,2000)
        
    # Collisions
    collisions = pygame.sprite.groupcollide(bird1, pipe, False, False)
    if collisions:
        print(1)

    # Game Window Visuals
        # Sky
    screen.blit(bg, (0,0))
        # Bird 1
    bird1.draw(screen)
    bird1.update()        
        # Bird 2
    bird2.draw(screen)
    bird2.update()
        # Obstacles
    pipe.draw(screen)
    pipe.update()

    # Update
    pygame.display.update()

    # FPS
    clock.tick(60)