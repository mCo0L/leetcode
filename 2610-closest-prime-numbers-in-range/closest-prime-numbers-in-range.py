class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        for num in range(left, right+1):
            if self.isPrime(num):
                primes.append(num)

        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('Inf')
        num1 = None
        num2 = None
        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            if  diff < min_diff:
                min_diff = diff
                num1 = primes[i]
                num2 = primes[i+1]
        
        return [num1, num2]