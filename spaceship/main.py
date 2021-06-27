# Imports

import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Setup

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Spaceship Simulator")

# Variables

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60 
VEL = 3
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT = 2

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'Gun+Silencer.mp3'))
CONGRATS_SOUND = pygame.mixer.Sound(os.path.join('assets', 'Congrats.mp3'))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))
SPACE_IMAGE = pygame.image.load(os.path.join('assets', 'space.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# Functions

def bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)    
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def display(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):

    WIN.blit(SPACE, (0, 0))
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)  

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update() # Required to render graphics

def movement(keys_pressed, red, yellow):
    if keys_pressed[pygame.K_LSHIFT]:
        if keys_pressed[pygame.K_a] and yellow.x > 0: # Yellow Boost Left
           yellow.x -= VEL * 2       
        if keys_pressed[pygame.K_d] and yellow.x < WIDTH - SPACESHIP_WIDTH: # Yellow Boost Right
           yellow.x += VEL * 2
        if keys_pressed[pygame.K_w] and yellow.y > 0: # Yellow Boost Up
           yellow.y -= VEL * 2       
        if keys_pressed[pygame.K_s] and yellow.y < HEIGHT - SPACESHIP_HEIGHT - 20: # Yellow Boost Down
           yellow.y += VEL * 2  
    else:
        if keys_pressed[pygame.K_a] and yellow.x > 0: # Yellow Left
            yellow.x -= VEL        
        if keys_pressed[pygame.K_d] and yellow.x < WIDTH - SPACESHIP_WIDTH: # Yellow Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y > 0: # Yellow Up
            yellow.y -= VEL        
        if keys_pressed[pygame.K_s] and yellow.y < HEIGHT - SPACESHIP_HEIGHT - 20: # Yellow Down
            yellow.y += VEL       
        
    if keys_pressed[pygame.K_RSHIFT]:
        if keys_pressed[pygame.K_LEFT] and red.x > 0: # Red Left
            red.x -= VEL * 2        
        if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - SPACESHIP_WIDTH: # Red Right
            red.x += VEL * 2
        if keys_pressed[pygame.K_UP] and red.y > 0: # Red Up
            red.y -= VEL * 2       
        if keys_pressed[pygame.K_DOWN] and red.y < HEIGHT - SPACESHIP_HEIGHT - 20: # Red Down
            red.y += VEL * 2
    else:
        if keys_pressed[pygame.K_LEFT] and red.x > 0: # Red Left
            red.x -= VEL        
        if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - SPACESHIP_WIDTH: # Red Right
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y > 0: # Red Up
            red.y -= VEL        
        if keys_pressed[pygame.K_DOWN] and red.y < HEIGHT - SPACESHIP_HEIGHT - 20: # Red Down
            red.y += VEL

def winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, WHITE)
    CONGRATS_SOUND.play()
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def loop():
    
    red = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # Red Collision
    yellow = pygame.Rect(200, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) # Yellow Collision
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    winner_text = ""
    
    clock = pygame.time.Clock()
    run = True
    while run:
        
        clock.tick(FPS) # FPS Capper
        
        # Event Checker
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN: # Handle Keys for Bullets
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
                
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
                
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
            
        if winner_text != "":
            winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed() # Handle Keys for Movement

        bullets(yellow_bullets, red_bullets, yellow, red)
        movement(keys_pressed, red, yellow)
        display(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) # Required to render all displays
    
    loop()
    
if __name__ == "__main__":
    loop()