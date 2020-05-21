#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/14 9:36 下午
@Author  : duanpy001
@File    : 31.py
@Link    : https://leetcode-cn.com/problems/next-permutation/
@Desc    :
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = len(nums) - 2
        # 从最后一个往前，找到第一个值小于右边元素
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
        # 当 p < 0 时意味着整个序列是一个降序，直接反转
        if p >= 0:
            # 从后面再次扫描已走过的地方，找到比轴值大的最小数
            q = len(nums) - 1
            while q > p and nums[q] <= nums[p]:
                q -= 1
            # 交换这两个元素
            nums[q], nums[p] = nums[p], nums[q]
        # 右边部分自然是一个升序，直接翻转为降序
        nums[p+1:] = reversed(nums[p+1:])

    def nextPermutation_sec(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                return
        nums.sort()


if __name__ == '__main__':
    nums = [[1], [1, 2], [2, 1], [4, 3, 2, 1], [1, 3, 2], [1, 3, 2, 7, 5, 2, 1], [1, 2, 3], [1, 3, 2, 7, 2, 1, 5], [1, 3, 2, 7, 1, 5, 2], ]
    s = Solution()
    for i in nums:
        s.nextPermutation(i)
        print(i)
