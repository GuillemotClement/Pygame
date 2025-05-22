import pygame
from pygame.examples.setmodescale import screen

from constants import *

def main():
    # initialisation de pygame
    pygame.init()
    # definition de la taille de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # boucle infinie du jeu
    while True:
        # permet de fermer le programme en quittant la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # on set la couleur a noir
        screen.fill("black")
        # on refresh le screen
        pygame.display.flip()

if __name__ == "__main__":
        main()