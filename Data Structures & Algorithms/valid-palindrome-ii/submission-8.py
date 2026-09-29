class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        chance = 1
        tp = []

        while left < right:
            
            if s[right] != s[left]:
                l1 = s[left+1:right+1]
                v1 = s[left:right]
                print(l1,v1)
                if l1[::-1] == l1 or v1[::-1] == v1:
                    return True
                else:
                    return False
            right-=1
            left+=1
        return True

        


        