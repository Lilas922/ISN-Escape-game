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

robinet = pygame.Rect((375, 355), (35, 40))
rect_surf = pygame.Surface(robinet.size)

tiroir1 = pygame.Rect((256, 457), (65, 40))
rect_surf = pygame.Surface(tiroir1.size)

tiroir2 = pygame.Rect((256, 497), (65, 40))
rect_surf = pygame.Surface(tiroir2.size)

tiroir3 = pygame.Rect((256,527), (65, 40))
rect_surf = pygame.Surface(tiroir3.size)

tiroir4 = pygame.Rect((256,557), (65, 40))
rect_surf = pygame.Surface(tiroir4.size)

tiroirG = pygame.Rect((136, 460), (117, 56))
rect_surf = pygame.Surface(tiroirG.size)


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
                
                            m1 = pygame.image.load("m1.jpg").convert()

                            fenetre.blit(m1, (300,190))

                            pygame.display.flip()
                            
                            if event.type == KEYDOWN:

                                if event.key == K_SPACE:

                                    print ("ok")

                                    cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                                    fenetre.blit(cellule, (0,0))
                                
                                    pygame.display.flip()
                                    
                                    if tiroirG.collidepoint(event.pos) :
                                                                            
                                        print ("ok tiroirG")
                                                                            
                                        tiroir = pygame.image.load("tiroir.jpg").convert()
                                                                            
                                        fenetre.blit(tiroir, (250, 250))
                                                                            
                                        pygame.display.flip()
                    
                                        if event.type == MOUSEBUTTONDOWN:

                                            if event.button == 1: # 1= clique gauche
                
                                                m2 = pygame.image.load("enigme.jpg").convert()

                                                fenetre.blit(m2, (200,150))

                                                pygame.display.flip()
                                                                            
                                                if event.type == KEYDOWN:

                                                    if event.key == K_SPACE:

                                                        print ("ok")

                                                        cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                                                        fenetre.blit(cellule, (0,0))
                                                                                        
                                                        pygame.display.flip()
                                
                                         
                if tiroir1.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroir1")
                                                                            
                    tiroir = pygame.image.load("tiroir.jpg").convert()
                                                                            
                    fenetre.blit(tiroir, (250, 250))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.jpg").convert()

                            fenetre.blit(m2, (200,150))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroir2.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroir2")
                                                                            
                    tiroir = pygame.image.load("tiroir.jpg").convert()
                                                                            
                    fenetre.blit(tiroir, (300, 300))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.jpg").convert()

                            fenetre.blit(m2, (250,200))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroir3.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroir3")
                                                                            
                    tiroir = pygame.image.load("tiroir.jpg").convert()
                                                                            
                    fenetre.blit(tiroir, (350, 350))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.jpg").convert()

                            fenetre.blit(m2, (300,250))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()
                            
                
                if tiroir4.collidepoint(event.pos) :
                                                                            
                    print ("ok tiroir4")
                                                                            
                    tiroir = pygame.image.load("tiroir.jpg").convert()
                                                                            
                    fenetre.blit(tiroir, (400, 400))
                                                                            
                    pygame.display.flip()
                    
                    if event.type == MOUSEBUTTONDOWN:

                        if event.button == 1: # 1= clique gauche
                
                            m2 = pygame.image.load("m2.jpg").convert()

                            fenetre.blit(m2, (350,300))

                            pygame.display.flip()
                                                                            
                    if event.type == KEYDOWN:

                        if event.key == K_SPACE:

                            print ("ok")

                            cellule = pygame.image.load("cellule800.jpg").convert()  #.convert = conversion de l'image au format de la fenêtre

                            fenetre.blit(cellule, (0,0))
                                                                                        
                            pygame.display.flip()

