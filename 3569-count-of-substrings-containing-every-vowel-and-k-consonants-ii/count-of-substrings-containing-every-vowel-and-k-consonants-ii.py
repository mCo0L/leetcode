class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels for quick lookup
        
        vowel_count = {}  # Tracks the frequency of vowels in the current window
        total_substrings = 0  # Final count of valid substrings
        consonant_count = 0  # Number of consonants in the current window
        distinct_vowel_count = 0  # Number of unique vowels in the current window
        extra_vowel_starts = 0  # Tracks extra valid start positions
        left = 0  # Left pointer of the sliding window
        
        for right, char in enumerate(word):
            # Expand the window by adding the rightmost character
            if char in vowels_set:
                vowel_count[char] = vowel_count.get(char, 0) + 1
                if vowel_count[char] == 1:  # If it's a new vowel in the window
                    distinct_vowel_count += 1
            else:
                consonant_count += 1  # Increase consonant count
            
            # Shrink the window if the consonant count exceeds k
            while consonant_count > k:
                left_char = word[left]
                if left_char in vowels_set:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:  # If a vowel count drops to zero
                        distinct_vowel_count -= 1
                else:
                    consonant_count -= 1  # Reduce consonant count
                left += 1
                extra_vowel_starts = 0  # Reset extra starts since we changed the window
                
            # Count extra valid starting positions while all vowels are present
            while (distinct_vowel_count == 5 and consonant_count == k and 
                   left < right and word[left] in vowels_set and vowel_count[word[left]] > 1):
                extra_vowel_starts += 1
                vowel_count[word[left]] -= 1
                left += 1

            # If we have a valid window, count it along with extra valid starts
            if distinct_vowel_count == 5 and consonant_count == k:
                total_substrings += (1 + extra_vowel_starts)

        return total_substrings
