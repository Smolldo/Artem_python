import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

shoot_sound = pygame.mixer.Sound('shot.mp3')
explosion_sound = pygame.mixer.Sound('hit.mp3')

def load_image(path, scale):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, scale)

player_img = load_image('player.png', (80,100))
enemy_img = load_image('enemy.png', (70, 70))
bullet_img = load_image('bullet.png', (15, 10))
boss_img = load_image('enemy.png', (200, 250))


player = player_img.get_rect(center = (WIDTH//2, HEIGHT - 100))
player_speed = 7

lives = 3

bullets = []
enemies = []

boss = None
boss_hp = 30
boss_active = False
boss_speed = 5
boss_direction = 1

score =  0
font = pygame.font.SysFont('Arial', 40)


def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_img.get_width())
    rect = enemy_img.get_rect(topleft=(x, -70))
    return rect

running = True
while running:
    screen.fill((10, 10, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = bullet_img.get_rect(midbottom=player.midtop)
                bullets.append(bullet)
                shoot_sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    for bullet in bullets:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)


    if not boss_active:
        if random.randint(1, 25) == 1:
            enemies.append(spawn_enemy())

    for enemy in enemies:
        enemy.y += 4
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                explosion_sound.play()
                score += 1
                break

    for enemy in enemies:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            lives -= 1
            explosion_sound.play()


    if score >= 30 and not boss_active:
        boss = boss_img.get_rect(center=(WIDTH//2, -250))
        boss_active = True

    if boss_active:
        if boss.y < 5:
            boss.y += 2

        else:
            boss.x += boss_speed * boss_direction

            if boss.left <= 0 or boss.right >= WIDTH:
                boss_direction *= -1

    
        for bullet in bullets:
            if boss.colliderect(bullet):
                bullets.remove(bullet)
                boss_hp -=1
                explosion_sound.play()

        if player.colliderect(boss):
            lives -= 1
            explosion_sound.play()

            if lives <= 0:
                print("GAME OVER")
                pygame.quit()
                sys.exit()

        if boss_hp <= 0:
            print('You WIN')
            pygame.quit()
            sys.exit()

    screen.blit(player_img, player)

    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    if boss_active:
        screen.blit(boss_img, boss)

        hp_text = font.render(f'Boss HP: {boss_hp}', True, (255,  98, 45))
        screen.blit(hp_text, (WIDTH//2 -100, 10))

    score_text = font.render(f'SCore: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))

    screen.blit(score_text, (15,15))
    screen.blit(lives_text, (15, 55))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()