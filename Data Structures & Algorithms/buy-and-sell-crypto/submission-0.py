class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if (prices[j] - prices[i]) > max1:
                    print(prices[i])
                    print(prices[j])
                    max1 = prices[j] - prices[i]
        return max1

        