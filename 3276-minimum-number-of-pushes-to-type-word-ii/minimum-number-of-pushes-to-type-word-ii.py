class Solution:
    def minimumPushes(self, word: str) -> int:
        word_len = len(word)
        if word_len <= 8:
            return word_len

        counts = collections.Counter(word)
        cost = 0
        for i, (_, val) in enumerate(sorted(counts.items(), reverse=True, key=lambda x: counts[x[0]])):
            cost += val * ((i+8) // 8)
        
        return cost



        