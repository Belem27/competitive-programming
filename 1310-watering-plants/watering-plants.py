class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps, i = 0, 0
        water = capacity

        while i < len(plants):      
            if water < plants[i]:
                steps += 2*i    
                water = capacity
            
            water -= plants[i]
            steps += 1
            i += 1

        return steps    