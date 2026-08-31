class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Complexity. O(n * L log L) where l is average length of string and n strings
# space would prolly be o(n*L) since n strings each avg length L
# would be o(n) if just stroign n constant space things
# create list or sorted strings will be same length sorting each char in word
# hve a hashmap. loop throug sorted list if a key add unsorted at index
#HASHMAP KEY WILL BE A STRING VALUE WILL BE A LIST
#loop through values of hashmap add each list into another list and return
        sorted_strs = []
        dict1 = {}
        result = []
        for element in strs:
            sorted_strs.append(''.join(sorted(element)))
        
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in dict1:
                dict1[sorted_strs[i]].append(strs[i])
            else:
                dict1[sorted_strs[i]] = [strs[i]]
        
        for key,value in dict1.items():
            result.append(value)
        return result


            



        