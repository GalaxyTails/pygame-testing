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
VEL = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Functions

def display(red, yellow):

    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update() # Required to render graphics

def loop():
    
    red = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        
        clock.tick(FPS) # FPS Capper
        
        # Event Checker
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
        
        # Input Checker
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # Yellow Left
            yellow.x -= VEL        
        if keys_pressed[pygame.K_d]: # Yellow Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: # Yellow Up
            yellow.y -= VEL        
        if keys_pressed[pygame.K_s]: # Yellow Down
            yellow.y += VEL        
        if keys_pressed[pygame.K_LEFT]: # Red Left
            red.x -= VEL        
        if keys_pressed[pygame.K_RIGHT]: # Red Right
            red.x += VEL
        if keys_pressed[pygame.K_UP]: # Red Up
            red.y -= VEL        
        if keys_pressed[pygame.K_DOWN]: # Red Down
            red.y += VEL

        
        display(red, yellow) # Required to render all displays
                
    pygame.quit()
    
if __name__ == "__main__":
    loop()