import pygame
from grid import make_grid, get_clicked_position, draw
from algorithm import algorithm_astar


dimension = 500

window = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("A* Python Pathfinding")


def main(win, width):
    rows = dimension // 10
    grid = make_grid(rows, width)

    # Start and end positions
    start = None
    end = None

    # If mainloop has run or not
    run = True

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

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
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for tile in row:
                            tile.update_neighbors(grid)
                    
                    algorithm_astar(lambda: draw(win, grid, rows, width), grid, start, end)

            
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)
    pygame.quit()

main(window, dimension)