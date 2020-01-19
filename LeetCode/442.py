#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/8 9:48
@Author  : duanpy001
@File    : 442.py
@Link    : https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            nums[(nums[i] - 1) % n] += n
        for i in range(n):
            if nums[i] > 2 * n:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    test_data = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDuplicates(test_data))
