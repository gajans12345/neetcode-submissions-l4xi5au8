class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        count =0
        temp = []
        flag = False
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] == nums[j]:
                    flag = True
                    nums[i] = -37.2       
            if not flag:
                count+=1
            flag = False
        print
        for i in range(length):
            if nums[i] != -37.2:
                temp.append(nums[i])
        nums[:] = temp
        return count

                    


        