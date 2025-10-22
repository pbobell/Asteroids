import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
       
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable_group, drawable_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill("black")
        updatable_group.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collides(player):
                print("Game Over!")
                return
            for shot in shots_group:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()        
        
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
