#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/13 8:59 下午
@Author  : duanpy001
@File    : 26.py
@Link    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
@Desc    :
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, q = 0, 0
        while q < len(nums):
            if nums[p] != nums[q]:
                p += 1
                nums[p] = nums[q]
            q += 1
        return p + 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates(nums))
    print(nums)