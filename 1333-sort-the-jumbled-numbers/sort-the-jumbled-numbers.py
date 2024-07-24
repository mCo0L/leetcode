class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))

        # Create a list of tuples (original number, mapped value)
        nums_with_mapped = [(num, mapped_value(num)) for num in nums]

        # Sort the list of tuples by the mapped values
        nums_with_mapped.sort(key=lambda x: x[1])

        # Extract and return the original numbers from the sorted list
        return [num for num, _ in nums_with_mapped]

        