class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        ans+=nums
        for i in nums:
            ans.append(i)
        return ans    