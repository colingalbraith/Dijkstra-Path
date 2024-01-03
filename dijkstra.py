import pygame
import numpy as np
import math
import sys
from collections import deque

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graph Pathfinding")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Graph representation
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, position):
        self.nodes.append(position)
        self.edges[position] = []

    def add_edge(self, node1, node2):
        if node1 != node2 and node2 not in self.edges[node1]:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            for key in self.edges:
                if node in self.edges[key]:
                    self.edges[key].remove(node)
            self.edges.pop(node, None)

    def reset_graph(self):
        self.nodes = []
        self.edges = {}

    def draw(self, screen, path=[]):
        # Draw edges
        for node, edges in self.edges.items():
            for edge in edges:
                color = GREEN if (node, edge) in path or (edge, node) in path else WHITE
                pygame.draw.line(screen, color, node, edge, 3)

        # Draw nodes
        for node in self.nodes:
            color = GREEN if node in path else RED
            pygame.draw.circle(screen, color, node, 7)


def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    nodes = graph.nodes.copy()

    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)

        if distances[current_node] == float('infinity'):
            break

        for neighbor in graph.edges[current_node]:
            new_distance = distances[current_node] + 1  # Assuming all edges have the same weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        if current_node == end:
            break

    path = deque()
    current_node = end
    while previous_nodes[current_node] is not None:
        path.appendleft((previous_nodes[current_node], current_node))
        current_node = previous_nodes[current_node]

    return list(path)


def get_node_at_pos(pos, nodes):
    for node in nodes:
        if math.sqrt((node[0] - pos[0]) ** 2 + (node[1] - pos[1]) ** 2) < 10:
            return node
    return None


def calculate_shortest_path(graph, selected_nodes):
    if len(selected_nodes) == 2:
        return dijkstra(graph, selected_nodes[0], selected_nodes[1])
    return []


def main():
    running = True
    selected_nodes = []
    dragging_node = None 
    last_click_time = 0
    shortest_path = []
    graph = Graph()

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                node = get_node_at_pos(pos, graph.nodes)

                if event.button == 1:  # Left click
                    if node:
                        if current_time - last_click_time < 300:  # Double click detected
                            if node not in selected_nodes:
                                selected_nodes.append(node)
                                if len(selected_nodes) == 2:
                                    shortest_path = dijkstra(graph, selected_nodes[0], selected_nodes[1])
                                    selected_nodes.clear()
                        else:
                            # Start dragging the node
                            dragging_node = node
                    else:
                        graph.add_node(pos)
                    last_click_time = current_time

                elif event.button == 3:  # Right click
                    if node:
                        if len(selected_nodes) == 1:
                            graph.add_edge(selected_nodes[0], node)
                            selected_nodes.clear()
                        else:
                            selected_nodes = [node]

                elif event.button == 2:  # Middle click (reset)
                    graph.reset_graph()
                    shortest_path.clear()

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # Stop dragging the node
                dragging_node = None


            elif event.type == pygame.MOUSEMOTION:

                # Update the position of the node being dragged

                if dragging_node:

                    index = graph.nodes.index(dragging_node)

                    graph.nodes[index] = event.pos

                    for edge in graph.edges[dragging_node]:
                        graph.edges[edge].remove(dragging_node)

                        graph.edges[edge].append(event.pos)

                    graph.edges[event.pos] = graph.edges.pop(dragging_node)

                    dragging_node = event.pos

                    # Recalculate the shortest path if two nodes are selected

                    shortest_path = calculate_shortest_path(graph, selected_nodes)

            # Check for space key and mouse click for node removal
            if pygame.key.get_pressed()[pygame.K_SPACE] and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                node = get_node_at_pos(pos, graph.nodes)
                if node:
                    graph.remove_node(node)
                    shortest_path.clear()

        # Update the display
        screen.fill(BLACK)
        graph.draw(screen, shortest_path)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
