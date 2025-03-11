class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Predefine the vowel set for membership checks.
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        
        # frequencies[0] acts as a "set" of vowels (for compatibility with your code).
        # frequencies[1] tracks counts of vowels in the current window.
        frequencies = [{v: 1 for v in vowels_set}, {}]
        
        response = 0
        currentK = 0  # count of consonants in current window
        vowels = 0    # count of distinct vowels in current window
        extraLeft = 0
        left = 0

        for right, rightChar in enumerate(word):
            # Update counts using the pre-defined vowels_set
            if rightChar in vowels_set:
                frequencies[1][rightChar] = frequencies[1].get(rightChar, 0) + 1
                if frequencies[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1

            # Shrink the window if there are too many consonants.
            while currentK > k:
                leftChar = word[left]
                if leftChar in vowels_set:
                    frequencies[1][leftChar] -= 1
                    if frequencies[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0  # Reset extraLeft when adjusting for extra consonants.

            # Slide left further to count additional valid starting positions.
            while (vowels == 5 and currentK == k and left < right and 
                   word[left] in vowels_set and frequencies[1][word[left]] > 1):
                extraLeft += 1
                frequencies[1][word[left]] -= 1
                left += 1

            if currentK == k and vowels == 5:
                response += (1 + extraLeft)

        return response
