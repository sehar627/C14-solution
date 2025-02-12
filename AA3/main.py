import pygame
from nanobot import NanoBot
from robot import Robot
# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")

# Create NanoBot instances
nano_bot = NanoBot(200, 200)  # Red
robot=Robot(300,200)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill("blue")  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Change positions manually
    nano_bot.update(event)
    robot.update(event)

    # Draw NanoBots
    nano_bot.draw(screen)
    robot.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
