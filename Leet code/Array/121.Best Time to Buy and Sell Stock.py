class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        max=0
        while r < len(prices):
            if (prices[r] > prices[l]):
                profit=prices[r]-prices[l]
                if (profit > max):
                    max = profit
            else:
                l=r
            r+=1
        return max



        
