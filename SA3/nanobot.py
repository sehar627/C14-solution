import pygame

class NanoBot:
    def __init__(self, width, height):
        """Initialize the player"""
        self.image = pygame.image.load("nanobot.png")  # Replace with your image path
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize if needed
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height
        self.velocity = 15

    def update(self, event):
        """Update the player movement based on key press"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
