class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        temp1 = ""
        for word in s:
            if word.isalnum() == True:
                temp+=word
        a = 0
        b = len(temp) - 1
        temp1 = temp.lower()
        for i in range(len(temp1)):
            print("A",temp[a])
            print("B",temp[b])
            if a == b:
                return True
            elif temp1[a] != temp1[b]:
                return False
            else:
                a +=1
                b-=1
        return True
                
        