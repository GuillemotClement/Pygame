import pygame

from constants import *

def main():
    # initialisation de pygame
    pygame.init()
    # definition de la taille de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0


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

        # limit le framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
        main()