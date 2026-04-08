class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mytuple = ()
        lst = []
        lst2 = []
        dict1 = {}
        for element in strs:
            lst = [0]*26
            for letter in element:
                index = ord(letter) - ord('a')  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25
                lst[index] += 1 
            m = tuple(lst)
            if m not in dict1.keys():
                dict1[m] = []        
                dict1[m].append(element)
            else:
                dict1[m].append(element)
        for element in dict1.keys():
            lst2.append(dict1[element])
        return lst2


        

            

        