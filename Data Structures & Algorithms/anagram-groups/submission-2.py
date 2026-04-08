class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        lst = []

        for item in strs:
            #print("Analyzing " + item)
            lst1 = [0] * 26
            for item1 in item:
                index = ord(item1) - ord('a')
                lst1[index]+=1
            if tuple(lst1) in dict1.keys():
                #print("Already")
                dict1[tuple(lst1)].append(item)
            else:
                #print("Adding")
                dict1[tuple(lst1)] = [item]
           #print(dict1)
        for key,value in dict1.items():
            lst.append(value)
        return lst


        



        


        

            

        