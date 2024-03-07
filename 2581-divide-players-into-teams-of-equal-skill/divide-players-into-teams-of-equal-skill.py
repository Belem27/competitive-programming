class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]

        skill.sort()

        prev = None
        result = 0
        
        for i in range(n//2):
            j = n - i - 1
            
            if prev is None:
                prev = skill[i] + skill[j]
                result = skill[i] * skill[j]
            elif prev == skill[i] + skill[j]:
                result += skill[i] * skill[j]
            else: return -1

        return result