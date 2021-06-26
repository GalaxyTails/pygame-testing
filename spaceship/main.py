# Imports

import pygame
import os

# Setup

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Spaceship Simulator")

# Variables

WHITE = 255, 255, 255
BLACK = 0, 0, 0

FPS = 60 

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))

# Functions

def display():

    WIN.fill((WHITE))
    pygame.display.update() # Required to render graphics

def loop():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        
        # FPS Capper
        
        clock.tick(FPS)
        
        # Event Checker
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        display()
                
    pygame.quit()
    
if __name__ == "__main__":
    loop()