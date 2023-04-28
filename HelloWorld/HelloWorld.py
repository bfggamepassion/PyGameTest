import pygame

def eratosthene(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

print("")
print("Hello World !")
print("")

nombres_premiers = eratosthene(250)
print(nombres_premiers[:50])

pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Créer la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

# Définir les coordonnées du cercle
#circle_x = screen_width // 2
#circle_y = screen_height // 2
circle_x = 0
circle_y = 0

circle_radius = 50

# Définir la couleur du cercle
circle_color = (255, 0, 0)  # Rouge

# Boucle principale du programme
running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill((255, 255, 255))  # Blanc

    # Dessiner le cercle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Rafraîchir l'écran
    pygame.display.flip()
    circle_x = circle_x + 1
    circle_y = circle_y + 1

    if circle_x > 800:
        circle_x = 0
    if circle_y > 600:
        circle_y = 0

# Quitter Pygame
pygame.quit()