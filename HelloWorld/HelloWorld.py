import pygame
import lib_Circle

# Cette fonction c'est juste pour le fun !!
def eratosthene(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

# On dit bonjour, c'est toujours plus poli !
print("")
print("Hello World !")
print("")

# Calcule les nombres premier jusque 250 et affiche les 50 premiers de la liste
nombres_premiers = eratosthene(250)
print(nombres_premiers[:50])

#Initilisation de PyGame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Créer la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

circle = lib_Circle.Cercle(0,0,50,255,0,0)
circle_player = lib_Circle.Cercle(screen_width // 2,screen_height // 2,50,255,255,0)


# Définir la vitesse de déplacement du cercle
circle_player_speed = 5

# Boucle principale du programme
running = True

clock = pygame.time.Clock()
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 # Déplacement du cercle avec les touches curseurs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_player.x -= circle_player_speed
    if keys[pygame.K_RIGHT]:
        circle_player.x += circle_player_speed
    if keys[pygame.K_UP]:
        circle_player.y -= circle_player_speed
    if keys[pygame.K_DOWN]:
        circle_player.y += circle_player_speed

    # Effacer l'écran
    screen.fill((255, 255, 255))  # Blanc

    # Dessiner le cercle
    circle_player.show(screen)
    circle.show(screen)

    # Rafraîchir l'écran
    pygame.display.flip()
    circle.x = circle.x + 1
    circle.y = circle.y + 1

    if circle.x > 800:
        circle.x = 0
    if circle.y > 600:
        circle.y = 0

    clock.tick(60)
    
# Quitter Pygame
pygame.quit()