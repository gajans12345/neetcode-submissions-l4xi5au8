class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        a = 0
        b = 1
        while a < len(prices) - 1:
            if b > len(prices) - 1:
                break
            profit1 = prices[b] - prices[a]
            if profit1 > profit:
                profit = profit1
            if profit1 < 0:
                a = a + 1
            else:
                b = b + 1
            if(a == b):
                b = a + 1
           
        return profit


        
                
        