import copy
import time
from copy import deepcopy

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def make_adjacency(self):
        self.adjacency_matrix = {}
        for row, _ in enumerate(self.graph):
            for column, _ in enumerate(self.graph[row]):
                adj = {}
                for neighbor in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    # Don't let the world wrap around
                    if row + neighbor[0] < 0 or column + neighbor[1] < 0 or row + neighbor[0] >= len(self.graph) or column + neighbor[1] >= len(self.graph):
                        pass
                    else:
                        adj[(row+neighbor[0], column+neighbor[1])] = self.graph[row+neighbor[0]][column+neighbor[1]]
                self.adjacency_matrix[(row, column)] = adj

def Astar(grid, start, end):
    # List of visited nodes, whoes neighbors have not all been inspected
    open_list = set([start])
    # List of visited node, whoes neighbors have been inspected
    closed_list = set([])

    # Distance from start to all other nodes
    cost_to_node = {}
    cost_to_node[start] = grid.graph[start[0]][start[1]]

    # Adjacency mapping of all nodes
    adj_map = {}
    adj_map[start] = start

    while len(open_list) > 0:
        currentNode = None

        # Current node becomes the node with the lowest value f
        for item in open_list:
            if currentNode == None or cost_to_node[item] + grid.graph[item[0]][item[1]] < cost_to_node[currentNode] + grid.graph[currentNode[0]][currentNode[1]]:
                currentNode = item

        if currentNode == None:
            print("There is no path")
            return None

        if currentNode == end:
            path = []
            while adj_map[currentNode] != currentNode:
                path.append(currentNode)
                currentNode = adj_map[currentNode]

            total_cost = 0
            for step in path:
                total_cost += grid.graph[step[0]][step[1]]

            path.append(start)
            path.reverse()

            return path, total_cost

        # For all neighbors
        for (x, y) in grid.adjacency_matrix[currentNode]:
            weight = grid.adjacency_matrix[currentNode][(x, y)]
            if (x, y) not in open_list and (x, y) not in closed_list:
                open_list.add((x, y))
                adj_map[(x, y)] = currentNode
                cost_to_node[(x, y)] = cost_to_node[currentNode] + weight
            else:
                if cost_to_node[(x, y)] > cost_to_node[currentNode] + weight:
                    cost_to_node[(x, y)] = cost_to_node[currentNode] + weight
                    adj_map[(x, y)] = currentNode

                    if (x, y) in closed_list:
                        closed_list.remove((x, y))
                        open_list.add((x, y))

        open_list.remove(currentNode)
        closed_list.add(currentNode)

    print("There is no path")
    return None

def day15():
    start = time.time()

    with open('Day15_input.txt') as file:
        input_file = [line.strip() for line in file]

    testing = False
    if testing:
        input_file = [['1163751742'],['1381373672'],['2136511328'],
                      ['3694931569'],['7463417111'],['1319128137'],
                      ['1359912421'],['3125421639'],['1293138521'],
                      ['2311944581']]

    # Format the input file
    for line_index, line in enumerate(input_file):
        input_file[line_index] = [int(num) for sublist in line for num in sublist]

    grid = Graph(input_file)
    grid.make_adjacency()

    shortest_route = Astar(grid, (0,0), (len(grid.graph)-1, len(grid.graph[0])-1))

    print("The shortest route is:", shortest_route[0], "\nThe answer to part 1 is:", shortest_route[1])

    part2_grid = copy.deepcopy(input_file)
    # Make the grid 5x larger, first horizontally expand
    for i in range(1,5):
        to_be_added = copy.deepcopy(input_file)
        for row_index, _ in enumerate(to_be_added):
            for column_index, _ in enumerate(to_be_added[row_index]):
                to_be_added[row_index][column_index] += i
                if to_be_added[row_index][column_index] > 9:
                    to_be_added[row_index][column_index] -= 9
        for line, _ in enumerate(part2_grid):
            part2_grid[line].extend(to_be_added[line])

    part2_grid_copy = copy.deepcopy(part2_grid)

    for i in range(1,5):
        to_be_added = copy.deepcopy(part2_grid_copy)
        for row_index, _ in enumerate(to_be_added):
            for column_index, _ in enumerate(to_be_added[row_index]):
                to_be_added[row_index][column_index] += i
                if to_be_added[row_index][column_index] > 9:
                    to_be_added[row_index][column_index] -= 9
        part2_grid.extend(to_be_added)

    grid = Graph(part2_grid)
    grid.make_adjacency()

    shortest_route = Astar(grid, (0,0), (len(grid.graph)-1, len(grid.graph[0])-1))

    print("The shortest route is:", shortest_route[0], "\nThe answer to part 2 is:", shortest_route[1])

    end = time.time()

    print("The elapsed time is:", end-start)