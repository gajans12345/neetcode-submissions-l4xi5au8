class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        curcount = 0
        count = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            dict1 = {}
            count = 1
            dict1[s[i]] = 0
            print("Added", s[i])
            for j in range(i+1,len(s)):
                if s[j] not in dict1:
                    print("Added", s[j])
                    count+=1
                    dict1[s[j]] = 0
                else:
                    break
            if count > curcount:
                print("Updating on i =",i)
                curcount = count
        return curcount
        