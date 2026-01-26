import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Car properties
CAR_WIDTH = 50
CAR_HEIGHT = 80
CAR_COLOR = RED
CAR_SPEED = 5
TURN_SPEED = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Simulator Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Facing up initially (0 degrees)
        self.speed = 0
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(CAR_COLOR)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        # Rotate the car image
        rotated = pygame.transform.rotate(self.image, -self.angle)  # Negative for clockwise rotation
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect.topleft)

    def move(self):
        # Calculate velocity components
        rad = pygame.math.radians(self.angle)
        vx = self.speed * pygame.math.sin(rad)
        vy = -self.speed * pygame.math.cos(rad)  # Negative for forward direction

        self.x += vx
        self.y += vy

        # Boundary checks (wrap around for simplicity)
        if self.x > SCREEN_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = SCREEN_WIDTH
        if self.y > SCREEN_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = SCREEN_HEIGHT

# Create car instance
car = Car(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main game loop
running = True
while running:
    screen.fill(GREEN)  # Grass-like background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()

    # Acceleration and braking
    if keys[pygame.K_UP]:
        car.speed = min(car.speed + 0.5, CAR_SPEED)  # Accelerate
    elif keys[pygame.K_DOWN]:
        car.speed = max(car.speed - 0.5, -CAR_SPEED // 2)  # Brake/reverse
    else:
        # Natural deceleration
        if car.speed > 0:
            car.speed -= 0.2
        elif car.speed < 0:
            car.speed += 0.2

    # Turning
    if keys[pygame.K_LEFT]:
        car.angle -= TURN_SPEED if car.speed != 0 else 0
    if keys[pygame.K_RIGHT]:
        car.angle += TURN_SPEED if car.speed != 0 else 0

    # Normalize angle
    car.angle %= 360

    # Move the car
    car.move()

    # Draw the car
    car.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()