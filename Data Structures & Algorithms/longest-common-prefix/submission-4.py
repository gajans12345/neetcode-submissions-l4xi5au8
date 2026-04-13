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
            for element in strs:
                if element[i] != shortest[i]:
                    return prefix
            prefix+=shortest[i]

        return prefix