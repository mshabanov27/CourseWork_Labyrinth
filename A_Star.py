from queue import PriorityQueue
from Graph import Graph
import math

# Graph representation with A* algorithm used


class GraphForAStar(Graph):
    def AStarAlgorithm(self, start, goal, heuristic):
        border = PriorityQueue()
        came_from = {}
        path_cost = dict()
        visited = []

        border.put((0, (0, start)))
        came_from[start] = None
        path_cost[start] = 0

        while not border.empty():
            current = border.get()[1]

            if current == (1, goal):
                break

            for next_node in list(set(self.graph[current[1]]) - set(visited)):
                new_cost = path_cost[current[1]] + next_node[0]
                if next_node not in path_cost or (next_node in path_cost and new_cost < path_cost[next_node][1]):
                    path_cost[next_node[1]] = new_cost
                    priority = new_cost + heuristic(goal, next_node[1])
                    border.put((priority, next_node))
                    came_from[next_node[1]] = current
            visited.append(current)
        return Graph.reconstruct_path(came_from, start, goal), visited

    @staticmethod
    def manhattanHeuristic(dot1, dot2):
        return abs(dot1[0] - dot2[0]) + abs(dot1[1] - dot2[1])

    @staticmethod
    def euclidHeuristic(dot1, dot2):
        return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
