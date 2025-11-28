import random
import pygame

pygame.init()
WIDTH, HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Screen Saver")
x, y = random.randint(100, WIDTH - 100), random.randint(55, HEIGHT - 55)
x_direction, y_direction = 1, 1
clock = pygame.time.Clock()
running = True

logo = pygame.image.load("dvd_logo.png").convert_alpha()
logoRect = logo.get_frect(center = (68, 78))

color_filter = pygame.Surface((WIDTH, HEIGHT))
#color_filter.fill(rgba(255, 255, 255, 150))


def colorChanger(surf):
    red, green, blue = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    surf.fill(rgba(red, green, blue, 150))

while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT :
            running = False
            
    screen.fill("black")

    logoRect.x += 1 * x_direction
    if logoRect.x < 0 or logoRect.x > WIDTH - 100 :
        x_direction *= -1
    logoRect.y += 1 * y_direction
    if logoRect.y < 0 or logoRect.y > HEIGHT - 55 :
        y_direction *= -1

    screen.blit(logo, logoRect)
    
    
    pygame.display.update()
pygame.quit()