from sre_parse import WHITESPACE
from string import whitespace
import pygame


red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255 ,255)
black = (0, 0, 0)
purple = (160, 110, 20)
orange = (255, 165, 0)
grey = (128, 128, 128)
turquoise = (64, 225, 208)

class Tile:
    def __init__(self, row, col, width, total_rows, isClickable):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = white
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.isClickable = isClickable


    def is_clickable(self):
        return self.isClickable

    # Functions to check if tile is a certain type
    def get_position(self):
        return self.row, self.col

    def is_checked(self):
        return self.color == red

    def is_open(self):
        return self.color == turquoise

    def is_barrier(self):
        return self.color == black
    
    def is_start(self):
        return self.color == orange

    def is_end(self):
        return self.color == purple

    # Functions to make the tile a certain type
    def make_checked(self):
        self.color = red

    def make_open(self):
        self.color = turquoise

    def make_barrier(self):
        self.color = black
    
    def make_start(self):
        self.color = orange

    def make_end(self):
        self.color = purple

    def make_path(self):
        self.color = green

    def reset(self):
        self.color = white


    # Actually draw the tile, pygame starts drawing from top left
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors = []

        # Can you move down?
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        
        # Can you move up?
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        
        # Can you move right?
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        
        # Can you move left?
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    # Compares two tiles and says the other tiles is less than the current tile
    def __lt__(self, other):
        return False

    
