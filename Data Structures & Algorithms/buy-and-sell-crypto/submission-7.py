class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1
        while right <= len(prices)-1:
            maxProfit = max(maxProfit,prices[right] - prices[left])
            if prices[right] - prices[left] < 0:
                left+=1
            else:
                right+=1
            if right == left:
                right+=1


        return maxProfit



        
                
        