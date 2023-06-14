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

# Player health
player_health = 100
max_health = 100
enemy_damage = 20

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
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Move the enemy downwards
    enemy_y += enemy_speed

    # Inside the game loop, after updating the enemy position

    # Detect collision between player and enemy
    if player_x < enemy_x + enemy_width and \
                player_x + player_width > enemy_x and \
                player_y < enemy_y + enemy_height \
                and player_y + player_height > enemy_y:
        player_health -= enemy_damage
        print(player_health)

    # Heal the player when they move off the screen
    if player_y < 0:
        player_health += 10
        print(player_health)
        if player_health > max_health:
            player_health = max_health
            player_y = window_height - player_height - 10
    
    # After updating the player's position

    # Check if player's health reaches zero
    if player_health <= 0:
        print("Game Over")
        player_health = max_health
        player_x = window_width // 2
        player_y = window_height - player_height - 10

    # Draw game objects
    window.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(window, (255, 0, 0), 
                     (player_x, player_y, 
                      player_width, player_height))  
    pygame.draw.rect(window, (0, 255, 0), 
                     (enemy_x, enemy_y, 
                      enemy_width, enemy_height))  # Draw enemy
    pygame.display.update()
