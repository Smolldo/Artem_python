import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

square = pygame.Rect(350, 250, 100, 100)
# dragging = False
color = (0, 128, 255)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # mouse_pos = pygame.mouse.get_pos()
    # mouse_buttons = pygame.mouse.get_pressed()

    # if mouse_buttons[0]:
    #     print('LKM pressed')
    # if mouse_buttons[2]:
    #     print('pkm pressed')

        # elif e.type == pygame.MOUSEBUTTONDOWN:
        #     if e.button == 1:
        #         print('LKM pressed')
        #     elif e.button == 3:
        #         print('PKM pressed')
        #     elif e.button == 2:
        #         print('SKM pressed')
        # elif e.type == pygame.MOUSEMOTION:
        #     mouse_pos = e.pos
        #     print(f'mouse po: {mouse_pos}')
        # elif e.type == pygame.MOUSEBUTTONUP:
        #     if e.button == 1:
        #         print('LKM unpressed')

        #Для гри перетягування квадрата
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(e.pos):
                # dragging = True
                # mouse_x, mouse_y = e.pos
                # offset_x = square.x - mouse_x
                # offset_y = square.y - mouse_y
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        elif e.type == pygame.MOUSEBUTTONUP:
            # dragging = False
            color = (0, 128, 255)

        # elif e.type == pygame.MOUSEMOTION:
            # if dragging:
            #     mouse_x, mouse_y = e.pos
            #     square.x = mouse_x + offset_x
            #     square.y = mouse_y + offset_y
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                square.x -= 40
            elif e.key == pygame.K_RIGHT:
                square.x += 40
            elif e.key == pygame.K_DOWN:
                square.y += 40
            elif e.key == pygame.K_UP:
                square.y -=40
        

    screen.fill((255,255,255))
    pygame.draw.rect(screen, color, square)



    # font = pygame.font.Font(None, 36)
    # text_pos = font.render(f'Позиція мишки: {mouse_pos}', True, (0,0,0))
    # screen.blit(text_pos, (20,20))

    # text_buttons = font.render(f'LKM {'Натиснута' if mouse_buttons[0] else 'Не натиснута'}',
    #                            True, (0,0,0))
    # screen.blit(text_buttons, (20, 60))

    # text_buttons = font.render(f'PKM {'Натиснута' if mouse_buttons[2] else 'Не натиснута'}',
    #                            True, (0,0,0))
    # screen.blit(text_buttons, (20, 100))




    pygame.display.flip()

pygame.quit()