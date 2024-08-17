class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["i", "e", "a", "o", "u", "A", "E", "I", "O", "U"])
        st = ''
        backpointer = len(s)
        for i in range(len(s)):
            if s[i] in vowels:
                backpointer -= 1
                while s[backpointer] not in vowels:
                    backpointer -= 1
                st += s[backpointer]
            else:
                st += s[i]
        return st
