import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((900,700))


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
frames = []
color_index = 0
frame_index = 0
x = 0
y = 300
speed = 5
animation_speed = 150
last_update = pygame.time.get_ticks()
clock = pygame.time.Clock()
fps = 60

# MOVE_EVENT = pygame.USEREVENT + 1
ANIMATION_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(MOVE_EVENT, 500)
pygame.time.set_timer(ANIMATION_EVENT, 200)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif e.type == MOVE_EVENT:
        #     x += speed
        #     if x > 900:
        #         x = -50
        # elif e.type == ANIMATION_EVENT:
        #     color_index = (color_index + 1) % len(colors)

        x += speed
        if x > 900:
            x = -50
        current_time = pygame.time.get_ticks()
        if current_time - last_update > animation_speed:
            last_update = current_time
            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0


    screen.fill(WHITE)
    pygame.draw.rect(screen, colors[color_index], (x, y, 50, 50))
    # x += speed
    # if x > 900:
    #     x = -50


    pygame.display.flip()
    clock.tick(fps)