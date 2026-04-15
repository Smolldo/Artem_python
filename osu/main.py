import pygame
import random
import sys
import time

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OSU Lite")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
BLUE = (80, 80, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)


notes = []
score = 0
combo = 0

spawn_interval = .8
last_spawn = time.time()


class Note:
    def __init__(self, hold = False):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)

        self.base_radius = 50
        self.radius = self.base_radius

        self.spawn_time = time.time()
        self.lifetime = 1.2

        self.hold = hold
        self.hold_time = .8
        self.holding = False
        self.hold_start = 0

    def update(self):
        elapsed = time.time() - self.spawn_time
        progress = elapsed / self.lifetime

        self.radius = int(self.base_radius * (1 - progress))
        if self.radius < 10:
            self.radius = 10

    def draw(self):
        color = BLUE if self.hold else RED
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius, 3)

        pygame.draw.circle(screen, WHITE, (self.x, self.y), 5)


    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx * dx + dy * dy <= self.radius * self.radius
    

running = True
while running:
    screen.fill(BLACK)
    now = time.time()

    if now - last_spawn > spawn_interval:
        hold = random.random() < .25
        notes.append(Note(hold))
        last_spawn = now

        spawn_interval *= .98
        if spawn_interval < .3:
            spawn_interval = .3
    
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    for note in notes:
        note.update()

        if now - note.spawn_time > note.lifetime:
            notes.remove(note)
            combo = 0
            continue

        if not note.hold:
            if mouse_pressed and note.is_clicked(mouse_pos):
                score += 10 + combo
                combo += 1
                notes.remove(note)

        else:
            if mouse_pressed and note.is_clicked(mouse_pos):
                if not note.holding:
                    note.holding = True
                    note.hold_start = now

                if now - note.hold_start >= note.hold_time:
                    score += 20 + combo
                    notes.remove(note)
            else:
                if note.holding:
                    combo = 0
                    notes.remove(note)

    for note in notes:
        note.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    combo_text = font.render(f"Combo: {combo}", True, GREEN)

    screen.blit(score_text, (10, 10))
    screen.blit(combo_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()