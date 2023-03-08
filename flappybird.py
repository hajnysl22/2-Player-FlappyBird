import pygame
import random
from pygame.locals import *
pygame.init()
from pipe import Pipe

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Visuals/bird.png").convert_alpha()
        self.bird1_x = screen_width/2
        self.bird1_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird1_x,self.bird1_y))
        self.bird_height = 0
        self.bird_speed = 0
        
    def gameplay(self):
        global keys
        self.collision = pygame.sprite.groupcollide(bird1, pipe, False, False)
        self.rect.y += self.bird_height
        self.rect.x -= self.bird_speed

        # Punishment for colliding the pipe
        if self.collision:    
            if keys[pygame.K_UP]:
                self.bird_height -= 0.075
                if self.bird_height >= -0.15:
                    self.bird_height = -0.15
            if keys[pygame.K_DOWN]:
                self.bird_height += 0.075
                if self.bird_height <= 0.15:
                    self.bird_height = 0.15
            # Punishing the player
            self.bird_speed = pipe_speed + 1

            # Border
                    # Y
            if self.rect.y <= 0-5:
                self.rect.y = 0-5
                    # Y
            if self.rect.bottom >= screen_height+10:
                self.rect.bottom = screen_height+10
                    # X
            if self.rect.right >= screen_width:
                self.rect.right = screen_width

        # Normal gameplay
        else:
                self.rect.y += self.bird_height
                self.rect.x -= self.bird_speed
                keys = pygame.key.get_pressed()
                # Height
                if keys[pygame.K_UP]:
                    self.bird_height -= 0.075
                    if self.bird_height >= -0.15:
                        self.bird_height = -0.15
                if keys[pygame.K_DOWN]:
                    self.bird_height += 0.075
                    if self.bird_height <= 0.15:
                        self.bird_height = 0.15
                # Movement  
                if keys[pygame.K_LEFT]:
                    self.bird_speed += 0.075
                    if self.bird_speed <= 0.15:
                        self.bird_speed = 0.15
                if keys[pygame.K_RIGHT]:
                    self.bird_speed -= 0.075
                    if self.bird_speed >= -0.15:
                        self.bird_speed = -0.15

                # Border
                if self.rect.y <= 0-5:
                    self.rect.y = 0-5

                if self.rect.bottom >= screen_height+10:
                    self.rect.bottom = screen_height+10

                if self.rect.right >= screen_width:
                    self.rect.right = screen_width

                # Game Over
                global bird1_alive
                if self.rect.right <= 0:
                    bird1_alive = False
                    self.kill()

    def update(self):
        self.gameplay()

class Bird2(pygame.sprite.Sprite):
    global bird_speed
    def __init__(self):
        super().__init__()
        # Bird 2 variables
        self.image = pygame.image.load("Visuals/bird2.png").convert_alpha()
        self.bird2_x = screen_width/5
        self.bird2_y = screen_width/2
        self.rect = self.image.get_rect(midbottom = (self.bird2_x,self.bird2_y))
        self.bird_height = 0
        self.bird_speed = 0

    def gameplay(self):
        global keys
        self.collision = pygame.sprite.groupcollide(bird2, pipe, False, False)
        self.rect.y += self.bird_height
        self.rect.x -= self.bird_speed

        # Punishment for colliding the pipe
        if self.collision:
            self.bird_speed = pipe_speed + 1

            if keys[pygame.K_w]:
                self.bird_height -= 0.075
                if self.bird_height >= -0.15:
                    self.bird_height = -0.15
            if keys[pygame.K_s]:
                self.bird_height += 0.075
                if self.bird_height <= 0.15:
                    self.bird_height = 0.15

            # Border
            if self.rect.y <= -10:
                self.rect.y = -10

            if self.rect.bottom >= screen_height+10:
                self.rect.bottom = screen_height+10

            if self.rect.right >= screen_width:
                self.rect.right = screen_width

        # Normal gameplay
        else:
                self.rect.y += self.bird_height
                self.rect.x -= self.bird_speed
                keys = pygame.key.get_pressed()
                # Height
                if keys[pygame.K_w]:
                    self.bird_height -= 0.075
                    if self.bird_height >= -0.15:
                        self.bird_height = -0.15
                if keys[pygame.K_s]:
                    self.bird_height += 0.075
                    if self.bird_height <= 0.15:
                        self.bird_height = 0.15
                # Movement  
                if keys[pygame.K_a]:
                    self.bird_speed += 0.075
                    if self.bird_speed <= 0.15:
                        self.bird_speed = 0.15
                if keys[pygame.K_d]:
                    self.bird_speed -= 0.075
                    if self.bird_speed >= -0.15:
                        self.bird_speed = -0.15

                # Border
                    # Y
                if self.rect.y <= 0-5:
                    self.rect.y = 0-5
                    # Y
                if self.rect.bottom >= screen_height+10:
                    self.rect.bottom = screen_height+10
                    # X
                if self.rect.right >= screen_width:
                    self.rect.right = screen_width

                # Game Over
                global bird2_alive
                if self.rect.right <= 0:
                    bird2_alive = False
                    self.kill()

    def update(self):
        self.gameplay()

