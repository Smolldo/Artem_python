import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('Arial', 22)


hp = 100
turn = 0
max_turns = 6

locations = [
    'темному лісі',
    'забутій печері',
    'покинутому місті',
    'старому храмі'
]

enemies = ["вовк", "бандит", "ельф", "монстр"]
loot = ['золото', 'меч', 'зілля', 'артефакт']
events = ["ти почув дивний звук", "земля затрусилась", "щось рухається в темряві", 'виник спалах світла']

current_scene = {}

def generate_scene():
    scene_type = random.choice(['enemy', 'loot', 'event'])

    if scene_type == 'enemy':
        enemy = random.choice(enemies)
        return {
            'text': f'перед тобою {enemy}. що робиш?',
            'options': ['Атакувати', 'Втекти', 'Захищатися'],
            'effects': [-20, -5, -10]
        }
    elif scene_type == 'loot':
        item = random.choice(loot)
        return {
            'text': f'ти знайшов {item}. що робиш?',
            'options': ['Взяти', 'Ігнорувати', 'Перевірити'],
            'effects': [0, 5, 10]
        }
    else:
        e = random.choice(events)
        return {
            'text': f'{e}. Що робиш',
            'options': ['Йти далі', 'Перевірити', 'Сховатися'],
            'effects': [0, -5, -10]
        }
    

def draw_text(text, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        img = font.render(line, True, (255,255,255))
        screen.blit(img, (x, y + i * 25))

current_scene = generate_scene()

running = True

while running:
    screen.fill((0,0,0))

    draw_text(f'HP: {hp}', 10, 10)
    draw_text(current_scene['text'], 10, 50)

    for i, opt in enumerate(current_scene['options']):
        draw_text(f'{i+1}. {opt}', 10, 200 + i * 30)

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                running = False
            
            if e.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                choice = int(e.unicode) - 1

                hp += current_scene['effects'][choice]

                turn += 1

                current_scene = generate_scene()

                if hp <= 0:
                    current_scene = {
                        'text': 'Ти програв',
                        'options': ['-', '-', '-'],
                        'effects': [0, 0, 0]
                    }

                elif turn >= max_turns:
                    current_scene = {
                        'text': 'Ти Переміг',
                        'options': ['-', '-', '-'],
                        'effects': [0, 0, 0]
                    }
                
pygame.quit()
sys.exit()

                

