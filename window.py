import pygame
from tile import Tile


# Size of window
(width, height) = (800, 800)
default_color = (200,200,200)

class Maze:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.flip()   
        self.running = True
        pygame.display.set_caption('A* Pathfinding')
        background_colour = (255,255,255)
        screen.fill(background_colour)


    def populateScreen():
        size = 20
        x_coord = 0
        y_coord = 0

        for x in range(width/size):
            tile = Tile(default_color, (size, size))
            tiles = pygame.surface(20)
            tiles.blit((0,0), (x, x, size))

            


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

maze = Maze()
maze.run()