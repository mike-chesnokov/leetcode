"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


class Solution:

    def built_in_sort(self, nums: List[int]) -> List[int]:
        """
        Using built-in sort
        """
        return sorted(nums)

    def merge_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        method for merging sorted arrays
        """
        result = []

        if nums1 and not nums2:
            return nums1
        elif not nums1 and nums2:
            return nums2
        elif not nums1 and not nums2:
            return []

        # print('***************')
        # print('nums1 = ', nums1)
        # print('nums2 = ', nums2)

        ind1 = 0
        ind2 = 0

        nums1_len = len(nums1)
        mums2_len = len(nums2)

        while ind1 < nums1_len or ind2 < mums2_len:

            # print('ind1 = ', ind1)
            # print('ind2 = ', ind2)

            if ind1 == nums1_len and ind2 < mums2_len:
                result.append(nums2[ind2])
                ind2 += 1
                continue

            if ind1 < nums1_len and ind2 == mums2_len:
                result.append(nums1[ind1])
                ind1 += 1
                continue

            if nums1[ind1] < nums2[ind2]:
                result.append(nums1[ind1])
                ind1 += 1
            else:
                result.append(nums2[ind2])
                ind2 += 1

        return result

    def merge_sort(self, nums: List[int]) -> List[int]:
        """
        Imlementation of "merge sort" algo
        """
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        # apply method recursively to each part
        left_nums = self.merge_sort(nums[:pivot])
        right_nums = self.merge_sort(nums[pivot:])
        # join sorted arrays
        return self.merge_arrays(left_nums, right_nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.built_in_sort(nums)  # accepted
        return self.merge_sort(nums)
