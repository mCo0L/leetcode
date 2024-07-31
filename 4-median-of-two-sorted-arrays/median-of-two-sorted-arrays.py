class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA = len(nums1)
        lenB = len(nums2)

        i, j = 0, 0;

        newArr = []

        while(i < lenA or j < lenB):
            if i == lenA:
                newArr += nums2[j:]
                j = lenB
                continue
            
            if j == lenB:
                newArr += nums1[i:]
                i = lenA
                continue
            
            if nums1[i] < nums2[j]:
                newArr.append(nums1[i])
                i += 1
            else:
                newArr.append(nums2[j])
                j += 1

        newL = lenA + lenB

        if newL % 2 == 0:
            return (newArr[(newL // 2) - 1] + newArr[newL // 2])/2
        else:
            return newArr[newL//2]