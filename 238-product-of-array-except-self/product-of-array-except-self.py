class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        pre_mult = 1
        suf_mult = 1
        

        for i in range(n):
            pre_mult *= nums[i]
            prefix[i] = pre_mult
            
            suf_mult *= nums[n-1-i]
            suffix[n-1-i] = suf_mult
        
        results = []
        for i in range(n):
            left = prefix[i-1] if i-1 >= 0 else 1
            right = suffix[i+1] if i+1 < n else 1
            results.append(left*right)
        
        return results


        