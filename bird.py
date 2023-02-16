import pygame

# definice vsech budoucich hracu
class Bird(pygame.sprite.Sprite):
    # konstruktor
    def __init__(self, pozice, velikost, barva, left_key, right_key, up_key, down_key):
        self.pozice = list(pozice)
        self.velikost = list(velikost)
        self.barva = list(barva)
        
        self.v = 0.5
        
        self.left = left_key
        self.right = right_key
        self.up = up_key
        self.down = down_key
    
    def vykreslit(self, plocha):
        pygame.draw.rect(plocha, self.barva, (self.pozice, self.velikost))
    
    def ovladat(self, stav_klavesnice):
        if(stav_klavesnice[self.left]):
            self.pozice[0] -= self.v
        if(stav_klavesnice[self.right]):
            self.pozice[0] += self.v
        if(stav_klavesnice[self.up]):
            self.pozice[1] -= self.v
        if(stav_klavesnice[self.down]):
            self.pozice[1] += self.v