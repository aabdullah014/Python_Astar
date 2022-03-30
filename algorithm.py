from queue import PriorityQueue
from heuristic import h
from grid import reconstruct_path
import pygame

def algorithm_astar(draw, grid, start, end):
    count = 0

    # PriorityQueue is efficient way to get smallest element everytime
    open_set = PriorityQueue()

    # Add start node to open set
    open_set.put((0, count, start))

    # Keep track of what tiles/nodes came from where
    came_from = {}

    # Current shortest distance from start node to this node, float('inf) is infinity
    g_score = {tile: float("inf") for row in grid for tile in row}
    g_score[start] = 0

    # Distance from this node to end node
    f_score = {tile: float("inf") for row in grid for tile in row}

    # Approximate how far end node is from start node
    f_score[start] = h(start.get_position(), end.get_position())

    # Keep track of items in PriorityQueue, see if something is in open_set
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # 2 because we want node/tile
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # At the end
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        # Consider g and f score of all neighbors
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        # Already considered
        if current != start:
            current.make_checked()

    return False
