class Solution(object):
    def checkDivisibility(self, n):
        digits = [int(digit) for digit in str(n)]
        
        digit_sum = sum(digits)
        
        digit_product = 1
        for d in digits:
            digit_product *= d
            
        divisor = digit_sum + digit_product
    

        return n % divisor == 0
        