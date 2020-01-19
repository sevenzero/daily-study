#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/17 9:31
@Author  : duanpy001
@File    : 11.py
@Link    : https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        last_short_height = 0
        while i <= j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    test_data = [[1, 8, 6, 2, 5, 4, 8, 3, 7]]
    for i in test_data:
        print(s.maxArea(i))
