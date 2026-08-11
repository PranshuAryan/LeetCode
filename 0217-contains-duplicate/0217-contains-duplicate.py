class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_set=len(set(nums))
        if(len(nums) == len_set):
            return False
        else:
            return True