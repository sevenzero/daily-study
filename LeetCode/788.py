#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/8 11:21
@Author  : duanpy001
@File    : 788.py
@Link    : https://leetcode-cn.com/problems/rotated-digits/
"""
class Solution:
    def rotatedDigits(self, N: int) -> int:
        return len([i for i in range(1, N + 1) if not any([d for d in str(i) if int(d) in (3, 4, 7)]) and any(
            [d for d in str(i) if int(d) in (2, 5, 6, 9)])])
if __name__ == '__main__':
    s = Solution()
    print(s.rotatedDigits(100))
