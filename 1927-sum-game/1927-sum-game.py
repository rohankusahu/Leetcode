class Solution(object):
    def sumGame(self, num):

        n = len(num)
        half = n // 2
        
        sum_l = 0
        sum_r = 0
        q_l = 0
        q_r = 0
        

        for i in range(half):
            if num[i] == '?':
                q_l += 1
            else:
                sum_l += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q_r += 1
            else:
                sum_r += int(num[i])

        if (q_l + q_r) % 2 != 0:
            return True
            
        return (sum_l - sum_r) != 9 * (q_r - q_l) / 2