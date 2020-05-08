import pygame
from pygame.locals import *   #importer les constantes de Pygame
pygame.init()        #initialise tous les modules


fenetre = pygame.display.set_mode(( 800 , 800 )) ## affichage fenêtre pygame 405 largeur/hauteur_grille * largeur/hauteur image

cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre
fenetre.blit(cellule, (0,0))

import pygame
from pygame.locals import *   #importer les constantes de Pygame
pygame.init()        #initialise tous les modules


fenetre = pygame.display.set_mode(( 800 , 800 )) ## affichage fenêtre pygame 405 largeur/hauteur_grille * largeur/hauteur image

cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre
fenetre.blit(cellule, (0,0))

lettre = pygame.image.load("lettre.jpg").convert()    ## image lettre

fenetre.blit(lettre, (104,56))


pygame.display.flip() #afficher plusieurs images à la fois, "rafraîchir" l'écran pour voir les changements effectués depuis le dernier rafraîchissement

continuer = 1

f = open("lettre.jpg")

robinet = pygame.Rect((375, 355), (35, 40)) #première parenthèse pour le coin en haut à gauche de la zone de clic et deuxième parenthèse pour la taille de rectangle
rect_surf = pygame.Surface(robinet.size)

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
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # 1= clique gauche
                if robinet.collidepoint(event.pos):
                    print ("ok robinet")
                    clé = pygame.image.load("clé.jpg").convert()                
                    fenetre.blit(clé, (300,300))
                    pygame.display.flip()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            print ("ok")
                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre
                            fenetre.blit(cellule, (0,0))
                            pygame.display.flip()

# Il y aurait des petits trucs à modifier sur la lettre :
# - Il faudrait mettre que pour enlever des images qui apparaissent sur la fenêtre, il faut appuyer sur la touche espace
