class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict={}
        second = {}
        for char in s:
            if(len(s) != len(t)):
                return False
            if(char in mydict):
                mydict[char] +=1
            else:
                mydict[char] = 1
        for char in t:
            if(char in second):
                second[char]+=1
            else:
                second[char] = 1
        return second == mydict
            

        