def score():
    global high_score, bird1_score, bird2_score, last
    f = open('highscore.txt','r')
    file = f.readlines()
    last = int(file[0])

    if bird1_score > last:
        high_score = bird1_score
        f.close()
        file = open('highscore.txt', 'w')
        file.write(str(high_score))
        file.close()  
        return high_score
 
    elif bird2_score > last:      
        high_score = bird2_score
        f.close()
        file = open('highscore.txt', 'w')
        file.write(str(high_score))
        file.close()
        return high_score     

    return last

    # Game Window's variables
screen_width = 1920
screen_height = 1080

# Game Variables
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
bird_speed = 0

# Status of birds
bird1_alive = True
bird2_alive = True

# Game start + over
game_active = False

# Scores
bird1_score = 0
bird2_score = 0
font = pygame.font.Font("Visuals/FFFFORWA.TTF",25)
font2 = pygame.font.Font("Visuals/FFFFORWA.TTF",75)

# Highscore
high_score = ""


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

    # Game start
game_start = pygame.image.load("Visuals/game_start_screen.png").convert()
    # Game over
game_over = pygame.image.load("Visuals/game_over_screen.png").convert()
    # Pipes
pipe_top = pygame.image.load("Visuals/pipe_top.png").convert_alpha()
pipe_bottom = pygame.image.load("Visuals/pipe_bottom.png").convert_alpha()

    # Bird1
bird1 = pygame.sprite.Group()
bird1.add(Bird())

    # Bird2
bird2 = pygame.sprite.Group()
bird2.add(Bird2())

# Pipes
pipe = pygame.sprite.Group()

# Main Game Loop
while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True    
            bird1_alive = True
            bird2_alive = True

        if game_active:
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
    if game_active:
        if bird1_alive:
            bird1_score = int(pygame.time.get_ticks() / 1000)
            score1 = font.render(f'Player 1:  {bird1_score}', False, (255,102,178))
            score1_rect = score1.get_rect(center = (120, 50))

            # Player 2
        if bird2_alive:
            bird2_score = int(pygame.time.get_ticks() / 1000)
            score2 = font.render(f'Player 2:  {bird2_score}', False, (255,102,178))
            score2_rect = score1.get_rect(center = (120, 100))

        # Score counter
        score()

    if game_active:
        # Game Window Visuals
            # Sky
        screen.blit(bg, (0,0))
            # Obstacles
        pipe.draw(screen)
        pipe.update()
            # Bird 1
        bird1.draw(screen)
        bird1.update()        
            # Bird 2
        bird2.draw(screen)
        bird2.update()
            # Score 1
        screen.blit(score1, score1_rect)
            # Score 2
        screen.blit(score2, score2_rect)
            # Highscore
        highscore = font.render(f'Highscore:  {last}', False, (255,102,178))
        highscore_rect = highscore.get_rect(center = (1700, 50))
        screen.blit(highscore, highscore_rect)

    if game_active == False: 
        if bird1_score == 0  and bird2_score == 0:
            # Game start
            screen.blit(game_start, (0,0))
    if bird1_alive == False and bird2_alive == False:
        # Game over screen
        screen.blit(game_over, (0,0))
        # Highscore = font.render(f'Highscore: {
        highscore = font2.render(f'{last}', False, (0,0,0))
        highscore_rect = highscore.get_rect(center = (950, 450))
        screen.blit(highscore, highscore_rect)

    # Update
    pygame.display.update()

    # FPS
    clock.tick(60)