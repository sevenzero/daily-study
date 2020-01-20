#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/19 11:31 上午
@Author  : duanpy001
@File    : 16.py
@Link    : https://leetcode-cn.com/problems/3sum-closest/
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff = float("inf")
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            low = i + 1
            high = n - 1
            while low < high:
                cursum = nums[low] + nums[high] + nums[i]
                if cursum == target:
                    while low < high and nums[low] == nums[low + 1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high - 1]:
                        high = high - 1
                    high = high - 1
                    low = low + 1
                elif cursum > target:
                    high = high - 1
                else:
                    low = low + 1
                # 比较mindiff和当前计算差值的绝对值
                if abs(mindiff) > abs(target - cursum):
                    # 每次记录的都是target - 当前三数之和
                    mindiff = target - cursum
        return target - mindiff


if __name__ == '__main__':
    s = Solution()
    test_data = [([-1, 2, 1, -4], 1), ([0, 1, 2], 3)]
    test_res = [2]
    for i in test_data:
        print(s.threeSumClosest(i[0], i[1]))
