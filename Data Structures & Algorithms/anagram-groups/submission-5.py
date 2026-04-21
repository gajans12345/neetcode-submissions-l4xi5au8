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
                tempLst.append([element,tuple(tempLst1)])
        lst = []

        for element in tempLst:
            if element[1] in dict1:
                dict1[element[1]].append(element[0])
            else:
                dict1[element[1]] = [element[0]]

        for key, value in dict1.items():
            lst.append(value)

        return lst