
import math
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
    Planet((67, 26, 9), 800, 0, 60, 300),
    Planet((67, 26, 9), 0, 400, 60, 200),
    # Planet((90, 80, 137), 400, 80, 80, 1000)
]
CONSTANT_G = 100



def handle_forces(asteroid: Asteroid):
    acceleration_x = 0
    acceleration_y = 0

    for planet in PLANETS:
        dist = math.sqrt((asteroid.x - planet.x)**2 + (asteroid.y - planet.y)**2)
        sin = (planet.y - asteroid.y) / dist
        cos = (planet.x - asteroid.x) / dist
        
        acceleration_x += CONSTANT_G * planet.mass * cos / (dist ** 2)
        acceleration_y += CONSTANT_G * planet.mass * sin / (dist ** 2)

    asteroid.set_acceleration(acceleration_x, acceleration_y)

def handle_collisions(asteroid: Asteroid):

    if asteroid.x <= 0:
        asteroid.x = 0
        asteroid.collide = True
    if asteroid.x >= WIDTH:
        asteroid.x = WIDTH
        asteroid.collide = True
    if asteroid.y <= 0:
        asteroid.y = 0
        asteroid.collide = True
    if asteroid.y >= HEIGHT:
        asteroid.y = HEIGHT
        asteroid.collide = True

    for planet in PLANETS:
        dist = math.sqrt((asteroid.x - planet.x)**2 + (asteroid.y - planet.y)**2)
        if asteroid.radius + planet.radius >= dist:
            asteroid.collide = True

def draw_window(asteroid: Asteroid):
    WINDOW.fill(BACKGROUND_COLOR)

    for planet in PLANETS:
        planet.draw(WINDOW)
    
    asteroid.draw(WINDOW)

    pygame.display.update()

def update(asteroid: Asteroid):
    
    handle_collisions(asteroid)
    handle_forces(asteroid)
    
    asteroid.update()

def main():

    pygame.init()
    pygame.display.set_caption(CAPTION)

    asteroid = Asteroid(x=400, y=375)

    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(asteroid)
        draw_window(asteroid)

    pygame.quit()

if __name__ == "__main__":
    main()