# Problem: Shortest Path to Get All Keys - https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        key_bits = {chr(i + ord('a')): i for i in range(6)}
        lock_bit = {chr(i + ord('A')): i for i in range(6)}
        all_keys = 0
        start = None

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys |= (1 << key_bits[grid[i][j]])

        q = deque([(start[0], start[1], 0, 0)])
        visited = set((start[0], start[1], 0))

        while q:
            r, c, keys, steps = q.popleft()

            for dr, dc in direction:
                row, col = r + dr, c + dc
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    cell = grid[row][col]

                    if cell == '#':
                        continue
                    
                    if cell.islower():
                        new_keys = keys | (1 << key_bits[cell])
                    else:
                        new_keys = keys
                    
                    if cell.isupper() and not (keys & (1 << lock_bit[cell])):
                        continue
                    
                    if new_keys == all_keys:
                        return steps +1

                    if (row, col, new_keys) not in visited:
                        visited.add((row, col, new_keys))
                        q.append((row, col, new_keys, steps +1))

        return -1
