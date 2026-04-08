class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max2 = 0
        for i in range(len(prices)):
            print("loop")
            for j in range(i+1,len(prices)):
                if (prices[j] - prices[i]) > max2:
                    print("prices[i",prices[i])
                    print("prices[j]",prices[j])
                    max2 = prices[j] - prices[i]
        return max2
                
        