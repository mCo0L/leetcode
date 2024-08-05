class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = {}
        for ch in arr:
            counter[ch] = counter.get(ch, 0) + 1
        
        count = 0
        for ch in arr:
            if counter[ch] == 1:
                count += 1
                if count == k:
                    return ch
        
        return ""