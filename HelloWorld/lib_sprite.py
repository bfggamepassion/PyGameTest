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
        self.action_end_loop = 0                # Action en fin d'animation :
                                                #    0 - Boucle ou pas selon anim_loop
                                                #    1 - Désactive le Lutin
        def affiche_lutin(screen):              # 

        def maj_lutins():                       # Met a jour les animations de lutin