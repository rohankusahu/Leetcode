class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        l=[]
        for i in nums:
            if i==1:
                c+=1
            else:
                l.append(c)
                c=0
            l.append(c)
        return max(l)
        """
        :type nums: List[int]
        :rtype: int
        """
        