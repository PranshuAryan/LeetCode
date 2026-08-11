class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = [0]
        for i in range(len(nums)):
            a = nums[i] + list[i]
            list.append(a)
        list.pop(0)
        return(list)