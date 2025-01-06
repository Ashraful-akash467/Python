import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Fonts
font = pygame.font.SysFont("Arial", 30)
large_font = pygame.font.SysFont("Arial", 50)

# Load Assets
car_image = pygame.image.load("car.png")  # Load your car image
enemy_image = pygame.image.load("enemy_car.png")  # Load enemy car image
background_image = pygame.image.load("road.png")  # Optional background image

# Constants
CAR_WIDTH = 50
CAR_HEIGHT = 100
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 100
LANE_WIDTH = 200

# Player Car Position
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20

# Game Variables
score = 0
clock = pygame.time.Clock()

# Enemy Car Positions
enemies = [
    {"x": random.choice([150, 350, 550]), "y": -200},
    {"x": random.choice([150, 350, 550]), "y": -600},
]

# Game Over Screen
def game_over():
    screen.fill(BLACK)
    game_over_text = large_font.render("Game Over!", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 20))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# Main Game Loop
def main():
    global car_x, score

    # Reset Variables
    car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
    car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
    score = 0
    enemies[0]["y"], enemies[1]["y"] = -200, -600

    running = True

    while running:
        screen.fill(WHITE)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 150:
            car_x -= 10
        if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - 150 - CAR_WIDTH:
            car_x += 10

        # Draw Background
        screen.blit(background_image, (0, 0))

        # Draw Player Car
        screen.blit(car_image, (car_x, car_y))

        # Update Enemies
        for enemy in enemies:
            enemy["y"] += 10  # Enemy speed
            if enemy["y"] > SCREEN_HEIGHT:
                enemy["y"] = random.randint(-800, -100)
                enemy["x"] = random.choice([150, 350, 550])
                score += 1

            # Check Collision
            if (
                car_x < enemy["x"] + ENEMY_WIDTH
                and car_x + CAR_WIDTH > enemy["x"]
                and car_y < enemy["y"] + ENEMY_HEIGHT
                and car_y + CAR_HEIGHT > enemy["y"]
            ):
                if game_over():
                    main()
                else:
                    pygame.quit()
                    sys.exit()

            # Draw Enemy
            screen.blit(enemy_image, (enemy["x"], enemy["y"]))

        # Display Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update Display
        pygame.display.update()

        # Frame Rate
        clock.tick(30)


if __name__ == "__main__":
    main()
