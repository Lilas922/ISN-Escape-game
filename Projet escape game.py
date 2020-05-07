import pygame
from pygame.locals import *   #importer les constantes de Pygame
pygame.init()        #initialise tous les modules

#largeur_grille = 10  ## nombre de case
#hauteur_grille = 10
#position_grille_x = 0  ## position
#position_grille_y = 0

fenetre = pygame.display.set_mode(( 800 , 800 )) ## affichage fenêtre pygame 405 largeur/hauteur_grille * largeur/hauteur image

cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre
fenetre.blit(cellule, (0,0))

lettre = pygame.image.load("lettre.jpg").convert()    ## image lettre
#f = open("lettre.jpg")
#pygame.image.load(f)
fenetre.blit(lettre, (104,56))


pygame.display.flip() #afficher plusieurs images à la fois, "rafraîchir" l'écran pour voir les changements effectués depuis le dernier rafraîchissement

continuer = 1

f = open("lettre.jpg")
#Boucle infinie
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print ("ok")
                cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre
                fenetre.blit(cellule, (0,0))
                pygame.display.flip()
