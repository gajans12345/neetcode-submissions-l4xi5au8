class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach get product without 0 if its there
        # divide by the current element
        returnLst = [0]*len(nums)
        product0 = 1
        productIncluding0 = 0
        containsZero = False
        for element in range(len(nums)):
            if nums[element] == 0:
                if containsZero == True:
                    product0 = 0
                else:
                    containsZero = True
            else:
                product0*=nums[element]
        print(product0)
        for i in range(len(returnLst)):
            if nums[i] == 0:
                returnLst[i]= product0
            else:
                if containsZero:
                    returnLst[i] = productIncluding0 // nums[i]
                else:
                    returnLst[i] = product0 // nums[i]
        return returnLst


        