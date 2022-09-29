
import math
import pygame

from planet import Planet
from asteroid import Asteroid
import calcs

WIDTH, HEIGHT = 1200, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

CAPTION = "Planets"
BACKGROUND_COLOR = (21, 41, 76)
CONSTANT_G = 100
FINISH, INIT, RUNNING = range(3)
LEFT_MOUSE_BUTTON = 1
RIGHT_MOUSE_BUTTON = 3

world_offset_x = WIDTH / 2
world_offset_y = HEIGHT / 2

# Sample
PLANETS = [
    Planet((67, 26, 9), 200, 100, 50, 50),
    # Planet((67, 26, 9), 200, -100, 50, 50),
    # Planet((67, 216, 9), 500, 0, 80, -300)
]

MAX_INIT_VELOCITY = 8
INIT_VELOCITY_RADIUS = 300

def handle_forces(asteroid: Asteroid):
    acceleration_x = 0
    acceleration_y = 0

    for planet in PLANETS:
        dist = calcs.dist(planet.x, planet.y, asteroid.x, asteroid.y)
        sin = calcs.sin(planet.x, planet.y, asteroid.x, asteroid.y)
        cos = calcs.cos(planet.x, planet.y, asteroid.x, asteroid.y)

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

def handle_asteroid_initial_velocity(asteroid: Asteroid):
    click_pos = pygame.mouse.get_pos()
    dist = calcs.dist(asteroid.x, asteroid.y, click_pos[0], click_pos[1])
    init_vel = 0

    if dist > INIT_VELOCITY_RADIUS:
        init_vel = MAX_INIT_VELOCITY
    else:
        init_vel = dist * (MAX_INIT_VELOCITY/INIT_VELOCITY_RADIUS)

    ratio = init_vel / dist
    asteroid.set_velocity(ratio * (click_pos[0]-asteroid.x), ratio * (click_pos[1]-asteroid.y))

def draw_window(asteroid: Asteroid):
    WINDOW.fill(BACKGROUND_COLOR)

    for planet in PLANETS:
        planet.draw(WINDOW)
    
    asteroid.draw(WINDOW)

    pygame.display.update()

def update(asteroid: Asteroid):
    
    global world_offset_x
    global world_offset_y

    world_offset_x -= asteroid.velocity_x
    world_offset_y -= asteroid.velocity_y

    for planet in PLANETS:
        planet.set_x(planet.initial_x + world_offset_x)
        planet.set_y(planet.initial_y + world_offset_y)

    handle_collisions(asteroid)
    handle_forces(asteroid)
    asteroid.update()
    
    # print(asteroid.velocity_x, world_offset_x)

def main():

    game_state = INIT
    clock = pygame.time.Clock()

    asteroid = Asteroid(x=0, y=0)
    player_click = False
    

    while game_state:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = FINISH
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_MOUSE_BUTTON:
                player_click = True
                handle_asteroid_initial_velocity(asteroid)
            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_MOUSE_BUTTON:
                player_click = True
                
        if game_state == INIT:
            
            asteroid.set_x(world_offset_x)
            asteroid.set_y(world_offset_y)

            for planet in PLANETS:
                planet.set_x(planet.initial_x + world_offset_x)
                planet.set_y(planet.initial_y + world_offset_y)

            draw_window(asteroid)
            game_state = RUNNING

        if game_state == RUNNING:
            
            if not player_click:
                continue
            draw_window(asteroid)
            update(asteroid)
            
        if game_state == FINISH:
            pygame.quit()
            

if __name__ == "__main__":
    main()