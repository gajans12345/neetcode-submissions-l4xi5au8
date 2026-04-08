class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 1
        res = 0
        count = 0
        lst = []
        curr = 0
        dict1 = {}
        l = 0
        r = 0
        for r in range(len(s)):
            if s[r] in dict1:
                dict1[s[r]]+=1
            else:
                dict1[s[r]] = 1
            maxCount = max(maxCount,dict1[s[r]])
            while (r - l + 1) - maxCount > k:
                dict1[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res
            

  
                



       



        