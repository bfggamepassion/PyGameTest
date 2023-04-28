import pygame

# Définir les dimensions de l'écran
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 192

# Définir la taille des images
IMAGE_SIZE = 8

# Définir le tableau d'indices d'images
image_indices = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 2, 2, 2, 2, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 0],
    [0, 1, 2, 2, 2, 2, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Initialiser Pygame
pygame.init()

# Créer la fenêtre d'affichage
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Charger les images
images = [
    pygame.image.load("image_0.png").convert(),
    pygame.image.load("image_1.png").convert(),
    pygame.image.load("image_2.png").convert(),
    pygame.image.load("image_3.png").convert(),
]

# Afficher les images au bon endroit
for i in range(len(image_indices)):
    for j in range(len(image_indices[i])):
        image_index = image_indices[i][j]
        image = images[image_index]
        x = j * IMAGE_SIZE
        y = i * IMAGE_SIZE
        screen.blit(image, (x, y))

# Rafraîchir l'affichage
pygame.display.flip()

# Attendre que l'utilisateur ferme la fenêtre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()