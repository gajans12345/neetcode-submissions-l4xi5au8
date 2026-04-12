class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        tempLength = len(strs[0])
        prefix = ""
        for element in strs:
            if len(element) < tempLength:
                tempLength = len(element)
                shortest = element
        for i in range(len(shortest)):
            counter= 0
            for element in strs:
                if element[0:i+1] == shortest[0:i+1]:
                    counter+=1
            if counter == len(strs):
                prefix+=shortest[i]

            else:
                break

            

        return prefix