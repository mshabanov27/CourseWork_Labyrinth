from queue import PriorityQueue
from Graph import Graph

# Graph representation with Dijkstra algorithm used


class GraphForDijkstra(Graph):
    def dijkstraAlgorithm(self, start, goal):
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
                if next_node != (1, start):
                    new_cost = path_cost[current[1]] + next_node[0]
                    if next_node not in path_cost or (next_node in path_cost and new_cost < path_cost[next_node][0]):
                        path_cost[next_node[1]] = new_cost
                        priority = new_cost
                        border.put((priority, next_node))
                        came_from[next_node[1]] = current
            visited.append(current)
        return Graph.reconstruct_path(came_from, start, goal), visited
