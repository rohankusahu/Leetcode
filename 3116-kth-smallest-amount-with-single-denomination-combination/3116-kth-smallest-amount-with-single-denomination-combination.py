class Solution:
    def findKthSmallest(self, coins, k) :
        n = len(coins)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        subsets = []
        for mask in range(1, 1 << n):
            current_lcm = 1
            count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    current_lcm = lcm(current_lcm, coins[i])
                    count += 1
            sign = 1 if count % 2 == 1 else -1
            subsets.append((current_lcm, sign))
        low, high = 1, min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            total_count = sum(sign * (mid // lcm_val) for lcm_val, sign in subsets)
            
            if total_count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans