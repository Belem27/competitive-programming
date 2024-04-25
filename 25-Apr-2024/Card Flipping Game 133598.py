# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        not_facing_up = set()
    
        # Find numbers that appear on the back but not on the front
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_facing_up.add(fronts[i])
        
        min_good_integer = float('inf')
        
        # Find the smallest number that is not in not_facing_up set
        for num in fronts:
            if num not in not_facing_up:
                min_good_integer = min(min_good_integer, num)
        
        for num in backs:
            if num not in not_facing_up:
                min_good_integer = min(min_good_integer, num)
        
        return min_good_integer if min_good_integer != float('inf') else 0                                             