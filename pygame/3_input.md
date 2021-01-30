# Lesson 3: Input

## Introduction
Games follow the structure of Input => Processing => Output. We're great at the Processing part through Python, as well as the Output part through drawing. Now, how can we use the Input? Input takes many forms, but the ones we'll be using are the keyboard and the mouse.

## Mouse Input
Let's create a function that draws something. This example was made by Tony Dong:

```python
def draw_stickman(x, y):
    pygame.draw.ellipse(screen, "blue", [x, y, 200, 200]) #stick figure head
    pygame.draw.line(screen, "yellow", [x + 100, y + 200], [x + 100, y + 400], 7) #stick figure body
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 150, y + 150], 7) #stick figure main part of smile
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x, y + 500], 7) #left leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x + 200, y + 500], 7) #right leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x, y + 200], 7) #left arm of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x + 200, y + 200], 7) #right arm of stick igure
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 30, y + 130], 7) #left smile of stick figure
    pygame.draw.line(screen, "yellow", [x + 150, y + 150], [x + 170, y + 130], 7) #right smile of stick figure
    pygame.draw.polygon(screen, "red", [[x + 20, y + 100], [x + 60, y + 70], [x + 90, y + 100]]) #left eye of stick figure
    pygame.draw.polygon(screen, "red", [[x + 100, y + 100], [x + 140, y + 70], [x + 170, y + 100]]) #right eye of stick figure
```

This function will draw a stick man at (x, y). Eg. `draw_stickman(100, 200)`.

To get the position of the mouse, we'll use a special Pygame function.

```python
    pos = pygame.mouse.get_pos()
```

`pygame.mouse.get_pos()` returns a list with the x coordinate and the y coordinate `[x, y]`. We are creating a variable `pos` equal to that list. To get the x coordinate, use `pos[0]`. To get the y coordinate, use `pos[1]`.

```python
    x = pos[0]
    y = pos[1]
```

Finally, we'll pass `x` and `y` into the `draw_stickman()` function.

```python
    draw_stickman(x, y)
```

Our final loop looks like this:

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    draw_stickman(x, y)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)
```

Try printing `x` and `y` to see the current position in numbers.

## Keyboard Input
To get keypresses, we will use Pygame events.

Using arrow keys, we're going to move our stick man around, so let's make some variables for animation.

```python
# Speed of the stick man. How many pixels in each direction it moves every frame.
x_speed = 0
y_speed = 0

# Position of the stick man. The current coordinates.
x_pos = 200
y_pos = 200
```

If you check the Pygame template, you'll notice something like this:

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

This code checks for the event type `pygame.QUIT` which occurs when the user presses the red 'x' button.

There are also events for keypresses. The `pygame.KEYDOWN` event occurs when a user presses a key down. The `pygame.KEYUP` event occurs when a user lets go of a key.

In order to make the stick man move, we are going to change the speeds depending on which keys are pressed.

When the left arrow is pressed, `x_speed` is set to -4 pixels every frame because we want to decrease the x position. When the right arrow is pressed, `x_speed` is set to 4 beacuse we want to increase the x position. The same goes for up and down arrows. Up arrow sets `y_speed` to -4, while down arrow sets `y_speed` to 4.

When the left or right arrow is let go, `x_speed` is set to 0 because we don't want to stick man to move anywhere. Similarly with the up or down arrows. When they are let go, set `y_speed` to 0.

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -4
            elif event.key == pygame.K_RIGHT:
                x_speed = 4
            elif event.key == pygame.K_UP:
                y_speed = -4
            elif event.key == pygame.K_DOWN:
                y_speed = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    screen.fill('white')

    x_pos += x_speed
    y_pos += y_speed

    draw_stickman(x_pos, y_pos)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)
```

There are many other keys you can search for besides the arrows. Check the internet and documentation to find their codes!

## Completed Example Code

### Mouse input
```python
# Import the Pygame library
import pygame

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

def draw_stickman(x, y):
    pygame.draw.ellipse(screen, "blue", [x, y, 200, 200]) #stick figure head
    pygame.draw.line(screen, "yellow", [x + 100, y + 200], [x + 100, y + 400], 7) #stick figure body
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 150, y + 150], 7) #stick figure main part of smile
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x, y + 500], 7) #left leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x + 200, y + 500], 7) #right leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x, y + 200], 7) #left arm of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x + 200, y + 200], 7) #right arm of stick igure
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 30, y + 130], 7) #left smile of stick figure
    pygame.draw.line(screen, "yellow", [x + 150, y + 150], [x + 170, y + 130], 7) #right smile of stick figure
    pygame.draw.polygon(screen, "red", [[x + 20, y + 100], [x + 60, y + 70], [x + 90, y + 100]]) #left eye of stick figure
    pygame.draw.polygon(screen, "red", [[x + 100, y + 100], [x + 140, y + 70], [x + 170, y + 100]]) #right eye of stick figure

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    draw_stickman(x, y)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)
```

### Keyboard Input
```python
# Import the Pygame library
import pygame

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

def draw_stickman(x, y):
    pygame.draw.ellipse(screen, "blue", [x, y, 200, 200]) #stick figure head
    pygame.draw.line(screen, "yellow", [x + 100, y + 200], [x + 100, y + 400], 7) #stick figure body
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 150, y + 150], 7) #stick figure main part of smile
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x, y + 500], 7) #left leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 400], [x + 200, y + 500], 7) #right leg of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x, y + 200], 7) #left arm of stick figure
    pygame.draw.line(screen, "yellow", [x + 100, y + 300], [x + 200, y + 200], 7) #right arm of stick igure
    pygame.draw.line(screen, "yellow", [x + 50, y + 150], [x + 30, y + 130], 7) #left smile of stick figure
    pygame.draw.line(screen, "yellow", [x + 150, y + 150], [x + 170, y + 130], 7) #right smile of stick figure
    pygame.draw.polygon(screen, "red", [[x + 20, y + 100], [x + 60, y + 70], [x + 90, y + 100]]) #left eye of stick figure
    pygame.draw.polygon(screen, "red", [[x + 100, y + 100], [x + 140, y + 70], [x + 170, y + 100]]) #right eye of stick figure

# Speed of the stick man. How many pixels in each direction it moves every frame.
x_speed = 0
y_speed = 0

# Position of the stick man. The current coordinates.
x_pos = 100
y_pos = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -4
            elif event.key == pygame.K_RIGHT:
                x_speed = 4
            elif event.key == pygame.K_UP:
                y_speed = -4
            elif event.key == pygame.K_DOWN:
                y_speed = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    screen.fill('white')

    x_pos += x_speed
    y_pos += y_speed

    draw_stickman(x_pos, y_pos)

    # Update the screen
    pygame.display.flip()

    # Set framerate to 60 per second
    clock.tick(60)
```