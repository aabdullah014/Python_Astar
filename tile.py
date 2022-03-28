from sre_parse import WHITESPACE
from string import whitespace
import pygame
import colors

class Tile:
    def __init__(self, row, col, width, total_rows, isClickable):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = colors.white
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
        return self.color == colors.red

    def is_open(self):
        return self.color == colors.green

    def is_barrier(self):
        return self.color == colors.black
    
    def is_start(self):
        return self.color == colors.orange

    def is_end(self):
        return self.color == colors.purple

    # Functions to make the tile a certain type
    def make_checked(self):
        self.color == colors.red

    def make_open(self):
        self.color == colors.green

    def make_barrier(self):
        self.color == colors.black
    
    def make_start(self):
        self.color == colors.orange

    def make_end(self):
        self.color == colors.purple

    def make_path(self):
        self.color = colors.turquoise

    def reset(self):
        self.color == colors.white


    # Actually draw the tile, pygame starts drawing from top left
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        

    
