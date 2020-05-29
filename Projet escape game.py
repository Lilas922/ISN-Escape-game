import pygame

from pygame.locals import *   #importer les constantes de Pygame

pygame.init()        #initialise tous les modules

fenetre = pygame.display.set_mode(( 800 , 800 )) ## affichage fenêtre pygame 405 largeur/hauteur_grille * largeur/hauteur image

cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

fenetre.blit(cellule, (0,0))

lettre = pygame.image.load("lettre.png").convert()    ## image lettre

fenetre.blit(lettre, (104,56))

pygame.display.flip() #afficher plusieurs images à la fois, "rafraîchir" l'écran pour voir les changements effectués depuis le dernier rafraîchissement

continuer = 1

f = open("lettre.png")

robinet = pygame.Rect((375, 355), (35, 40))
rect_surf = pygame.Surface(robinet.size)

tiroire1 = pygame.Rect((256, 457), (65, 40))
rect_surf = pygame.Surface(tiroire1.size)

tiroire2 = pygame.Rect((256, 497), (65, 40))
rect_surf = pygame.Surface(tiroire2.size)

tiroire3 = pygame.Rect((256,527), (65, 40))
rect_surf = pygame.Surface(tiroire3.size)

 tiroire4 = pygame.Rect((256,557), (65, 40))
rect_surf = pygame.Surface(tiroire4.size)

#tiroireG = pygame.Rect((140, 472), (115, 45))
#rect_surf = pygame.Suface(tiroireG.size)

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
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m1 = pygame.image.load("m1.png").convert()

                            fenetre.blit(m1, (300,190))

                            pygame.display.flip()
                            
                            if event.type == KEYDOWN:

                                if event.key == K_SPACE:

                                    print ("ok")

                                    cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                                    fenetre.blit(cellule, (0,0))
                                
                                    pygame.display.flip()
                                
                                         
                if tiroire1.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroire1")
                                                                            
                    tiroire = pygame.image.load("tiroire.jpg").convert()
                                                                            
                    fenetre.blit(tiroire, (250, 250))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.png").convert()

                            fenetre.blit(m2, (200,150))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroire2.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroire2")
                                                                            
                    tiroire = pygame.image.load("tiroire.jpg").convert()
                                                                            
                    fenetre.blit(tiroire, (300, 300))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.png").convert()

                            fenetre.blit(m2, (250,200))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroire3.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroire3")
                                                                            
                    tiroire = pygame.image.load("tiroire.jpg").convert()
                                                                            
                    fenetre.blit(tiroire, (350, 350))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.png").convert()

                            fenetre.blit(m2, (300,250))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroire4.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroire4")
                                                                            
                    tiroire = pygame.image.load("tiroire.jpg").convert()
                                                                            
                    fenetre.blit(tiroire, (400, 400))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.png").convert()

                            fenetre.blit(m2, (350,300))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()

                            
#J'ai avancé un peu mais la je dois m'arreter j'ai des trucs a faire je reviens...                          
