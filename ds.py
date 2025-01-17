# Activate your virtual environment
venv  # On Windows

# Then install Pygame
pip install pygame


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')

# Player settings
player_color = (0, 128, 255)
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Fill the screen with a color (RGB)
    window.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(window, player_color, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
