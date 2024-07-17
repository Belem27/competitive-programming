# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length = len(board)
        board.reverse()

        def getRolCol(pos):
            r = (pos - 1) // length
            c = (pos - 1) % length
            if r % 2:
                c = length - 1 - c
            return (r,c)

        q = deque()
        q.append([1,0])
        visited = set()
        while q:
            pos, steps = q.popleft()
            for i in range(1,7):
                nextPos = pos + i
                r,c = getRolCol(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                if nextPos == length * length:
                    return steps+1
                if nextPos not in visited:
                    visited.add(nextPos)
                    q.append([nextPos, steps+1])
        return -1

