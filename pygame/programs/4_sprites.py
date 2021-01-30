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


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, size):
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(colour)

        self.rect = self.image.get_rect()


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block('black', 20)

    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)

    block_list.add(block)
    all_sprites_list.add(block)

player = Block("red", 30)
all_sprites_list.add(player)

score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("white")

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    score += len(blocks_hit_list)

    all_sprites_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)