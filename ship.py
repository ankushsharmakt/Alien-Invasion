import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # a class to manage the ship

    def __init__(self, ai_game):
        # initialize th ship and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ship's position bsed on the movement flag
        # update ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
