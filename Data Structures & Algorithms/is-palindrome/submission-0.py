class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = 0
        s = s.replace(" ", "")
        x = len(s) - 1
        print(s)
        for i in range(len(s)):
            print(s[i])
            print(x)
            print(v)
            if v == x:
                return True
            elif not (s[v].isalpha() or s[v].isnumeric()):
                v = v + 1
                continue
            elif not (s[x].isalpha() or s[x].isnumeric()):
                 x = x - 1
                 continue
            elif s[v].lower() != s[x].lower():
                return False
            else:
                v = v + 1
                x = x - 1
        return True

        