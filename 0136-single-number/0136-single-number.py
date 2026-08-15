class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range (len(nums)):
            if(nums.count(nums[i]) == 2):
                continue
            else:
                return(nums[i])
        