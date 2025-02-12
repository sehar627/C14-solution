import pygame

class Robot:
    def __init__(self,x,y):
        """Initialize the player"""
        self.image = pygame.image.load("robot.png")  # Replace with your image path
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize if needed
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=200
        self.velocity = 15

    def update(self, event):
        """Update the player movement based on key press"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.rect.y-= self.velocity
            if event.key == pygame.K_DOWN:
                self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
