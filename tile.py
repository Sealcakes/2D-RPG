import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/User/Desktop/Python/2D RPG/graphics/sprites/Rocks/blue crystal.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)