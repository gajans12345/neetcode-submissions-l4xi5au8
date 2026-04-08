class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        a = 0
        b = 0
        maxCount = 0
        dict1 = {}

        while b < len(s):
            # duplicate found → shrink window
            if s[b] in dict1:
                del dict1[s[a]]
                a += 1
            else:
                dict1[s[b]] = 0
                b += 1
                maxCount = max(maxCount, b - a)

        return maxCount
