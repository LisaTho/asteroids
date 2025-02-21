# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    uhu = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2    
    drawable = pygame.sprite.Group()    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player_ship = Player(x, y)
    asteroid_field = AsteroidField()
    asteroid_field.spawn(50, pygame.Vector2(100, 100), pygame.Vector2(0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((1, 1, 1))
        for to_draw in drawable:
            to_draw.draw(screen)
        updatable.update(dt)
        pygame.display.flip()        
        dt = uhu.tick(60)/1000
        for asteroid_ in asteroids:
            if asteroid_.is_colliding(player_ship):
                sys.exit("Game over!")
            

if __name__ == "__main__":
    main()