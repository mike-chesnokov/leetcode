"""
864. Shortest Path to Get All Keys

You are given an m x n grid grid where:
    '.' is an empty cell.
    '#' is a wall.
    '@' is the starting point.
    Lowercase letters represent keys.
    Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal directions.
You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter
of the first k letters of the English alphabet in the grid.
This means that there is exactly one key for each lock, and one lock for each key;
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:
Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:
Input: grid = ["@Aa"]
Output: -1
"""
from typing import List, Tuple


class Solution:

    def bfs(self,
            grid: List[str],
            start_point: Tuple[int, int, str],
            cnt_keys: int
            ) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = [start_point]
        # visited will be (x, y, keys)
        # not (x, y) - possible to come back
        visited = set()
        cnt_moves = 0

        while queue:
            len_q = len(queue)

            # traverse through all current points in queue
            for _ in range(len_q):

                # take next neighbor from queue
                cur_point = queue.pop(0)
                # print('cur_point', cur_point)

                if cur_point in visited:
                    continue

                if len(cur_point[2]) == cnt_keys:
                    return cnt_moves

                visited.add(cur_point)

                # iterate over all directions
                for row_shift, col_shift in directions:
                    # calculate new point
                    new_point = (cur_point[0] + row_shift,
                                 cur_point[1] + col_shift,
                                 cur_point[2])
                    # print('new_point = ', new_point)

                    # skip the move if we get outside the grid
                    # or get to the wall
                    if new_point[0] < 0 or new_point[0] == len(grid) or \
                            new_point[1] < 0 or new_point[1] == len(grid[0]) or \
                            grid[new_point[0]][new_point[1]] == '#':
                        continue
                    else:
                        new_point_value = grid[new_point[0]][new_point[1]]
                        # print('new_point_value = ', new_point_value)

                        # found new key, add new key to keys_set
                        if new_point_value.islower():
                            if new_point_value not in new_point[2]:
                                new_point = (
                                    new_point[0],
                                    new_point[1],
                                    new_point[2] + new_point_value
                                )
                            queue.append(new_point)
                            continue
                        # process empty cell
                        elif new_point_value in '.@':
                            queue.append(new_point)
                            continue
                        # process lock
                        if new_point_value.isupper() and \
                                str.lower(new_point_value) in cur_point[2]:
                            queue.append(new_point)

            # print('queue = ', queue)
            # print('visited = ', visited)
            cnt_moves += 1
        return -1

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # find starting point - (row_ind, col_ind, keys string)
        # find number of keys
        start_point = None
        cnt_keys = 0

        for row_ind in range(len(grid)):
            for col_ind in range(len(grid[0])):
                if grid[row_ind][col_ind] == '@':
                    start_point = (row_ind, col_ind, '')
                if grid[row_ind][col_ind].islower():
                    cnt_keys += 1
        return self.bfs(grid, start_point, cnt_keys)
