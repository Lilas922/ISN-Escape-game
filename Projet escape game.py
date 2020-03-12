import pygame
from pygame.locals import *
pygame.init()
largeur_grille = 10     ## nombre de case
hauteur_grille = 10
position_grille_x = 0   ## position
position_grille_y = 0

fenetre = pygame.display.set_mode(( 10 * 80 , 10 * 80 )) ## 405 largeur/hauteur_grille * largeur/hauteur image

cellule = pygame.image.load("cellule_de_prison.JPG").convert()
fenetre.blit(cellule, (0,0))

lettre = pygame.image.load("lettre.PNG").convert()     ## image lettre
fenetre.blit(lettre, (130,100))

pygame.display.flip()