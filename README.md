# Graph Pathfinding Visualizer

## Description
This project is a graphical user interface (GUI) application developed using Pygame to visualize Dijkstra's Algorithm for finding the shortest path between nodes in a graph. Users can interactively create nodes, connect them with edges, and visualize the pathfinding process.

## Features
- **Node Placement**: Click to place nodes.
- **Node Connection**: Right-click to create edges between nodes.
- **Pathfinding**: Double-click on two nodes to visualize the shortest path.
- **Node Deletion**: Press space and click to delete a node.
- **Graph Reset**: Middle click to reset the graph.

## Visual Demonstrations
- **Placing and Connecting Nodes**
  
  ![Initial Setup](https://github.com/colingalbraith/Dijkstra-Path/assets/146497900/d27a0d57-d2d5-4eec-82af-60cf28bb678c)
  
- **Finding Shortest Path**
  
  ![Pathfinding Example](https://github.com/colingalbraith/Dijkstra-Path/assets/146497900/eb4ac8dd-9fca-4a40-b879-7a6acc11fdb6)
  
- **Complex Graph Configuration**
  ![Complex Graph](https://github.com/colingalbraith/Dijkstra-Path/assets/146497900/3d489c92-fcd7-4594-a8c6-4d305e0fa3ec)
- **Solved Path in a Complex Graph**
  ![Solved Complex Path](https://github.com/colingalbraith/Dijkstra-Path/assets/146497900/6795806f-4c5b-4e86-8469-e871c010ef62)
- **Simple Pathfinding Example**
  ![Simple Solved Path](https://github.com/colingalbraith/Dijkstra-Path/assets/146497900/32aa0d89-f111-423a-aa85-0cea8e06fc3b)

## Mathematical Overview of Dijkstra's Algorithm

### Overview
Dijkstra's Algorithm is a robust graph-searching method used to compute the shortest paths from a source node to all other nodes in a graph with non-negative edge weights. This implementation visualizes the algorithm in an interactive GUI, allowing users to directly manipulate the graph and observe the algorithm's step-by-step execution.

### Theoretical Foundations
**Notation and Definitions:**
- **Graph Representation**: Let \( G = (V, E) \) denote the graph where \( V \) represents vertices (nodes) and \( E \) represents edges.
- **Edge Weights**: Each edge \( (u, v) \) in \( E \) has an associated non-negative weight \( w(u, v) \), representing the cost or distance between the nodes.
- **Distance Metric**: \( d(v) \) indicates the shortest known distance from the source node \( s \) to vertex \( v \).
- **Predecessor Nodes**: \( \pi(v) \) denotes the predecessor of \( v \) in the shortest path from \( s \).

### Algorithm Steps in the Visualizer:
1. **Priority Queue Usage**: The visualizer uses a priority queue to efficiently manage the nodes, always processing the node with the lowest distance.
2. **Relaxation Process**:
   - For each node \( u \) processed, the algorithm examines each adjacent node \( v \) connected by edge \( (u, v) \).
   - If a shorter path is found through \( u \), \( d(v) \) is updated and \( \pi(v) \) is set to \( u \), visually demonstrating the path's progression.
3. **Visualization and Interaction**:
   - Users can dynamically add, delete, and connect nodes and edges, while the algorithm updates the paths in real time.

## Installation

### Prerequisites
- Python 3.8 or above
- Pygame
- Numpy

### Setup
Clone the repository and install the required packages:
```bash
git clone https://github.com/your-username/Dijkstra-Path.git
cd Dijkstra-Path
pip install pygame numpy
