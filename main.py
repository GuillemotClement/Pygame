# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return 
      
    player.update(dt) # ajout de la rotation
      
    screen.fill("black") # ajoute le fond noir
    player.draw(screen) # dessine le joueur

    pygame.display.flip() # met a jour l'affichage

    dt = clock.tick(60) / 1000 # definit le delta



if __name__ == "__main__":
  main()