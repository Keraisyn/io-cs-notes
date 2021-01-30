# Import the Pygame library
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the window
size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Box")

# If this variable is true, keep the main loop running
running = True

# Manage frames per second
clock = pygame.time.Clock()


# Create Player class. Remember to add pygame.sprite.Sprite.
class Player(pygame.sprite.Sprite):

    # Constructor/Initializer
    def __init__(self, colour, size, x, y):
        # Call the parent (pygame.sprite.Sprite) constructor.
        super().__init__()

        # Set image of size x size with colour.
        self.image = pygame.Surface([size, size])
        self.image.fill(colour)

        # Get a reference to the rectangle and set the starting position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # vx and vy are speeds in each direction.
        # vx stands for velocity x. Velocity is another word for speed.
        self.vx = 0
        self.vy = 0

        # walls is the sprite group that we check collisions with.
        self.walls = None

    # Change the velocity/speeds. We will call this when keys are pressed.
    def change_speed(self, change_x, change_y):
        # Add velocity changes to vx and vy. 
        # Positive x means going right. Negative x means going left.
        # Positive y means going down. Negative y means going up.
        self.vx += change_x
        self.vy += change_y

    def update(self):
        # Change x position by vx. This is movement.
        self.rect.x += self.vx
        
        # Check if Player collides with a wall.
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        # For every wall Player collides with:
        for block in block_hit_list:
            # If Player is going right, set Player's right side to the wall's left.
            if self.vx > 0:
                self.rect.right = block.rect.left
            # If Player is going left, set Player's left side to the wall's right
            else:
                self.rect.left = block.rect.right
        

        # Movement in the y direction.
        self.rect.y += self.vy
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If Player is going down, set Player's bottom side to the wall's top.
            if self.vy > 0:
                self.rect.bottom = block.rect.top
            # If Player is going up, set Player's top side to the wall's bottom.
            else:
                self.rect.top = block.rect.bottom


# The Block class. Also known as walls.
class Block(pygame.sprite.Sprite):

    # Constructor. Specify colour and side length.
    def __init__(self, colour, size):
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(colour)

        self.rect = self.image.get_rect()


# Sprite groups
# block_list is for the walls. all_sprites_list contains every sprite.
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Create random blocks
for i in range(50):
    # Instantiate a Block
    block = Block('black', 20)

    # Give that block a random (x, y)
    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)

    # Add to appropriate sprite groups.
    block_list.add(block)
    all_sprites_list.add(block)

# Instantiate Player and specify which walls to collide with.
player = Player("red", 30, 200, 200)
player.walls = block_list
all_sprites_list.add(player)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # When a key is pressed, change the speed in the correct direction.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, 3)

        # When a key is released, return the speed to normal.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, -3)

    # Call update() on all sprites
    all_sprites_list.update()

    # Clear the screen
    screen.fill("white")

    all_sprites_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)
