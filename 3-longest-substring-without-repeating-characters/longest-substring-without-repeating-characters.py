class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest = 0
        stack = [s[0]]
        for i in range(1, n):
            if s[i] not in stack:
                stack.append(s[i])
                continue
            longest = max(longest, len(stack))
            while True:
                if s[i] == stack.pop(0):
                    break
            stack.append(s[i])
        
        longest = max(longest, len(stack))
        return longest
            

                
        