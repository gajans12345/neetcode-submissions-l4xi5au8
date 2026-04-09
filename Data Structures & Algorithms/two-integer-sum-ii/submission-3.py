class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        left = 0
        lst = []
        right = len(numbers) - 1
        while left < right:
            sum1 = numbers[left] + numbers[right]
            if sum1 == target:
                lst.append(left+1)
                lst.append(right+1)
                break
            elif sum1 > target:
                right-=1
            else:
                left+=1
        return lst


        