# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])
        q = deque([0])

        while q:
            node = q.popleft()
            for nei in rooms[node]:
                if nei not in visited:
                    visited.add(nei)
                    if len(visited) == len(rooms):
                        return True
                    q.append(nei)
        return len(visited) == len(rooms)