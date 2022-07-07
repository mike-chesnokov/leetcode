"""
200. Number of Islands
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:

    def bfs(self, grid: List[List[str]]) -> int:
        """
        1. find all ones - collect to array "all_ones"
        2. start bfs from every one from previous step
        3. delete one from array "all_ones" if it is found
        4. append this one coordinates to queue
        """
        num_rows = len(grid)
        num_cols = len(grid[0])

        # find all ones
        all_ones = []
        for row_ind in range(num_rows):
            for col_ind in range(num_cols):
                if grid[row_ind][col_ind] == "1":
                    all_ones.append((row_ind, col_ind))
        # start from every "1", go below and to the right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt_islands = 0

        while all_ones:
            # print('********************************')
            # print('all_ones =', all_ones)
            # print('cnt_islands =', cnt_islands)
            cur_one = all_ones.pop(0)
            cnt_islands += 1
            queue = [cur_one]
            visited = {cur_one}

            while queue:
                # print('queue = ', queue)
                # print('visited = ', visited)
                # print('grid = ', grid)
                # print('all_ones =', all_ones)

                q_size = len(queue)
                for _ in range(q_size):
                    cur_point = queue.pop(0)
                    # print('queue = ', queue)
                    # print('all_ones =', all_ones)
                    for row_diff, col_diff in directions:
                        new_row = cur_point[0] + row_diff
                        new_col = cur_point[1] + col_diff

                        if new_row >= len(grid) or new_row < 0 or \
                                new_col >= len(grid[0]) or new_col < 0 or \
                                (new_row, new_col) in visited:
                            continue
                        # connected "1" found
                        if grid[new_row][new_col] == '1':
                            # delete this "1" as connected to cur_point "1"
                            all_ones.remove((new_row, new_col))
                            # append to queue only connected "1"
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
        return cnt_islands

    def bfs2_helper(self, cur_row: int, cur_col: int, grid: List[List[str]]):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = [(cur_row, cur_col)]
        visited = {(cur_row, cur_col)}

        while queue:
            q_size = len(queue)

            for _ in range(q_size):
                cur_point = queue.pop(0)

                for row_diff, col_diff in directions:
                    new_row = cur_point[0] + row_diff
                    new_col = cur_point[1] + col_diff

                    if new_row >= len(grid) or new_row < 0 or \
                            new_col >= len(grid[0]) or new_col < 0 or \
                            (new_row, new_col) in visited:
                        continue
                    # connected "1" found
                    if grid[new_row][new_col] == '1':
                        # delete this "1" as connected to cur_point "1"
                        grid[new_row][new_col] = 'x'
                        # append to queue only connected "1"
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

    def bfs2(self, grid: List[List[str]]) -> int:
        """
        1. start bfs from every "1"
        2. connected "1" change to "x"
        3. connected "1" append to queue
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        cnt_islands = 0
        # iterate over grid
        for row_ind in range(num_rows):
            for col_ind in range(num_cols):
                if grid[row_ind][col_ind] == "1":
                    # start bfs from every "1"
                    cnt_islands += 1
                    self.bfs2_helper(row_ind, col_ind, grid)
        return cnt_islands

    def numIslands(self, grid: List[List[str]]) -> int:
        # return self.bfs(grid)  # accepted solution
        return self.bfs2(grid)  # accepted solution, faster
