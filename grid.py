from tile import Tile
import pygame


white = (255, 255 ,255)
grey = (128, 128, 128)


def make_grid(rows, width):
    grid = []
    gap = width // rows

    for x in range(rows):
        grid.append([])
        for y in range(rows):
            tile = Tile(x, y, gap, rows, True)
            grid[x].append(tile)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    
    for x in range(rows):
        pygame.draw.line(win, grey, (0, x*gap), (width, x*gap))
        for y in range(rows):
            pygame.draw.line(win, grey, (y*gap, 0), (y*gap, width))

def draw(win, grid, rows, width):
    win.fill(white)

    for row in grid:
        for tile in row:
            tile.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_position(pos, rows, width):
    gap = width // rows
    x,y = pos

    row = x // gap
    col = y // gap

    return row, col

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()