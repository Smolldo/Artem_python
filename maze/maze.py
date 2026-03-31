import pygame
import random

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 100
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self, surface):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls[0]:
            pygame.draw.line(surface, WHITE, (x, y), (x + CELL_SIZE, y), 2)
        if self.walls[1]:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls[2]:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE), 2)
        if self.walls[3]:
            pygame.draw.line(surface, WHITE, (x, y + CELL_SIZE), (x, y), 2)


def generate_maze():
    grid = [[Cell(x, y) for y in range(ROWS)] for x in range(COLS)]
    stack = []
    current = grid[0][0]
    current.visited = True

    while True:
        neighbors = []
        x, y = current.x, current.y
        if y > 0 and not grid[x][y - 1].visited:
            neighbors.append( grid[x][y - 1])    
        if x < COLS - 1 and not grid[x+1][y].visited:
            neighbors.append(grid[x+1][y])    
        if y < ROWS - 1 and not grid[x][y + 1].visited:
            neighbors.append(grid[x][y + 1])
        if x > 0 and not grid[x - 1][y].visited:
            neighbors.append(grid[x - 1][y])

        if neighbors:
            next_cell = random.choice(neighbors)

            dx = next_cell.x - current.x
            dy = next_cell.y - current.y

            if dx == 1:
                current.walls[1] = False
                next_cell.walls[3] = False
            elif dx == -1:
                current.walls[3] = False
                next_cell.walls[1] = False
            elif dy == 1:
                current.walls[2] = False
                next_cell.walls[0] = False
            elif dy == -1:
                current.walls[0] = False
                next_cell.walls[2] = False


            stack.append(current)
            current = next_cell
            current.visited = True
        elif stack:
            current = stack.pop()
        else:
            break
    return grid


def reset_game():
    maze = generate_maze()
    player_x, player_y = 0, 0
    finish_x, finish_y = COLS - 1, ROWS - 1

    
    keys = []
    for _ in range(3):
        x = random.randint(0, COLS -1)
        y = random.randint(0, ROWS -1)
        if (x, y) != (0, 0) and (x, y) != (finish_x, finish_y):
            keys.append((x, y))

    visited_cells = set()
    score = 0

    return maze, player_x, player_y, finish_x, finish_y, visited_cells, keys, score

maze, player_x, player_y, finish_x, finish_y, visited_cells, keys, score = reset_game()


maze = generate_maze()

player_x, player_y = 0, 0
finish_x, finish_y = COLS - 1, ROWS - 1
font = pygame.font.SysFont('Arial', 24)


running = True

while running:
    screen.fill(BLACK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            cell = maze[player_x][player_y]
            if e.key == pygame.K_UP and not cell.walls[0]:
                player_y -= 1
            if e.key == pygame.K_RIGHT and not cell.walls[1]:
                player_x += 1
            if e.key == pygame.K_DOWN and not cell.walls[2]:
                player_y += 1
            if e.key == pygame.K_LEFT and not cell.walls[3]:
                player_x -= 1
            
    if (player_x, player_y) in keys:
        keys.remove((player_x, player_y))
        score +=1

    for col in maze:
        for cell in col:
            cell.draw(screen)

    # Гравець
    pygame.draw.rect(screen, RED, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Фініш
    pygame.draw.rect(screen, GREEN, (finish_x * CELL_SIZE, finish_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for kx, ky in keys:
        pygame.draw.circle(screen, GREEN,
                    (kx * CELL_SIZE + CELL_SIZE // 2,
                    kx * CELL_SIZE + CELL_SIZE // 2), 10)

    if player_x == finish_x and player_y == finish_y:
        win_text = font.render('U WIN', True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        maze, player_x, player_y, finish_x, finish_y, visited_cells, keys, score = reset_game()

    pygame.display.flip()


pygame.quit()