class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []
        for customer in accounts:
            add = sum(customer)
            wealth.append(add)
        return(max(wealth))
        