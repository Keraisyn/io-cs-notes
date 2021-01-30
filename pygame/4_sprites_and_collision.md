# Lesson 4: Sprites and Collision

## Introduction
As we know, classes are really useful for creating reusable blueprints. In video games especially, this will allow us to have more efficient and simpler code.

In a platformer game, there's probably a player class, an enemy class, an item class, and so forth. The player class, for example, might have attributes health, points, x-position, y-position, current item. It might also have a draw() method, an update() method, a jump() method.

## Pygame Sprites
Sprites are a graphic element that moves separately from the background. The player is a sprite, the enemies are sprites, even bullets are sprites. Pygame has a built-in Sprite class that already has features programmed in.

When creating a sprite, add `pygame.sprite.Sprite` in brackets after the class name.

```python
# Put pygame.sprite.Sprite in brackets after Block. This is inheritence.
class Block(pygame.sprite.Sprite):
    def __init__(self, colour, size):
        # Initialize the super class
        super().__init__()

        # Create the image (what's seen)
        self.image = pygame.Surface([size, size])
        self.image.fill(colour)

        # Get a reference to the rectangle of this sprite.
        # Used for getting current position and setting the position.
        self.rect = self.image.get_rect()
```

This is called *inheritence* which is a more complicated topic which we'll cover in the future. Essentially, we're saying that class `Block` is a Pygame sprite. Also notice the line `super().__init__()`. This is another part of inheritence. It calls the __init__ function of pygame.sprite.Sprite, the super class. 

NOTE: Don't worry about what all this means for now. What's important is that the code is there.

Next, we create `self.image` and set it equal to a new Surface of size x size. Then, we fill it with the specified colour with `image.fill(colour)`. This image is what we see on the screen.

Finally, self.rect gets a reference to the rectangle of the sprite. With this rect, we can get access the current position `self.rect.x` and `self.rect.y`. 

## Sprite Groups
It can be really useful to group sprites together. For example, you may want to check collisions between the player and the wall sprite group. Let's create a new sprite group.

```python
# For all the block sprites. Useful for collision.
block_list = pygame.sprite.Group()
# For all sprites. Useful for drawing.
all_sprites_list = pygame.sprite.Group()
```

Then, let's create some Block sprites and add them to the group.

```python
# Create 50 blocks
for i in range(50)
    # Instantiate Block with colour black and side length 20
    block = Block('black', 20)

    # Give random starting position
    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)

    # Add to sprite group with .add()
    block_list.add(block)
    all_sprites_list.add(block)
```

## Collision
Collision detection can be a tough thing to do manually. You would need to check if every single object collides with every other one. If you have time, try coding it yourself! Luckily, Pygame sprites come with collision detection.

First let's create a player block to control.

```python
player = Block('red', 30)
all_sprites_list.add(player)
```

And setup our main loop.

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("white")

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]
```

Now, let's check for collision between the player sprite and the `block_list` sprite group with the `spritecollide()` function.

```python
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
```

The first argument is the sprite, the second is a sprite group, and `True` means to remove collided sprites from the group. This means blocks will stop being updated or drawn, essentially dissappearing.

The final step is to use `draw()` to draw all sprites from a group on screen.

```python
all_sprites_list.draw(screen)
```

Notice we use the `all_sprites_list` group to draw every sprite at the same time.

Final code is at the end of this file.

## Wall Collision
From the previous section, we know how to check when a sprite collides with a sprite group. Now, let's do something with that information by adding walls. 

Instead of having our player as a `Block` object, let's create a new player class.

```python
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
```

Then, let's check for keypresses. Depending on the key pressed, update Player's speed. Put this code into your main loop.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, -3)
```

Finally, add `all_sprites_group.update()` in the main loop. This will call the `update()` method of each sprite in the group.

```python
    all_sprites_group.update()
``` 

## Completed Example Code

### Collision Detection
```python
# Import the Pygame library
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the window
size = width, height = 800, 600
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
# all_sprites_list.add(player)

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
```

This example partially from programarcadegames.com.
They are a fantastic resource which you should check out!

### Wall Collision Example

```python
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
```

