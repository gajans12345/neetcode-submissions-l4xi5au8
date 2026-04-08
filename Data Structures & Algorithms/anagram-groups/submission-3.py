class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        temp = {}
        for element in strs:
            v = ''.join(sorted(element))
            if v not in temp.keys():
                tempy = []
                tempy.append(element)
                temp[v] = tempy
            else:
                temp[v].append(element)
        for k,v in temp.items():
            lst.append(v)
        return lst

        