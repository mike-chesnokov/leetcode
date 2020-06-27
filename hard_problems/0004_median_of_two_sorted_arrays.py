"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    
    def mergeSortedLists(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_len, nums2_len = len(nums1), len(nums2)
        merged_len = nums1_len + nums2_len
        
        p1 = 0
        p2 = 0
        result = []
        # compare elements from 2 lists 1 by 1
        while p1 + p2 < merged_len:
            # print(p1, p2, result)
            # if end of list reached, don't use this list
            if p1 < nums1_len:
                el1 = nums1[p1]
            else:
                el1 = 10e10
                
            if p2 < nums2_len:
                el2 = nums2[p2]
            else:
                el2 = 10e10
            
            if el1 < el2:
                result.append(el1)
                p1 += 1
            else:
                result.append(el2)
                p2 += 1
            # print(p1, p2, result)
                
        return result, merged_len
    
    def mergeBeforeCalculateMedian(self, nums1: List[int], nums2: List[int]) -> float:
        # Runtime: 100 ms, faster than 50.66% of Python3 online submissions
        # Memory Usage: 14.2 MB, less than 21.45% of Python3 online submissions
        # merge lists and find median
        merged, merged_len = self.mergeSortedLists(nums1, nums2)
        median_ind = merged_len // 2
        # print(merged, merged_len, median_ind)
        
        # for even number of elements use 2 el for median calculation
        # else take middle of array
        if merged_len % 2 == 0:
            median = (merged[median_ind] + merged[median_ind - 1]) / 2
        else:
            median = merged[median_ind]
            
        return median
    
    def bruteForce(self, nums1: List[int], nums2: List[int]) -> float:
        # Runtime: 88 ms, faster than 93.58% of Python3 online submissions
        # Memory Usage: 14.1 MB, less than 30.22% of Python3 online submissions
        # use python list sorting
        merged = nums1 + nums2
        merged.sort()
        merged_len = len(merged)
        
        median_ind = merged_len // 2
        # for even number of elements use 2 el for median calculation
        # else take middle of array
        if merged_len % 2 == 0:
            median = (merged[median_ind] + merged[median_ind - 1]) / 2
        else:
            median = merged[median_ind]
            
        return median 
        
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.bruteForce(nums1, nums2)
        #return self.mergeBeforeCalculateMedian(nums1, nums2)
