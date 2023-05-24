import pygame

class Lutin:
     def __init__(self):
        self.actif = False                      # Le sprite doit il être affiché ?
        self.pos_x = 0                          # Position x du sprite
        self.pos_y = 0                          # Position y du sprite
        self.col_x = 0                          # Position dans l'image du coin supérieur gauche du bloc de collision
        self.col_y = 0
        self.col_l = 0                          # Hauteur et largeur du bloc de collision
        self.col_h = 0
        self.frames[0,0,0,0,0,0,0,0,0,0,0,0]    # Index des images composants l'animaton
        self.nb_frames = 0                      # Nombre d'images composants l'animation
        self.frame_delay = 0                    # Temps de pause entre les images composants l'animation
        self.anim_loop = True                   # L'animation boucle t'elle ?
        self.action_end_loop = 0                # Action en fin d'animation : 0 - Boucle ou pas selon anim_loop / 1 - Désactive le Lutin
        self.current_frame=0
        self.inner_counter=0
        
        def affiche_lutin(screen,image_bank):   
            screen.blit(image_bank[self.frames[self.current_frame]], (self.pos_x, self.pos_y)) 

        def maj_lutins():                                    # Met a jour les animations de lutin
            if (self.inner_counter==self.frame_delay):       # delay atteint pour image suivante
                self.inner_counter = 0                       # remise du compteur a 0
                if (self.current_frame==self.nb_frames):     # on est à la dernière frame ?
                    if (self.anim_loop==True):               # doit on boucler ?
                        self.current_frame=0                 # si oui on boucle
                else:                                        # on est pas à la dernière frame
                    self.current_frame++                     # on passe alors à la suivante
            else:                                            # delay non atteind
                self.inner_counter++                         # on incrémente le compteur
                    