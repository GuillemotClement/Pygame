import pygame

from constants import *
from player import Player


def main():
    # initialisation de pygame
    pygame.init()
    # definition de la taille de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # instanciation du player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # boucle infinie du jeu
    while True:
        # permet de fermer le programme en quittant la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # on viens update la position du player
        player.update(dt)
        # on set la couleur a noir
        screen.fill("black")
        # affichage du player
        player.draw(screen)
        # on refresh le screen
        pygame.display.flip()
        # limit le framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
        main()