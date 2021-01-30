# Import the Pygame library
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the window
size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("My first Pygame program")

# If this variable is true, keep the main loop running
running = True

# Manage frames per second
clock = pygame.time.Clock()


# TODO: CREATE BLOCK CLASS


# TODO: CREATE SPRITE GROUPS


# TODO: GENERATE 50 BLOCKS AT RANDOM POSITIONS


player = Block("red", 30)
all_sprites_list.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("white")

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]


    # TODO: PERFORM COLLISION DETECTION BETWEEN PLAYER AND BLOCKS


    all_sprites_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)