class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Given n cars on one line
        # array of position and speed of each car
        # target is the finish line
        # no overtaking, only catch up so noincedent
        # return number of fleets
        # essentially cars will maybe group find number
        # of car groupings 1 or many
        
        # length max
        # fleet decrement over
        fleet = len(position)
        dict1 = {}
        for i in range(len(position)):
            dict1[position[i]] = speed[i]
        
        position = sorted(position)
        for i in range(len(position)):
            speed[i] = dict1[position[i]] 
        # now matching
        # continous time means we have to look at time not snaphots
        # time for car i is (target-position)/speed
        #so once you have all, you loop through nested and so some merging
        # [3,4.5,10,3]. 4 - 1
        # [10,4.5,3,3] 3
        # order : [1,1,0,2]

        #pos : [1,6,2.666]
        result = [0]*len(position)
        for i in range(len(position)):
            result[i] = float((target - position[i])/speed[i])
        
        for i in range(len(result)-1):
            for j in range(i+1,len(result)):
                if result[i] <= result[j]:
                    fleet-=1
                    break
                    
        return fleet


