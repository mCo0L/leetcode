class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = {}
        for ch in arr:
            counter[ch] = counter.get(ch, 0) + 1
        
        for ch in arr:
            if counter[ch] == 1:
                k -= 1
                if k == 0:
                    return ch
        
        return ""