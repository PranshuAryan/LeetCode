class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        list =[]
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= max(candies)):
                list.append(True)
            else:
                list.append(False)
        return(list)
        