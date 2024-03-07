class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums) 
        result = []
        nums.sort()
        for a in range(n):
            for b in range(a+1, n):
                c = b+1
                d = n-1

                while c < d:
                    total = nums[a]+nums[b]+nums[c]+nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        arr = [nums[a], nums[b], nums[c], nums[d]]
                        if arr not in result:
                            result.append(arr)
                        c += 1
                        d -= 1
        return result