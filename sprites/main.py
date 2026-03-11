import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
# sprite_image = pygame.image.load('Sonic-0.png')

sonic = pygame.image.load('Sonic-1.png')
sonic1 = pygame.image.load('Sonic-0.png')
scaled = pygame.transform.scale(sonic, (50, 50))
scaled1 = pygame.transform.scale(sonic1, (50, 50))
sprite_images = [
        scaled1,
        scaled
        ]


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = sprite_image
#         self.rect = self.image.get_rect()
#         self.rect.center = (640, 360)

#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= 5
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += 5
#         if keys[pygame.K_UP]:
#             self.rect.y -= 5
#         if keys[pygame.K_DOWN]:
#             self.rect.y += 5


# player = Player()
# all_sprites.add(player)


class Animated(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.images = sprite_images
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)
        self.animation_speed = 1
        self.time = 1

    def update(self):
        self.time += self.animation_speed
        if self.time >= len(self.images):
            self.time = 0
        self.current_image = int(self.time)
        self.image = self.images[self.current_image]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1

all_sprites = pygame.sprite.Group()
animated = Animated()
all_sprites.add(animated)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255,255,255))

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()

    


    