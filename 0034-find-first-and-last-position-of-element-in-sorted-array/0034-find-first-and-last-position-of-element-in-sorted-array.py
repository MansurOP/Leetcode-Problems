class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      
        i1=-1
        i2=-1
        for i in range(len(nums)):
            if target == nums[i]:
                if i1 == -1:
                    i1 = i
                    i2 = i
                else:
                    i2= i 
        return ([i1,i2])