class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convertToMinutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        if len(timePoints) > 1440:
            return 0

        minutes = sorted(convertToMinutes(time) for time in timePoints)
        min_diff = float('inf')
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])
        
        return min_diff