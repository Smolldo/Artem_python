import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('ds.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

shoot_sound = pygame.mixer.Sound('shot.mp3')
hit_sound = pygame.mixer.Sound('hit.mp3')
pygame.mixer.music.load('fon.mp3')

shoot_sound.set_volume(.4)
hit_sound.set_volume(.6)
pygame.mixer.music.set_volume(.1)


pygame.mixer.music.play(-1)

player = pygame.Rect(50, 150, 50, 50)
enemy = pygame.Rect(400, random.randint(0, 350), 50, 50)

speed = 2

running = True
while running:
    screen.fill((0,0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                shoot_sound.play()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed

    enemy.x -= 1


    if player.colliderect(enemy):
        hit_sound.play()
        enemy.x = WIDTH
        enemy.y = random.randint(0, 350)

    if enemy.x < 0:
        enemy.x = WIDTH
        enemy.y = random.randint(0, 350)

    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (0, 255 , 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    

    pygame.display.flip()

pygame.quit()