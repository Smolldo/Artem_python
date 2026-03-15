import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))

player_img = pygame.image.load('minecraft_player.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 70))

pickaxe_img = pygame.image.load('pickaxe.png').convert_alpha()
pickaxe_img = pygame.transform.scale(pickaxe_img, (30, 30))

wood_img = pygame.image.load('planks.jpg')
wood_img = pygame.transform.scale(wood_img, (30, 30))

stone_img = pygame.image.load('stone.jpg')
stone_img = pygame.transform.scale(stone_img, (30, 30))

chest_img = pygame.image.load('chest.png').convert_alpha()
chest_img = pygame.transform.scale(chest_img, (30,30))

player = pygame.Rect(100,100, 50, 70)
chest = pygame.Rect(640, 360, 30, 30)
pickaxe = pygame.Rect(300, 150, 30, 30)
stone = pygame.Rect(600, 200, 30,30)
woods = [pygame.Rect(300,600,30,30), pygame.Rect(500,700,30,30)]

inventory = {'Pickaxe': 0, 'Wood': 0, 'Stone': 0}

chest_opened = False
has_pickaxe = False
item_collected = 0
clock = pygame.time.Clock()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -=5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_s]:
        player.y += 5
    if keys[pygame.K_w]:
        player.y -= 5

    if pickaxe and player.colliderect(pickaxe):
        if keys[pygame.K_e]:
            has_pickaxe = True
            inventory['Pickaxe'] = 1
            pickaxe = None

    if has_pickaxe:
        for wood in woods[:]:
            if player.colliderect(wood):
                if keys[pygame.K_SPACE]:
                    inventory['Wood'] += 1
    
    if has_pickaxe:
        if player.colliderect(stone):
            if keys[pygame.K_SPACE]:
                inventory['Stone'] += 1

    if inventory['Wood'] >= 50 and inventory['Stone'] >= 30 and player.colliderect(chest):
        print('U won!')
        running = False

    screen.fill((255,255,255))


    if chest_opened:
        screen.blit(chest_img, (chest.x, chest.y))
    else:
        screen.blit(chest_img, (chest.x, chest.y))


    if pickaxe:
        screen.blit(pickaxe_img, (pickaxe.x, pickaxe.y))

    for wood in woods[:]:
        screen.blit(wood_img, (wood.x, wood.y))

    screen.blit(player_img, (player.x, player.y))
    screen.blit(stone_img, (stone.x, stone.y))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Wood: {inventory['Wood']}", True, (0,0,0))
    screen.blit(text, (10,10))
    stone_text = font.render(f"Stone: {inventory['Stone']}", True, (0,0,0))
    screen.blit(stone_text,(10, 70))

    if has_pickaxe:
        pickaxe_text = font.render('Pickaxe: YES', True, (0,0,0))
    else:
        pickaxe_text = font.render('Pickaxe: NO', True, (0,0,0))
    screen.blit(pickaxe_text, (10, 50))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
