class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n = len(nums)
        a = []
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]> n/3:
                a.append(i)
        return a

            

        