
import pygame

from planet import Planet
from asteroid import Asteroid

WIDTH, HEIGHT = 1200, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

CAPTION = "Planets"
BACKGROUND_COLOR = (121, 121, 200)

# Sample
PLANETS = [
    Planet((67, 26, 9), 45, 200, 60, 200),
    Planet((90, 80, 137), 400, 80, 80, 300)
]

def draw_window(asteroid):
    WINDOW.fill(BACKGROUND_COLOR)

    for planet in PLANETS:
        planet.draw(WINDOW)
    
    asteroid.draw(WINDOW)

    pygame.display.update()

def main():

    pygame.init()
    pygame.display.set_caption(CAPTION)

    asteroid = Asteroid()

    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(asteroid)

    pygame.quit()

if __name__ == "__main__":
    main()