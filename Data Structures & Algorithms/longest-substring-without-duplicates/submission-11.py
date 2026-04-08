class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        maxCount = 1
        left = 0
        right = 1
        if len(s) == 0:
            return 0
        dict1[s[left]] = 1
        while right < len(s):
            curCount = 1
            while right < len(s) and s[right] not in dict1:
                curCount+=1
                dict1[s[right]] = 1
                right+=1
            maxCount = max(maxCount,curCount)
            left+=1
            right = left + 1
            dict1.clear()
            dict1[s[left]] = 1
        return maxCount
            
            

   