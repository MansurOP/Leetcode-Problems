class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        d = {0:1}
        s = 0

        for i in nums:
            s+=i

            if s-k in d:
                c=c+d[s-k]
            if s not in d:
                d[s]=1
            else:
                d[s]+=1
        return c