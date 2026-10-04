class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)
        dict1 = {}
        for i in range(len(position)):
            dict1[position[i]] = speed[i]
        
        position = sorted(position,reverse=True)
        for i in range(len(position)):
            speed[i] = dict1[position[i]] 
        # now matching
        # continous time means we have to look at time not snaphots
        # time for car i is (target-position)/speed
        #so once you have all, you loop through nested and so some merging
        # [3,4.5,10,3]. 4 - 1
        # [10,4.5,3,3] 
        # order : [1,1,0,2]

        #pos : [1,6,2.666]
        # [3,3,4.5,10]
        result = [0]*len(position)
        for i in range(len(position)):
            result[i] = float((target - position[i])/speed[i])
        
        for i in range(len(result)):
            for j in range(i):                 # only cars ahead
                if result[i] <= result[j]:     # I arrive same time or sooner → blocked
                    fleet -= 1
                    break
                    
        return fleet


