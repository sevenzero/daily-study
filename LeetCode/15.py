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
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            # 剪枝，该位置数为正数，那么后面所有数都大于零，三数和不会等于零
            if nums[i] > 0:
                break
            # 遇见重复值跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 两指针分别从当前固定值之后的子数组的首尾开始搜索
            low = i + 1
            high = n - 1
            while low < high:
                cursum = nums[low] + nums[high] + nums[i]
                if cursum == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    # 跳过重复数
                    while low < high and nums[low] == nums[low + 1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high - 1]:
                        high = high - 1
                    high = high - 1
                    low = low + 1
                # 三数之和大于 0，说明尾指针数太大，往前移
                elif cursum > 0:
                    high = high - 1
                # 三数之和小于 0，说明头指针数太小，头指针往后移
                else:
                    low = low + 1
        return res


if __name__ == '__main__':
    s = Solution()
    test_data = [[-1, 0, 1, 2, -1, -4]]
    test_res = [[-1, -1, 2], [-1, 0, 1]]
    for i in test_data:
        print(s.threeSum(i))
