class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        dict1 = {}
        tempLst = []
        for element in strs:
                tempLst1 = [0] * 26
                for char in element:
                        code = ord(char) - ord('a')
                        print(code) 
                        tempLst1[code]+=1
                tempLst1 = tuple(tempLst1)
                if tempLst1 in dict1:
                        dict1[tempLst1].append(element)
                else:
                        dict1[tempLst1] = [element]
        lst = []

        for key, value in dict1.items():
            lst.append(value)

        return lst