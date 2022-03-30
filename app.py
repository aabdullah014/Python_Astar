import pygame
import math
from grid import make_grid, get_clicked_position, draw
from algorithm import algorithm_astar


dimension = 900

window = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("A* Python Pathfinding")


def main(win, width):
    rows = dimension // 10
    grid = make_grid(rows, width)

    # Start and end positions
    start = None
    end = None

    # If mainloop has run or not, and if algorithm has started or not
    run = True
    started = False

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Once algorithm started, user should not be able to change anything
            if started:
                continue

            # Check for LMB click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, rows, width)

                tile = grid[row][col]

                if not start and tile != end:
                    start = tile
                    start.make_start()
                elif not end and tile != start:
                    end = tile
                    end.make_end()
                elif tile != start and tile != end:
                    tile.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, rows, width)

                tile = grid[row][col]

                tile.reset()

                if tile == start:
                    start = None
                
                if tile == end:
                    end = None
            
            # Start algorithm when space key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for tile in row:
                            tile.update_neighbors(grid)
                        algorithm_astar(lambda: draw(win, grid, rows, width), grid, start, end)
    pygame.quit()

main(window, dimension)