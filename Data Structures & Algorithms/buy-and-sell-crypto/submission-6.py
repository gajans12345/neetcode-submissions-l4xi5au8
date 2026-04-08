class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    print(prices[i],prices[j])
                    maxProfit = prices[j] - prices[i]
        return maxProfit



        
                
        