class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        lst = []
        for letter in strs:
            res = ''.join(sorted(letter))
            if res not in dict1.keys():
                dict1[res] = [letter]
            else:
                dict1[res].append(letter)
        for item in dict1.values():
            lst.append(item)
        

        return lst