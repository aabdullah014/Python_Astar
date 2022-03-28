import pygame
import math
from queue import PriorityQueue

dimension = 800

window = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("A* Python Pathfinding")


def main(win, width):
    rows = 80