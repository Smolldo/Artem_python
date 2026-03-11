import pygame
import time

pygame.init()

pygame.display.set_caption('My first game')

screen = pygame.display.set_mode([800, 600])
icon = pygame.image.load('pygame1/chest.png')

pygame.display.set_icon(icon)




# font = pygame.font.Font(None, 36)
# text = font.render('Привіт, геймери!', True, (0,255,0))
# screen.blit(text, (50, 50))
# pygame.display.flip()


running = True
x_position = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.draw.line(screen, (0,0,0), (100, 100), (400, 400), 5)
    # pygame.draw.polygon(screen, (0,0,0), [(100,100), (200,100), (150, 200)], 1)
    # pygame.display.flip()
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), (x_position, 300, 50, 50))
    pygame.display.flip()

    x_position += 5
    if x_position > 800:
        x_position = 0

    pygame.time.delay(50)

pygame.quit()