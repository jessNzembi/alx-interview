#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """calculates perimeter of island"""
    visited = set()

    def dfs(i, j):
        """ depth first search"""
        if (i, j) in visited:
            return 0
        if i >= len(grid) or j >= len(grid) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        visited.add((i, j))
        total = dfs(i, j+1)
        total += dfs(i+1, j)
        total += dfs(i, j-1)
        total += dfs(i-1, j)

        return total

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
