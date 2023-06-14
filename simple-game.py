import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Health System Demo")

# Player attributes
player_width, player_height = 50, 50
player_x, player_y = window_width // 2, window_height - player_height - 10
player_speed = 1

# Enemy attributes
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = random.randint(0, window_width - enemy_width), 0
enemy_speed = 0.3

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player left or right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed

    # Move the enemy downwards
    enemy_y += enemy_speed

    # Draw game objects
    window.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(window, (255, 0, 0), 
                     (player_x, player_y, 
                      player_width, player_height))  
    pygame.draw.rect(window, (0, 255, 0), 
                     (enemy_x, enemy_y, 
                      enemy_width, enemy_height))  # Draw enemy
    pygame.display.update()
