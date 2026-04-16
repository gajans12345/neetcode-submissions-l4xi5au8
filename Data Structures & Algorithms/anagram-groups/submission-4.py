class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        dict1 = {}
        lst = []
        for element in strs:
            if "".join(sorted(element)) in dict1:
                dict1["".join(sorted(element))].append(element)
            else:
                dict1["".join(sorted(element))] = [element]
        for key,value in dict1.items():
            lst.append(value)
        return lst


        