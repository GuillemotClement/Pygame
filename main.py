import pygame

from constants import *
from player import Player


def main():
    # initialisation de pygame
    pygame.init()
    # definition de la taille de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0

    # creation des groupes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # ajoute des groupe au container Player
    Player.containers = (updatable, drawable)

    # instanciation du player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # boucle infinie du jeu
    while True:
        # permet de fermer le programme en quittant la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # limit le framerate to 60 FPS
        dt = clock.tick(60) / 1000

        # update la position des objets
        updatable.update(dt)

        # on set la couleur a noir
        screen.fill("black")

        # on utilise le groupe pour appliquer la methode sur chaque elements
        for sprite in drawable:
            sprite.draw(screen)

        # on refresh le screen
        pygame.display.flip()

if __name__ == "__main__":
        main()