# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        board.reverse()

        def helper(pos):
            r = (pos - 1) //n
            c = (pos - 1) % n
            if r % 2:
                c = n - 1 - c
            return (r,c)

        q=deque()
        q.append([1,0])
        visited = set()
        while q:
            pos, steps = q.popleft()
            for i in range(1,7):
                nextPos = pos+i
                r,c = helper(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                if nextPos == n**2:
                    return steps+1
                if nextPos not in visited:
                    visited.add(nextPos)
                    q.append([nextPos, steps+1])
        return -1