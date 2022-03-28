from tile import Tile
from colors import grey, white
import pygame

def make_grid(rows, width):
    grid = []
    gap = width // rows

    for x in range(rows):
        grid.append([])
        for y in range(rows):
            tile = Tile(x, y, gap, rows)
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
            tile.draw(width)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_position(pos, rows, width):
    gap = width // rows
    x,y = pos

    row = x // gap
    col = y // gap

    return row, col