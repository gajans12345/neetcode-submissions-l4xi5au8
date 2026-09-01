class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # have a dictionary where key is a string and value is tuple of its char frequency
    # 
        dict2 = {}
        lst1 = []
        for element in strs:
            lst = [0]*26
            for char in element:
                index = ord(char) - ord('a')
                lst[index] += 1
            if tuple(lst) not in dict2:
                dict2[tuple(lst)] = [element]
            else:
                dict2[tuple(lst)].append(element)
        for key,value in dict2.items():
            lst1.append(value)
        return lst1

        
            
        
                


                

