class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.running_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.running_sum[i + 1] = self.running_sum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.running_sum[right + 1] - self.running_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)