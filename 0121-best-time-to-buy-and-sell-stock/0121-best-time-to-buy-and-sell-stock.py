class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, profit = prices[0], 0
        for i in range(1 , len(prices)):
            if(buy > prices[i]):
                buy = prices[i]
            else:
                current_profit = prices[i]-buy
                if(current_profit > profit):
                    current_profit = prices[i]-buy
                    profit = current_profit
        return(profit)