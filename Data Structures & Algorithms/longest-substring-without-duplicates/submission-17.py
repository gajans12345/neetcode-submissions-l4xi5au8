class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        maxCount = 1
        left = 0
        right = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dict1[s[left]] = 1
        if s[right] not in dict1:
            dict1[s[right]] = 1
            curCount = 2
        else:
            curCount = 1
        right+=1
        maxCount = max(curCount,maxCount)
        while right < len(s):
            if s[right] not in dict1:
                curCount+=1
                dict1[s[right]] = 1
                right+=1
            else:
                curCount -=1
                del dict1[s[left]]
                left+=1
                if left >= right:
                    right+=1
            maxCount = max(curCount,maxCount)
        return maxCount
            
            

   