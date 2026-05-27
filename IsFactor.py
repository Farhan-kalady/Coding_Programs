from math import sqrt
class Solution:
    def countFactors (self, n):
        # code here
        count = 0
        
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                if n // i != i:
                    count += 1
        return count     
    
obj = Solution()
print(obj.countFactors(12))