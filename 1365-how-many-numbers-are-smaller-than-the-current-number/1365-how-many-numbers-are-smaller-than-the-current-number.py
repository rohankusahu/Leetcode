class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res=[]
        for i in nums :
            l=[]
            c=0
            for j in nums:
                if i>j:
                    c+=1
            res.append(c)
        return res
