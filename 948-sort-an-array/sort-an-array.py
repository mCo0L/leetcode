class Solution:
    def mergeSort(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            self.mergeSort(left)
            self.mergeSort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                
                    myList[k] = left[i]
                
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
            
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums