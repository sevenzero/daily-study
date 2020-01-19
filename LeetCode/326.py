#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/8 9:19
@Author  : duanpy001
@File    : 326.py
@Link    : https://leetcode-cn.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n != 1:
            n, remainder = divmod(n, 3)
            if remainder != 0:
                return False
            elif n == 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    test_data = [27, 0, 9, 45]
    for i in test_data:
        print(s.isPowerOfThree(i))
