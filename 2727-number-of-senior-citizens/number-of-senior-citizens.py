class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passanger in details:
            if int(passanger[11:13]) > 60:
                count += 1
        return count 
        