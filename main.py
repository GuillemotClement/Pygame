import sys
from csv import unix_dialect

import pygame

from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    # initialisation de pygame
    pygame.init()
    # definition de la taille de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    # creation des groupes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # groupement des asteroids
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # ajoute des groupes au container
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    # instanciation du player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        # permet de fermer le programme en quittant la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # limit le framerate to 60 FPS
        dt = clock.tick(60) / 1000

        # update la position des objets
        updatable.update(dt)

        for obj in asteroids:
            if player.check_collision(obj):
                print("Game over!")
                sys.exit(1)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    # si une bullet touche on split l'asteroid
                    new_asteroids = asteroid.split()
                    if new_asteroids is not None:
                        astr1, astr2 = new_asteroids
                        # on ajoute les deux nouveaux dans le group
                        asteroids.add(astr1)
                        asteroids.add(astr2)
                    bullet.kill()

        # on set la couleur a noir
        screen.fill("black")

        # on utilise le groupe pour appliquer la methode sur chaque elements
        for obj in drawable:
            obj.draw(screen)

        # on refresh le screen
        pygame.display.flip()




if __name__ == "__main__":
        main()