import pygame

# definice vsech budoucich hracu
class Bird:
    # konstruktor
    def __init__(self, x, y, image, left_key, right_key, up_key, down_key):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_speed = 3.5
        self.image = image
        self.screen_height = 1080
        self.screen_width = 1920
        self.bird1_x = x
        self.bird1_y = y
        self.rect = self.image.get_rect()
        self.bird_height = 0
        self.bird_speed = 0
        self.left = left_key
        self.right = right_key
        self.up = up_key
        self.down = down_key
        
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
            self.bird_speed = self.pipe_speed + 1

            # Border
                    # Y
            if self.rect.y <= 0-5:
                self.rect.y = 0-5
                    # Y
            if self.rect.bottom >= self.screen_height+10:
                self.rect.bottom = self.screen_height+10
                    # X
            if self.rect.right >= self.screen_width:
                self.rect.right = self.screen_width

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

                if self.rect.bottom >= self.screen_height+10:
                    self.rect.bottom = self.screen_height+10

                if self.rect.right >= self.screen_width:
                    self.rect.right = self.screen_width

                # Game Over
                global bird1_alive
                if self.rect.right <= 0:
                    bird1_alive = False
                    self.kill()

    def update(self):
        self.gameplay()