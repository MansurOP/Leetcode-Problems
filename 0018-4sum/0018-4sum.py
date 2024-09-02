from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique and handle duplicates
        res = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates for the first number
            
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue  # Skip duplicates for the second number
                
                l, r = j + 1, n - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        # Skip duplicates for the third number
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        # Skip duplicates for the fourth number
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        
                    elif total < target:
                        l += 1  # Increase the sum by moving left pointer to the right
                    else:
                        r -= 1  # Decrease the sum by moving right pointer to the left
        
        return res
