from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = 1
        y = len(nums) - 1
        lst = []
        v = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            print("This is i " + str(i))
            x = i + 1
            for j in range(i + 1, len(nums)):
                print("This is j " + str(j))
                print(" This is x " + str(nums[i]) + " " + str(nums[x]) + " " + str(nums[y]))
                if x >= y:
                    print("x equals y statement")
                    y = len(nums) - 1
                    break
                elif nums[i] + nums[x] + nums[y] == 0 and i != x and i != y and x != y:
                    print("found 3")
                    lst = [nums[i], nums[x], nums[y]]
                    lst.sort()  # Sort the triplet
                    if lst not in v:  # Check if the triplet is already in the result list
                        print("appending")
                        print(lst)
                        v.append(lst)  # Append the triplet
                    x = x + 1
                    y = y - 1
                elif nums[i] + nums[x] + nums[y] > 0:
                    print("greater")
                    y = y - 1
                elif nums[i] + nums[x] + nums[y] < 0:
                    print("less")
                    x = x + 1
        return v
