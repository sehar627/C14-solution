import pygame
from nanobot import NanoBot  # Import the NanoBot class

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")

# Create character instance
nano_bot = NanoBot(WIDTH, HEIGHT)
nano_bot1=NanoBot(WIDTH,HEIGHT)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill("blue")  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        nano_bot.update(event)  # Pass event to NanoBot
        nano_bot1.move(event)
    nano_bot.draw(screen)
    nano_bot1.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
