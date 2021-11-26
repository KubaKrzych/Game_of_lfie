import time
from random import randint
from Grid import Grid
import pygame

# GRID OBJECT
width = int(input('Width: '))
length = int(input('Length: '))
grid = Grid(width, length)
grid.randomizer()

# SETTINGS
pygame.init()
screen = pygame.display.set_mode(size=(width * 24, length * 24))
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('freesansbold.ttf', 24)
running = True

# GAME LOOP
while running:
    time.sleep(0.05) # You can change the fluidity using this value
    generation = str(grid.gen)
    img = font.render(generation, True, (255, 255, 255))
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pos = (pos[0] // 24, pos[1] // 24)
            grid[pos[0], pos[1]] = 1

    cords = grid.get_cords()
    grid.next_gen()
    # DRAWING CELLS ONTO SURFACE
    for pos in cords:
        pygame.draw.rect(surface=screen, color=(randint(0, 255), randint(0, 255), randint(0, 255)),
                         rect=(pos[0] * 24, pos[1] * 24, 24, 24), width=3, border_radius=4)

    screen.blit(img, (10, 10))
    pygame.display.update()
    # print(grid.gen)
