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
