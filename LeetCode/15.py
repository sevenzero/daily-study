#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/19 10:42
@Author  : duanpy001
@File    : 15.py
@Link    : https://leetcode-cn.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    s = Solution()
    test_data = [[-1, 0, 1, 2, -1, -4]]
    test_res = ['LCIRETOESIIGEDHN', 'LDREOEIIECIHNTSG', 'PINALSIGYAHRPI']
    for i in test_data:
        print(s.threeSum(i))
