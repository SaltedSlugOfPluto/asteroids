import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def  main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        player.move(dt)

        for asteroid in asteroids:
            if asteroid.check_collison(player):
                print("Game Over") 
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collison(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        player.timer -= dt
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()