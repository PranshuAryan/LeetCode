class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_nums, max_nums = min(nums), max(nums)
        for i in range(len(nums)):
            if (len(nums)>2):
                if (nums[i] == min_nums or nums[i] == max_nums):
                    continue
                else:
                    return nums[i]
            else:
                return -1        