from random import random
import random

# Random Maze generator


class Maze:
    def __init__(self, i, j, cols, rows):
        self.__cols = cols
        self.__rows = rows
        self.__grid = self.__make_temp_grid()
        current = (i, j)
        visited = [current]
        stack = [current]
        while stack:
            if not all(item in visited for item in Maze.__get_neighbours(self, current[0], current[1])):
                chosen = random.choice(list(set(Maze.__get_neighbours(self, current[0], current[1])) - set(visited)))
                self.__grid[(chosen[0] + current[0]) // 2][(chosen[1] + current[1]) // 2] = 0
                current = chosen
                visited.append(current)
                stack.append(current)
            else:
                current = stack.pop()

    @property
    def grid(self):
        return self.__grid

    def __make_temp_grid(self):
        temp = []
        i = 0
        while i < self.__rows:
            temp.append([])
            j = 0
            if i % 2 == 0:
                while j < self.__cols:
                    temp[i].append(1)
                    j += 1
            else:
                while j < self.__cols:
                    if j % 2 == 0:
                        temp[i].append(1)
                    else:
                        temp[i].append(0)
                    j += 1
            i += 1
        return temp

    def __get_neighbours(self, i, j):
        neighbors = [(i + 2, j), (i, j + 2), (i - 2, j), (i, j - 2)]

        if i == 1 or self.__grid[i - 1][j] == 0:
            neighbors.remove((i - 2, j))
        if j == 1 or self.__grid[i][j - 1] == 0:
            neighbors.remove((i, j - 2))
        if i == len(self.__grid) - 2 or self.__grid[i + 1][j] == 0:
            neighbors.remove((i + 2, j))
        if j == len(self.__grid[i]) - 2 or self.__grid[i][j + 1] == 0:
            neighbors.remove((i, j + 2))

        return neighbors
